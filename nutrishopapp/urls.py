
from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  path('',views.home,name='home'),
  path('services/',views.services,name='services'),
  path('about/',views.about,name='about'),
  path('supplement/',views.supplement,name='supplement'),
  path('product/<int:post_id>',views.product,name='product')
   
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)