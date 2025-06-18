"""
URL configuration for mysite attraction.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoattraction.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib          import admin
from django.urls             import path, include
from django.contrib.auth     import views as auth_views
from django.conf             import settings
from django.conf.urls.static import static  # Add this import


from  pages.views import (
    blog_page_view,
    home_screen_view,
    kontakt_page_view,
    impressum_page_view,
    datenschutz_page_view
    )
from  account.views import (
    registration_view, 
    logout_view,
    login_view,
    account_view, 
    must_authenticate_view
    )

from attractions.views        import ( attraction_detail, attraction_index)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls', 'blog')),                                #now and urls for blog will start with blog and than whatever
    path('blog_page/', blog_page_view, name = 'blog_page'),
    path('register/', registration_view, name = 'register'),
    path('logout/', logout_view, name = 'logout'),
    path('login/', login_view, name = 'login'),
    path('account/', account_view, name = 'account'),
    path('must_authenticate/', must_authenticate_view, name = 'must_authenticate'),
    path('', home_screen_view, name = 'home'),
    path('kontakt/', kontakt_page_view, name = 'kontakt'),
    path('impressum/', impressum_page_view, name = 'impressum'),
    path('datenschutz/', datenschutz_page_view, name = 'datenschutz'),
    #path('attractions/<int:pk>/', attraction_detail, name='attraction_detail'),
    path('attractions/<slug:slug>/', attraction_detail, name='attraction_detail'),

    # Password reset links (ref: https://github.com/django/django/blob/master/django/contrib/auth/views.py)
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), 
    name='password_change_done'),
    #we define some urls, what happens when i change/reset etc my password
    # im referencing the customd django views that django has (ref link)
    # inside the django source code views, i gonna referennce templates i am going to build
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'), 
    name='password_change'),

    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'),
    name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),
    name='password_reset_confirm'),
    
    path('password_reset/', auth_views.PasswordResetView.as_view(), 
    name='password_reset'),
    
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
    name='password_reset_complete'),
]

#telling the attraction where the static, media , static_cdn, media_cdn url
if settings.DEBUG: 
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# created 2 blog posts, why are they saved in media_contend_deliveryng_network _cdn?
# this folder is imitating my media content delivering network , in real production it would be save din my media server liek amazon webservice 

# when i put image in my static folder, and run ' python manage.py collectstatic it pushes all files fromm static folder to 
# static_contentdelivery network, in dev environment in production env it would get pushed to webservice 
