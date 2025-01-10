from django.urls    import path
from blog.views     import(
    create_blog_view,
    detail_blog_view,
    edit_blog_view,
    delete_blog_view
)

app_name = 'blog' # required
urlpatterns= [
    path('create', create_blog_view, name= 'create'),
    path('<slug>', detail_blog_view, name= 'detail'),                           #url will be .../blog/slug/...
    path('<slug>/edit', edit_blog_view, name= 'edit'),                          #url will be .../blog/slug/...
    path('<slug:slug>/delete/', delete_blog_view, name='delete'),  # Add this line


]

