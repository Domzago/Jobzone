from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_view
from job import views

urlpatterns = [
    path('', include('job.urls')),
    path('signup/', views.signup, name='signup'),
    path('login/', views.loginuser, name='login'),
    path('apply/', views.apply, name='apply'),
    path('admin/', admin.site.urls),
    path('logout/', auth_view.LogoutView.as_view(template_name='logout.html'), name='logout'),

] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
