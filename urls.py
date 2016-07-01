 from django.conf.urls import include, url
from django.contrib import admin
from signups import views

urlpatterns = [
    
    url(r'^$',views.home),
    url(r'^admin/', include(admin.site.urls)),
]
