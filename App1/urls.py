# from django.urls import path
# from . import views

# urlpatterns = [
#     path("", views.index_entity, name="index"),
#     # path("about/", views.about_entity, name="about"),
# ]


# .........

from django.urls import path
from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("about/", views.AboutView.as_view(), name="index"),
]
