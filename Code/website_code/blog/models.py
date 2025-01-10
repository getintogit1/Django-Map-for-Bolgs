from django.db import models


from django.db.models.signals import pre_save
from django.utils.text import slugify  
from django.conf import settings
from django.db.models.signals import post_delete
from django.dispatch import receiver
# Create your models here.

def upload_location(instance, filename, **kwargs):
    file_path = 'blog/{author_id}/{title}-{filename}'.format(author_id = str(instance.author.id), title = str(instance.title), filename = filename)
    return file_path

class BlogPost(models.Model):
    title                   = models.CharField(max_length = 50, null = False, blank=False)
    body                    = models.TextField(max_length = 5000, null = False, blank=False)
    image                   = models.ImageField(upload_to=upload_location, null = False, blank=False)
    date_published          = models.DateTimeField(auto_now_add = True, verbose_name="date_published")
    date_updated            = models.DateTimeField(auto_now = True, verbose_name="date_updated")
    author                  = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) #in settings our autuser model is set to our account model. on_delete we define what happens when this blog post gets deleted. dont delete the author that is accosiated but all other items that are associated with it
    slug                    = models.SlugField(blank = True, unique=True)

    
    def __str__(self):
        return self.title

@receiver(post_delete, sender = BlogPost)
def submission_delete(sender, instance, **kwargs):
    instance.image.delete(False) #if the blog post gets deleted i also want to delete teh image associated with it 

def pre_save_blog_post_receiver(sender, instance, **kwargs): #gets calle dbefore the blogpost gets posted to the database 
    if not instance.slug:
        instance.slug = slugify(instance.author.username + "-" + instance.title)

pre_save.connect(pre_save_blog_post_receiver, sender = BlogPost)