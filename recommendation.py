import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def results(movie_name):
    movie_name = movie_name.lower()
    movie_data = pd.read_csv('Appdata/Movie_dataset.csv')
    movie_data = movie_data.drop(['Unnamed: 0','genres','overview','production_companies'],axis=1)
    #movie_data = movie_data.iloc[:100]

    if movie_name not in movie_data['title'].unique():
        return 'Movie not in Database'
    else:
        cv = CountVectorizer(stop_words='english')
        count_matrix = cv.fit_transform(movie_data['combined_features'])
        cosine_sim = cosine_similarity(count_matrix)

        movie_index = movie_data[movie_data.title == movie_name]['index'].values[0]

        similar_movies = list(enumerate(cosine_sim[movie_index]))
        sorted_similar_movies = sorted(similar_movies,key=lambda x:x[1],reverse=True)

        result=[]
        score=[]
        i=0
        for element in sorted_similar_movies:
            if movie_data[movie_data.index == element[0]]["title"].values[0] == movie_name:
                pass
            else:
                result.append(movie_data[movie_data.index == element[0]]["title"].values[0])
                score.append(round(element[1],2))
                i=i+1
                if i>9:
                    break
        
        zip_iterator = zip(result, score)
        res_dct = dict(zip_iterator)

        return res_dct
    