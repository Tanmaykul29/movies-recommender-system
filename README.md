# movies-recommender-system
**Movie Recommender System using Streamlit and TMDB Dataset**

# Introduction

This project implements a Movie Recommender System using Streamlit, a Python library for creating web applications, and the TMDB (The Movie Database) dataset from Kaggle. The system recommends movies to users based on their selected movie preferences. The recommendation algorithm employs collaborative filtering to find similar movies and provide personalized movie suggestions to users.

# Overview

**1. Data Acquisition:**
   The project starts by obtaining the TMDB dataset from Kaggle, which contains information about thousands of movies, including details like titles, genres, cast, and user ratings.

**2. Data Preprocessing:**
   The dataset is preprocessed to create a movie dictionary and calculate movie similarity. This preprocessing step is crucial for efficient recommendation generation.

**3. Building the Recommender System:**
   - The user interacts with the system by selecting a movie from a dropdown menu.
   - Upon selecting a movie, the system employs collaborative filtering to identify similar movies.
   - The top five similar movies are recommended to the user.
   - Movie posters and titles are displayed in columns for easy viewing.

**4. Customization:**
   - The project allows customization of the system's title and favicon.
   - The title is set as "Recommender System," and the favicon is set as a rocket emoji.

# Technologies Used

- **Streamlit:** Streamlit is used to create the user interface for the recommender system. It simplifies web app development by allowing developers to create interactive apps with Python.

- **Pandas:** Pandas is utilized for data manipulation and analysis, making it easier to work with the TMDB dataset.

- **Requests:** The Requests library is used to fetch movie poster images from the TMDB API.

# Usage

Users can access the Movie Recommender System via the Streamlit web interface. They can:
- Select a movie from the dropdown menu.
- Click the "Recommend" button to receive personalized movie recommendations.
- View recommended movies along with their posters.

# Customization

The project's title is set as "Recommender System," and the favicon is a rocket emoji. Users can easily customize these by modifying the `st.set_page_config()` function in the code.

# Deployment

To deploy this project, follow these steps:
1. Install the necessary Python libraries (Streamlit, Pandas, Requests).
2. Obtain the TMDB dataset from Kaggle and preprocess it as shown in the code.
3. Host the application on a server or platform of your choice.
4. Allow users to access the recommender system via a web interface.

# Conclusion

This Movie Recommender System provides an interactive and personalized movie recommendation experience for users based on their selected movies. It leverages Streamlit's simplicity and the TMDB dataset's extensive movie information to deliver relevant suggestions. The system's customization options make it adaptable to various use cases, and it can be deployed to share movie recommendations with a broader audience.
