"""coopvirtual URL Configuration

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
from user import views
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login_inicial),
    path('login/submit', views.submit_login),
    path('logout/', views.logout_user),
    path('', views.principal_coop),
    path('index/', views.index),
    path('teste/', views.teste),
    path('cadastro/', views.cadastro),
    path('cadastro_oferta/', views.cadastro_oferta),
    path('cadastro_oferta/submit', views.set_oferta),
    path('cadastro/submit', views.cadastro_submit),
    path('meus_imoveis/', views.meus_imoveis),
    path('detalhes/<id>/', views.detalhes),
    path('delete/<id>/', views.delete),
    path('detalhes/<id>/pdf', views.pdf),
    path('detalhes/<id>/email', views.detalhes_submit),


]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)