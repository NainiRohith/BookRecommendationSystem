import streamlit as st
import pickle
import pandas as pd
import  numpy as np
popular_df=pickle.load(open('popular_df.pkl','rb'))
ptable=pickle.load(open('ptable.pkl','rb'))
books=pickle.load(open('books.pkl','rb'))
sim_scores=pickle.load(open('sim_scores.pkl','rb'))
new_books= pickle.load(open('pdf.pkl','rb'))

book_name = list(popular_df['Book-Title'].values),
author = list(popular_df['Book-Author'].values),
image = list(popular_df['Image-URL-M'].values),
votes = list(popular_df['num_ratings'].values),
rating = list(popular_df['avg_rating'].values)

st.title("Top 10 Books")

col1, col2, col3 ,col4,col5= st.columns(5)

col1, col2, col3, col4,col5 = st.columns(5)

with col1:
    st.image(image[0][0])
    st.subheader(book_name[0][0])

    st.image(image[0][5])
    st.subheader(book_name[0][5])



with col2:
    st.image(image[0][1])
    st.subheader(book_name[0][1])

    st.image(image[0][6])
    st.subheader(book_name[0][6])

with col3:
    st.image(image[0][2])
    st.subheader(book_name[0][2])

    st.image(image[0][7])
    st.subheader(book_name[0][7])

with col4:
    st.image(image[0][3])
    st.subheader(book_name[0][3])

    st.image(image[0][8])
    st.subheader(book_name[0][8])
with col5:
    st.image(image[0][4])
    st.subheader(book_name[0][4])

    st.image(image[0][9])
    st.subheader(book_name[0][9])






