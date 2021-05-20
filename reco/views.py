from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from reco.forms import IngredientInputForm
from reco.models import *
from reco.cos_sim import recommend


def mainpage(request):

    return render(request, 'reco/main.html',{})


def result(request):

    print('**********')
    print(request.POST)
    print('**********')
    ingre = request.POST['ingredients[]']
    print(ingre)

    top7_reco = recommend(ingre)

    selected_3_choice = []
    selected_4_choice = []

    for id in top7_reco[:3]:
        selected_3_choice.append(Recipe_info.objects.get(recipe_id=id))
    print(selected_3_choice)
    for id in top7_reco[3:]:
        selected_4_choice.append(Recipe_info.objects.get(recipe_id=id))
    print(selected_4_choice)
    context = {'ingredients':ingre,'reco_3_recipe':selected_3_choice,'reco_4_recipe':selected_4_choice}

    return render(request,'reco/result.html',context)


def detail(request, recipe_id) :
    try :
        recipe_choice = get_object_or_404(Recipe_info, recipe_id = recipe_id)
    except :
        # 구현 필요 부분
        context = {'error_message' : "선택된 레시피가 없습니다."}
        return render(request, "reco/index.html", context)
    else :
        # ingredient-unit split
        recipe_choice.ingredients = recipe_choice.ingredients[:-1] # 마지막 "|" 삭제
        ingredients_list = recipe_choice.ingredients.split("|")

        ingredients = {}
        chknum = 0
        for idx, str in enumerate(ingredients_list) :
            if  idx % 2 == 0 :
                ingredients_str = ingredients_list[idx] + " " + ingredients_list[idx + 1]
                ingredients[chknum] = ingredients_str
                chknum += 1

        recipe_choice.ingredients = ingredients

        # recipe split
        recipe_choice.recipes = recipe_choice.recipes[:-1] # 마지막 "|" 삭제
        recipes_list = recipe_choice.recipes.split("|")
        recipes = {}
        for idx, str in enumerate(recipes_list) :
            recipes[idx] = str

        recipe_choice.recipes = recipes

        context = {"recipe_choice" : recipe_choice}
        return render(request, "reco/detail.html", context)
