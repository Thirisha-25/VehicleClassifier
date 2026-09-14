from django.db import models

class PredictionHistory(models.Model):
    engine_size = models.FloatField()
    horsepower = models.IntegerField()
    weight = models.IntegerField()
    doors = models.IntegerField()
    seats = models.IntegerField()
    fuel = models.CharField(max_length=20)
    prediction = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.prediction} - {self.created_at.strftime('%Y-%m-%d %H:%M')}"