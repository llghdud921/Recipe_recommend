# Generated by Django 3.2.2 on 2021-05-18 04:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reco', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe_token',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reco.recipe_info'),
        ),
    ]