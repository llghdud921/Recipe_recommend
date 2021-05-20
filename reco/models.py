from django.db import models

# Create your models here.
class Recipe_info(models.Model):

    recipe_id = models.IntegerField(default=0, unique=True, primary_key=True)
    type = models.CharField(max_length = 50, default = '')
    titles = models.CharField(max_length = 200, default = '') # recipe_name, title
    comment = models.TextField(default = '')
    images = models.CharField(max_length = 200, default = '') # recipe_main_image_url
    serves = models.CharField(max_length = 50, default = '') # food serves
    cooking = models.CharField(max_length = 50, default = '') # cooking time
    recipes = models.TextField(default = '')
    ingredients = models.TextField(default = '')


class Recipe_token(models.Model):

    recipe = models.ForeignKey('Recipe_info', on_delete=models.CASCADE)
    clean_words = models.TextField()