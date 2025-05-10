
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('<slug:slug>/<slug:slug2>', views.ArticleView.as_view(), name="article"),
    path('<slug:slug>', views.ArticlesView.as_view(), name="articles"),
    path('', views.HelpcenterView.as_view(), name="helpcenter"),    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
