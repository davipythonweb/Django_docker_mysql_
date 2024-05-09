
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', lambda x: HttpResponse(
        '<center><h1 style="color:green;font-size:3rem;font-family: Gill Sans Extrabold, sans-serif;margin-top:250px;border:50px solid black;border-radius:8px;">Container Docker com bancon Mysql + Framework Django!</h1></center>'
    ))
]
