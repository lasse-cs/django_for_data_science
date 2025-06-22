from django.conf import settings
from django.shortcuts import render
import joblib
import numpy as np

from predict.forms import PredictionInputForm


model = joblib.load(settings.MODEL_DIR / "iris.joblib")


def predict_view(request):
    """
    View to handle prediction requests.
    """
    if request.method == "POST":
        form = PredictionInputForm(request.POST)
        if form.is_valid():
            prediction = form.save(commit=False)
            features = np.array(
                [
                    [
                        prediction.sepal_length,
                        prediction.sepal_width,
                        prediction.petal_length,
                        prediction.petal_width,
                    ]
                ]
            )
            prediction.species = model.predict(features)[0]
            prediction.save()
    else:
        prediction = None
        form = PredictionInputForm()
    return render(
        request,
        "predict/predict.html",
        context={
            "form": form,
            "prediction": prediction,
        },
    )
