import requests
import streamlit as st
import pickle
import pandas as pd


# Function to fetch the movie poster from TMDB API
def fetch_poster(movie_id):
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=066094f34fc7afdf8efd40538ec212c4'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
    else:
        return "https://via.placeholder.com/500x750?text=Poster+Not+Available"


# Function to recommend movies
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]

    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        # Fetch poster from API
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters


# Load preprocessed movie data
movies_dict = pickle.load(open('movie_dict.pkl', "rb"))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', "rb"))

# Streamlit App Configuration
st.set_page_config(page_title="Movie Recommender", layout="wide")
st.title("\U0001F3AC Movie Recommender System")
st.markdown("<style>body { background-color: #f5f5f5; }</style>", unsafe_allow_html=True)

# Dropdown to select a movie
selected_movie_name = st.selectbox(
    'Choose a movie you like:',
    movies['title'].values,
    help="Select a movie to see recommendations."
)

# Recommend button
if st.button('Recommend'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie_name)

    # Display Recommendations
    st.subheader(f"Movies similar to **{selected_movie_name}**:")

    cols = st.columns(5)
    for idx, col in enumerate(cols):
        with col:
            st.image(recommended_movie_posters[idx], caption=recommended_movie_names[idx], use_container_width=True)

# Footer
st.markdown("""
<hr style="border: 1px solid #eee;">
<div style="text-align: center; font-size: 14px; color: #555;">
    Developed By <strong>M.Abdulrehman Baig</strong> ❤️ using <strong>Streamlit</strong>
</div>
""", unsafe_allow_html=True)

