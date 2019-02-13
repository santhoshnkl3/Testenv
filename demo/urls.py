
from django.urls.conf import path
from . import views
urlpatterns=[
    
    path('card/',views.home,name="card"),
    path('home/',views.home1,name="grid")
    ]