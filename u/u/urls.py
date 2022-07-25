"""u URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import re_path as url
from django.contrib import admin
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt

from graphene_django.views import GraphQLView
from .settings import (SITE_NAME,DEBUG)

admin.site.site_header = SITE_NAME
admin.site.site_title = f"{SITE_NAME} Portal"
admin.site.index_title = f"Welcome to {SITE_NAME} Portal"

urlpatterns = [
    path("site-admin/", admin.site.urls),
    path("ql-query/", csrf_exempt(GraphQLView.as_view(graphiql=True))),
]

if DEBUG:
    import debug_toolbar

    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
