from django.db import models

class Color(models.Model):
    color = models.CharField()

    def __str__(self):
        return self.color

class Engine(models.Model):
    engine = models.FloatField()
    
    def __str__(self):
        return f"{self.engine}"
    
class Equipment(models.Model):
    equipment = models.CharField()

    def __str__(self):
        return self.equipment

class Car(models.Model):
    name = models.CharField(max_length=20)
    base_price = models.IntegerField()
    image_url = models.URLField()
    no_background_image = models.CharField()

    def __str__(self):
        return self.name