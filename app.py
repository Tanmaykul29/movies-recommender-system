import streamlit as st
import pickle
import pandas as pd
import requests

st.set_page_config(
    page_title="Recommender System",
    page_icon="🚀",  # You can use a URL to an image file here
)
st.title('Movie Recommender System')

movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# kaggel dataset: https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata?resource=download&select=tmdb_5000_movies.csv


def recommend(selected_movie):
    movie_index = movies[movies['title'] == selected_movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:6]

    recommended_movies, posters = [], []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].id
        posters.append(fetch_poster(movie_id))
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies,posters


def fetch_poster(movie_id):
    # poster_path
    response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=35f3417b2c6553c105d2f81f176e306c&language=en-US')
    data = response.json()
    print(data)
    return "https://image.tmdb.org/t/p/w500/"+data['poster_path']


movies = pd.DataFrame(movies_dict)


selected_movie_name = st.selectbox(
    'Select a movie',
    movies['title'].values
)

if st.button('Recommend'):
    movie, posters = recommend(selected_movie_name)
    # for movie in recommendations:
    #     st.write(movie)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(movie[0])
        st.image(posters[0])
    with col2:
        st.text(movie[1])
        st.image(posters[1])
    with col3:
        st.text(movie[2])
        st.image(posters[2])
    with col4:
        st.text(movie[3])
        st.image(posters[3])
    with col5:
        st.text(movie[4])
        st.image(posters[4])