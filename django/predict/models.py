from django.db import models


class Prediction(models.Model):
    class SpeciesChoices(models.TextChoices):
        SETOSA = "Iris-setosa"
        VERSICOLOR = "Iris-versicolor"
        VIRGINICA = "Iris-virginica"

    sepal_length = models.FloatField()
    sepal_width = models.FloatField()
    petal_length = models.FloatField()
    petal_width = models.FloatField()
    species = models.CharField(max_length=20)

    def __str__(self):
        return f"Prediction({self.id})"
