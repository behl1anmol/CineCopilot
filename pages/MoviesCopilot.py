import pickle
import streamlit as st
import requests
import pandas as pd

st. set_page_config(layout="wide")
def movieRecommender() -> None:
    data = pd.read_csv("./data/TmdbMovies.csv")
    modelPath = "./models/recommenderModel.pkl"

    # set page setting
    st.title('Movies Copilot 🎬')

    # set history var
    if 'history' not in st.session_state:
        st.session_state.history = []

    # import similarity (to be cached)
    def importSim(filename):
        sim = pickle.load(open(filename, 'rb'))
        return sim

    # recommender function
    def recommend_image(movie, sim):
        poster = []
        plot = []
        # index from dataframe
        index = data[data['title'] == movie].index[0]
        dist = dict(enumerate(sim[index]))
        dist = dict(sorted(dist.items(), reverse=True, key=lambda item: item[1]))
        # index from 1 because the first is the movie itself
        cnt = 0
        for key in dist:
            cnt = cnt + 1
            if cnt < 15:
                title = data.iloc[key].title
                try:
                    posterRes, plotRes = get_poster_plot(title)
                    poster.append(posterRes)
                    plot.append(plotRes)
                except:
                    pass
            else:
                break

        return poster[1:], plot[1:]

    # get poster
    def get_poster_plot(title):
        r = requests.get("http://www.omdbapi.com/?i=tt3896198&apikey=37765f04&t=" + title).json()
        posterElement = r["Poster"]
        plotElement = r["Plot"]
        return posterElement, plotElement

    # update last viewed list
    def update_las_viewed():
        if len(st.session_state.history) > 3:
            st.session_state.history.pop()

    similarity = importSim(modelPath)

    # sidebar
    st.sidebar.write("""
    This is a content based recommender system. Pick a movie from the list or search for it and then wait for the recommendations.
    You will get six movies, posters and plots.
    """)

    # select box
    title = st.selectbox("Pick a movie from the list and enjoy some new stuffs!", data["title"])
    if title not in st.session_state.history:
        st.session_state.history.insert(0, title)
    update_las_viewed()

    # recommend
    with st.spinner("Getting the best movies..."):
        recs, plots = recommend_image(title, similarity)

    # recommendation cols
    st.write("## What to watch next....")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image(recs[0])
        st.write(plots[0])
    with col2:
        st.image(recs[1])
        st.write(plots[1])
    with col3:
        st.image(recs[2])
        st.write(plots[2])

    col4, col5, col6 = st.columns(3)
    with col4:
        st.image(recs[3])
        st.write(plots[3])
    with col5:
        st.image(recs[4])
        st.write(plots[4])
    with col6:
        st.image(recs[5])
        st.write(plots[5])

    col7, col8, col9 = st.columns(3)
    with col7:
        st.image(recs[6])
        st.write(plots[6])
    with col8:
        st.image(recs[7])
        st.write(plots[7])
    with col9:
        st.image(recs[8])
        st.write(plots[8])

    # last viewed
    st.write("## Last viewed:")
    r1, r2, r3 = st.columns(3)
    with r1:
        try:
            st.image(get_poster_plot(st.session_state.history[0])[0])
        except IndexError:
            pass

    with r2:
        try:
            st.image(get_poster_plot(st.session_state.history[1])[0])
        except IndexError:
            pass

    with r3:
        try:
            st.image(get_poster_plot(st.session_state.history[2])[0])
        except IndexError:
            pass


movieRecommender()
