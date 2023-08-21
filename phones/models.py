from django.db import models
from django.utils.text import slugify
class Phone(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=255, unique=True)
    price = models.IntegerField()
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    release_date = models.DateField(auto_now=False, auto_now_add=False)
    lte_exists = models.BooleanField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Phone, self).save(*args, **kwargs)

    # def __str__(self):
    #     return self.name