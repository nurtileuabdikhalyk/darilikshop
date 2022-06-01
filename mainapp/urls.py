from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),

    path('dariler/', dariler, name='dariler'),
    path('dariler/<slug:slug>/', daridetails, name='daridetails'),
    path('dariler/create', dari_create, name='dari-create'),
    path('dariler/adddari', adddari, name='adddari'),
    path('dariler/<slug:slug>/delete', DariDeleteView.as_view(), name='dariler-delete'),
    path('dariler/<slug:slug>/update', DariUpdateView.as_view(), name='dariler-update'),

    path('scientists/', scientists, name='scientists'),
    path('scientists/<slug:slug>/', scientistsdetails, name='scientistsdetails'),
    path('scientists/<slug:slug>/delete', ScientistsDeleteView.as_view(), name='scientists-delete'),
    path('scientists/create', scientist_create, name='scientist-create'),
    path('scientists/<slug:slug>/update', ScientistsUpdateView.as_view(), name='scientists-update'),

    path('scientist_or_dari', scientist_or_dari, name='scientist_or_dari'),
    path('contact/', contact, name='contact'),
    path("addreview/", addreview, name="addreview"),
]
