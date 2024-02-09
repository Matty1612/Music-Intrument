from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("team", views.team, name="team"),
    path("instruments", views.instruments, name="instruments"),
    path("realtime/drums", views.real_drums, name="real-drums"),
    path("realtime/trumpet", views.real_trumpet, name="real-trumpet"),
    path("realtime/trombone", views.real_trombone, name="real-trombone"),
    path("realtime/xylophone", views.real_xylophone, name="real-xylophone"),
    path("realtime/cymbal", views.real_cymbal, name="real-cymbal"),
    path("realtime/piano", views.real_piano, name="real-piano"),
    path("realtime/guitar", views.real_guitar, name="real-guitar"),
    path("skeleton", views.skeleton, name="skeleton")
]
