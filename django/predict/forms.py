from django import forms
from predict.models import Prediction


class PredictionInputForm(forms.ModelForm):
    class Meta:
        model = Prediction
        fields = ["sepal_length", "sepal_width", "petal_length", "petal_width"]
