import pickle
import streamlit as st
import requests


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/



#--- FETCHING MOVIE POSTER USING API

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=ff1edc228ea8fb5ef32fafdd035330e2".format(movie_id)
   
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/original" + poster_path
    return full_path


# -- FETCHING THE MOVIE RECOMMENDED MOVIE TITLE---
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:11]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names,recommended_movie_posters

st.set_page_config(page_title='Movie Recommender System',layout="wide")
st.subheader("Hi, I am Prasant Poudel:wave:")
st.write("Small Project :panda_face:")
st.header('Movie Recommender System:clapper:')

 #-- Pickle loading -----

movies = pickle.load(open('movie.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

movie_list = movies['title'].values

#-- DROPDOWN BOX
selected_movie = st.selectbox("Type or select a movie from the dropdown",movie_list)

#--- Display part----
if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
    # col1, col2, col3, col4, col5,col6,col7,col8,col9,col10 = st.columns(10)
    col1, col2, col3, col4, col5=st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])
    col6,col7,col8,col9,col10 = st.columns(5)
    with col6:
        st.text(recommended_movie_names[5])
        st.image(recommended_movie_posters[5])
    with col7:
        st.text(recommended_movie_names[6])
        st.image(recommended_movie_posters[6])
    with col8:
        st.text(recommended_movie_names[7])
        st.image(recommended_movie_posters[7])
    with col9:
        st.text(recommended_movie_names[8])
        st.image(recommended_movie_posters[8])
    with col10:
        st.text(recommended_movie_names[9])
        st.image(recommended_movie_posters[9])

st.write("[Download From here>](https://vegamovies.buzz/)")
# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    
    contact_form = """
    <form action="https://formsubmit.co/777905928e24cdc5bc894c8a18977a3f" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()