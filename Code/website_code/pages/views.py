# pages/views.py

from django.shortcuts       import render, redirect
from attractions.models     import Attraction                                   # Import the attraction model

#import for blog screen page:
from django.shortcuts       import render
from account.models         import Account
from operator               import attrgetter                                   #sort the list, query all the blogpost
from django.core.paginator  import EmptyPage, PageNotAnInteger, Paginator

from blog.models            import BlogPost
from blog.views             import get_blog_queryset

#NOTE: Kontakt View
from attractions.views      import get_attractions_query_set
from website_code.forms     import *                                            # import our contakt form for email backend , in "kontakt.html"
from django.core.mail       import send_mail, BadHeaderError                    # neccesary for backend emails endig handling
from django.http            import HttpResponse                                 

BLOG_POST_PER_PAGE = 10
attractionS_PER_PAGE = 6

def home_screen_view(request):
   
    Attractions = list(Attraction.objects.values())                             # Retrieve all attractions values to use adresses for homepage map
    #print(Attractions)
    #return render(request, "pages/home.html", {'attractions': attractions})
    context = {}
    query = ""
    if request.GET:
        query = request.GET.get('q','')                                         #search for q , if tehre is a q than pass it 
        context['query'] = str(query)
 
    attractions = sorted(get_attractions_query_set(query), key=attrgetter('title'), reverse=True) 
    
                                                                                # getting the desired page number from url
    page_number = request.GET.get('page', 1)
    attractions_paginator = Paginator(attractions, attractionS_PER_PAGE)        # creating a paginator object
    
    try:
        attractions = attractions_paginator.get_page(page_number)               # returns the desired page object
    except PageNotAnInteger:
                                                                                # if page_number is not an integer then assign the first page
        attractions = attractions_paginator.page(attractionS_PER_PAGE)
    except EmptyPage:
                                                                                # if page is empty then return last page
        attractions = attractions_paginator.page(attractions_paginator.num_pages)
    context['attractions'] = attractions
    context['Attractions'] = Attractions                                        # important to add all backends to context, so js have access to it 
                                                                                # sending the page object to index.html
    return render(request, "pages/home.html", context)


def blog_page_view(request):
                                                                                # Accessing request headers
    #print(request.META)
    context = {}

    query = ""
    if request.GET:
        query = request.GET.get('q','')                                         #search for q , if tehre is a q than pass it 
        context['query'] = str(query)
 
    blog_posts = sorted(get_blog_queryset(query), key=attrgetter('date_updated'), reverse=True) 
    

                                                                                #PAGINATION is always the same, -> django docs
    page = request.GET.get('page', 1)
    blog_posts_paginator = Paginator(blog_posts, BLOG_POST_PER_PAGE)

    try:
        blog_posts=blog_posts_paginator.page(page)
    except PageNotAnInteger:
        blog_posts = blog_posts_paginator.page(BLOG_POST_PER_PAGE)
    except EmptyPage:
        blog_posts = blog_posts_paginator.page(blog_posts_paginator.num_pages)

    context['blog_posts'] = blog_posts

                                                                                # Rendering the template with the context
    return render(request, "pages/blog_page.html", context)



def kontakt_page_view(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():                                                     # backend check valid form
			subject = "Website Inquiry" 
			body = {
			'first_name': form.cleaned_data['first_name'],                      # retrieve typed in input from user
			'last_name': form.cleaned_data['last_name'], 
			'email': form.cleaned_data['email_address'], 
			'message':form.cleaned_data['message'], 
			}
			message = "\n".join(body.values())

			try:
				send_mail(subject, message, 'admin@example.com', ['admin@example.com']) 
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			return redirect ("home")                                            # redirect to homepage after succesful sending
      
	form = ContactForm()
	return render(request, "pages/kontakt.html", {'form':form})                 #POST filled out contact form, render komtakt.html
    


def impressum_page_view(request):
    return render(request, "pages/impressum.html")


def datenschutz_page_view(request):
    return render(request, "pages/datenschutz.html")