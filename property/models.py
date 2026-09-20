from django.db import models



class Agent(models.Model):
    image = models.ImageField(upload_to='agents/')

    def __str__(self):
        return str(self.image)
