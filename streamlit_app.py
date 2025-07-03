import pickle
import streamlit as st # type: ignore

# Load Data
movies = pickle.load(open('pickle_file\movie_list.pkl', 'rb'))
similarity = pickle.load(open('pickle_file\similarity.pkl', 'rb'))

# Recommend Function
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(
        list(enumerate(similarity[index])),
        reverse=True,
        key=lambda x: x[1]
    )
    recommended_movie_names = []
    for i in distances[1:6]:
        recommended_movie_names.append(movies.iloc[i[0]].title)
    return recommended_movie_names

# Streamlit UI
st.set_page_config(page_title=" Movie Recommender", layout="wide")
st.markdown("# Movie Recommendation System")
st.markdown("Get similar movies based on your favorite one.")

# Movie Selection
movie_list = movies['title'].values
selected_movie = st.selectbox(" Select a movie you like:", movie_list)

# Recommendation Display
if st.button(" Show Recommendations"):
    recommended_movie_names = recommend(selected_movie)
    st.subheader(" Top 5 Recommendations for You:")
    cols = st.columns(5)
    for idx, col in enumerate(cols):
        col.markdown(f"### #{idx+1}")
        col.success(f"**{recommended_movie_names[idx]}**")
