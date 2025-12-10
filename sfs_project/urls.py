from django.contrib import admin
from django.urls import path
from sfsapp.views import home,create,locate,delete
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",home,name="home"),
    path("create",create,name="create"),
    path("delete/<int:i>",delete,name="delete"),
    path("locate",locate,name="locate"),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
