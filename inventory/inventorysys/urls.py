from django.conf.urls import url
from django.urls import path, include
from . import api_urls

from .views import *

urlpatterns = [
    url(r'^$', index, name='index'),

    path('Device/', include('inventorysys.api_urls')),

    url(r'^display_laptops$', laptops, name='laptops'),
    url(r'^display_desktops$', desktops, name='desktops'),
    url(r'^display_mouse$', mouses, name='mouses'),
    url(r'^display_pendrives$', pendrives, name='pendrives'),
    url(r'^display_disks$', disks, name='disks'),

    url(r'^add_laptop$', add_Laptop, name='add_Laptop'),
    url(r'^add_desktop$', add_Desktop, name='add_Desktop'),
    url(r'^add_Mouse$', add_Mouse, name='add_Mouse'),
    url(r'^add_Pendrive$', add_Pendrive, name='add_Pendrive'),
    url(r'^add_Disk$', add_Disk, name='add_Disk'),

    url(r'^edit_laptop/(?P<pk>\d+)$', edit_laptop, name='edit_laptop'),
    url(r'^edit_desktop/(?P<pk>\d+)$', edit_desktop, name='edit_desktop'),
    url(r'^edit_mouse/(?P<pk>\d+)$', edit_mouse, name='edit_mouse'),
    url(r'^edit_pendrive/(?P<pk>\d+)$', edit_pendrive, name='edit_pendrive'),
    url(r'^edit_disk/(?P<pk>\d+)$', edit_disk, name='edit_disk'),

    url(r'^delete_laptop/(?P<pk>\d+)$', delete_laptop, name='delete_laptop'),
    url(r'^delete_desktop/(?P<pk>\d+)$', delete_desktop, name='delete_desktop'),
    url(r'^delete_mouse/(?P<pk>\d+)$', delete_mouse, name='delete_mouse'),
    url(r'^delete_pendrive/(?P<pk>\d+)$', delete_pendrive, name='delete_pendrive'),
    url(r'^delete_disk/(?P<pk>\d+)$', delete_disk, name='delete_disk'),

]
