import streamlit as st
import pickle
import pandas as pd
import numpy as np
popular_df=pickle.load(open('popular_df.pkl','rb'))
ptable=pickle.load(open('ptable.pkl','rb'))
books=pickle.load(open('books.pkl','rb'))
sim_scores=pickle.load(open('sim_scores.pkl','rb'))
new_books= pickle.load(open('pdf.pkl','rb'))





def recommend(book):


    data = []




    index = np.where(ptable.index == book)[0][0]

    similar_items = sorted(list(enumerate(sim_scores[index])), key=lambda x: x[1], reverse=True)[1:5]







    for i in similar_items:

        item = []
        temp_df = books[books['Book-Title'] == ptable.index[i[0]]]
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))


        data.append(item)

    return(data)


nbooks_list=list(new_books.index)

st.title("Book recommendor System")
book_selection = st.selectbox(
    'choose a book',
    (nbooks_list))
if st.button('Recommend'):
    recommendation= recommend(book_selection)
    col1, col2, col3,col4= st.columns(4)

    with col1:

        st.image(recommendation[0][1])
        st.header(recommendation[0][0])




    with col2:

        st.image(recommendation[1][1])
        st.header(recommendation[1][0])








    with col3:

        st.image(recommendation[2][1])
        st.header(recommendation[2][0])



    with col4:

        st.image(recommendation[3][1])
        st.header(recommendation[3][0])





