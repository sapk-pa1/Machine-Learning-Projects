import streamlit as st 
import pickle 
import pandas as pd 
movies_dict = pickle.load(open('..\data\processed\movies_dict.pkl', 'rb'))
similarity = pickle.load(open('../data/processed/similarity.pkl', 'rb'))

def recommend(movie): 
    
    movie_index = movies[movies['title']==movie]. index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse =True, key= lambda x: x[1])[1:6]
    recommended_movies = []
    for i in movies_list: 
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies



movies = pd.DataFrame(movies_dict)
movies_list = movies['title'].values

st.title("Movie Recommender System ")
selected_movie_name = st.selectbox("Movie Name ", movies_list)
if st.button("Recommend"): 
    recommendation = recommend(selected_movie_name)
    for i in recommendation: 
        st.write(i)