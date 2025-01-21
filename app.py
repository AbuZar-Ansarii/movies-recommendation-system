import streamlit as st
import pandas as pd
import pickle

st.title("MOVIES RECOMMENDER SYSTEM")

new_df = pickle.load(open('movies_new_df.pkl','rb'))
lst_name = pickle.load(open('lst_movies.pkl','rb'))
matching = pickle.load(open('match_movies.pkl','rb'))

movie_name = st.selectbox("Select Food",lst_name)


def movies_matcher(mov):
    index_of_recipe = new_df[new_df["title"] == mov].index[0]
    close_distance = matching[index_of_recipe]
    lst_of_movies = sorted(list(enumerate(close_distance)), reverse=True, key=lambda x: x[1])[0:15]

    return [new_df.title.iloc[i[0]] for i in lst_of_movies]


# action after button clicked

if st.button('Recommended'):
    st.header("RECOMMENDATION FOR")
    recommendations = movies_matcher(movie_name)
    for films in recommendations:
        st.subheader(films)
    st.dataframe(new_df)