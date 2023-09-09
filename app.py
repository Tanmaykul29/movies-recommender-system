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


def recommend(selected_movie, num_recommendations):
    movie_index = movies[movies['title'] == selected_movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[0:num_recommendations]

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

num_recommendations = st.slider('Select the number of recommendations to display', 1, 20)

if st.button('Recommend'):
    movie, posters = recommend(selected_movie_name,num_recommendations)

    # Limit the number of recommendations based on user's selection
    num_recommendations = min(len(movie), num_recommendations)

    # Determine the number of rows required based on num_recommendations and max 3 columns per row
    num_rows = (num_recommendations - 1) // 3 + 1

    for row in range(num_rows):
        cols = st.columns(3)  # Create 3 columns for each row

        for col in range(3):
            index = row * 3 + col
            if index < num_recommendations:
                with cols[col]:
                    st.text(movie[index])
                    st.image(posters[index])
