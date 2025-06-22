from django.contrib import admin
from predict.models import Prediction


@admin.register(Prediction)
class PredictionAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "sepal_length",
        "sepal_width",
        "petal_length",
        "petal_width",
        "species",
    )
