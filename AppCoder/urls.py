from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path("", inicio),
    path("about/", about),
    path("latestWork/", latestWork),
    path("comunidad/", comunidad),
    path("contacto/", contacto),


]
