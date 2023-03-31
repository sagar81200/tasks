from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('',views.index,name="index"),
    path('register',views.register,name="register"),
    path('login',views.login_me,name="login"),
    path('about',views.about,name="about"),
    path('contact',views.contact,name="contact"),
    path('profile',views.profile,name="profile"),
    path('myblog',views.myblog,name="myblog"),
    path('blog',views.blog,name="blog"),
    path('write',views.write,name="write"),
    path('details',views.details,name="details"),
    path('accounts/', include('allauth.urls')),

    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)