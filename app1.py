from flask import Flask,render_template,request
import pickle
import numpy as np



popular_df=pickle.load(open('popular_df.pkl','rb'))
ptable=pickle.load(open('ptable.pkl','rb'))
books=pickle.load(open('books.pkl','rb'))
sim_scores=pickle.load(open('sim_scores.pkl','rb'))
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('indexx.html',
                           book_name = list(popular_df['Book-Title'].values),
                           author=list(popular_df['Book-Author'].values),
                           image=list(popular_df['Image-URL-M'].values),
                           votes=list(popular_df['num_ratings'].values),
                           rating=list(popular_df['avg_rating'].values)
                           )
@app.route('/recommend')
def recommend_ui():
    return render_template('recommend.html')

@app.route('/recommend_books',methods=['post','get'])
def recommend():

    user_input = request.form.get('user_input')
    data = []
    book_list =books['Book-Title'].values
    


    if ((ptable.index== user_input).any()):
        index = np.where(ptable.index == user_input)[0][0]

        similar_items = sorted(list(enumerate(sim_scores[index])), key=lambda x: x[1], reverse=True)[1:5]

        for i in similar_items:
            item = []
            temp_df = books[books['Book-Title'] == ptable.index[i[0]]]
            item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
            item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
            item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))

            data.append(item)

        print(data)

        return render_template('recommend.html', data=data)

    else:
        data.append(" ")

        return render_template('recommend.html',data=data)




if __name__=='__main__':
    app.run(debug=True)