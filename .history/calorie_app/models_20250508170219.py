from django.db import models

class Food(models.Model):
    name = models.CharField(max_length=100)
    calories = models.PositiveIntegerField()
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.calories} kcal)"
