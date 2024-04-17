from django.urls import path
from . import views
from project3 import settings
from django.conf.urls.static import static

urlpatterns = [
     path("home",views.home,name="home"),
     path("calc",views.calc,name="calc"),
     path("result",views.result,name="result"),
     path("calc2",views.calc2,name="calc2"),
     path("result_post",views.result_post,name="result_post"),
     path("add_category",views.add_category,name="add_category"),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)