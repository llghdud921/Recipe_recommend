# from django.shortcuts import get_object_or_404
# import os
# import django
# import csv
# import sys
#
# # system setup
# os.chdir('.')
# print('Current dir의 경로 : ', end=''), print(os.getcwd())  # os가 파악한 현재 경로를 표기
# print('os.path.abspath(__file__)의 경로 : ', os.path.abspath(__file__))  # 현재 작업중인 파일을 포함 경로를 구체적으로 표기
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print('BASE_DIR=', end=''), print(BASE_DIR)
# print('똑같나? 다르나?', BASE_DIR == os.getcwd())  # 소문자 c , 대문자 C 차이 때문인것 같네요.
#
# sys.path.append(BASE_DIR) # sys 모듈은 파이썬을 설치할 때 함께 설치되는 라이브러리 모듈이다. sys에 대해서는 뒤에서 자세하게 다룰 것이다. 이 sys 모듈을 사용하면 파이썬 라이브러리가 설치되어 있는 디렉터리를 확인할 수 있다.
#
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'reco_recipe.settings')
# # python이 실행될 때 DJANGO_SETTINGS_MODULE라는 환경 변수에
# # 현재 프로젝트의 settings.py 파일 경로를 등록
# django.setup()

from reco.views import *
from reco.models import Recipe_token
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import pandas as pd

def recommend(input):
    info_token_df = pd.DataFrame(list(Recipe_token.objects.all().values()))

    # Tfidf Vectorizer
    vec = TfidfVectorizer(min_df=0, ngram_range=(1,3))
    vec_description = vec.fit_transform(info_token_df['clean_words'])
    vec_user_input = vec.transform([input])

    # description 기준으로 input 값 유사도 비교
    vec_sim = cosine_similarity(vec_description, vec_user_input)

    info_token_df['tfidf_vec'] = vec_sim

    # TfidfVectorizer 유사도 높은 순으로 정렬
    sim_df = info_token_df.sort_values(by='tfidf_vec', ascending=False)
    sim_df.reset_index(drop=True, inplace=True)

    top_3_titles = sim_df['recipe_id'][0:7]

    return list(top_3_titles)



