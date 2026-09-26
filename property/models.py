from django.db import models
from django.utils.text import slugify


class Property(models.Model):
    house_name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    location = models.CharField(max_length=300)
    price = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )
    area = models.PositiveIntegerField(
        help_text="Area in square feet"
    )
    bedrooms = models.PositiveIntegerField(default=0)
    bathrooms = models.PositiveIntegerField(default=0)
    year_built = models.PositiveIntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='properties/', blank=True, null=True)
    owner = models.ForeignKey('Owner',on_delete=models.SET_NULL,null=True,blank=True,related_name='properties')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.house_name)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.house_name

    class Meta:
        ordering = ['-created_at']



class Owner(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=30)
    whatsapp = models.CharField(max_length=30)
    image = models.ImageField(upload_to='owner_images/',blank=True,null=True)

    def __str__(self):
        return self.name


class PropertyImage(models.Model):
    property = models.ForeignKey(Property,on_delete=models.CASCADE,related_name='images')
    image = models.ImageField(upload_to='properties_detail/')

    def __str__(self):
        return f"{self.property.house_name} - Image"


class Agent(models.Model):
    image = models.ImageField(upload_to='agents/')

    def __str__(self):
        return str(self.image)
