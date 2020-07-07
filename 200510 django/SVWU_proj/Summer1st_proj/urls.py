"""Summer1st_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import s1app.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',s1app.views.home,name='home'),
    path('detail/<int:detail_id>',s1app.views.detail, name="detail"),
    path('create/',s1app.views.create,name="create"),
    path('change/<int:change_id>',s1app.views.change, name="change"),
    path('delete/<int:delete_id>',s1app.views.delete, name="delete"),
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)