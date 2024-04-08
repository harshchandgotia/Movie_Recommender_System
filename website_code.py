import streamlit as st
import pickle 
import pandas as pd

similarity = pickle.load(open('similarity.pkl','rb'))
movie_list1 = pickle.load(open('movies.pkl','rb'))
movie_list = movie_list1['title'].values
movies =  pd.DataFrame(movie_list1) 
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    
    recommended = []

    for i in movies_list:
        recommended.append(movies.iloc[i[0]].title)
    return recommended
st.title("Movie Recommender System")

option = st.selectbox('mention a movie',movie_list)

if st.button('Recommend'):
    recomm = recommend(option)
    for i in recomm:
        st.write(i)