from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('profiles/', include('profiles.urls')),
    path('lettings/', include('lettings.urls')),
]

handler404 = 'oc_lettings_site.views.custom_page_not_found_view'
handler500 = 'oc_lettings_site.views.custom_server_error_view'
