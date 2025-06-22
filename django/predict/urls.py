from django.urls import path

from predict import views


urlpatterns = [
    path("", views.predict_view, name="predict_view"),
]
