from django import forms

class IngredientInputForm(forms.Form):
    Ingredient_1 = forms.CharField(max_length=10)
    # Ingredient_2 = forms.CharField(max_length=10)
    # Ingredient_3 = forms.CharField(max_length=10)
