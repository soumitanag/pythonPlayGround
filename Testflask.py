from flask import Flask, render_template, jsonify, request
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]




# @app.route("/home",methods=['GET'])
# def hello():
#     return render_template("myHome.html")

@app.route('/file_upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    file_name = secure_filename(file.filename)
    file.save(file_name)
    return ('file uploaded successfully')


@app.route('/resources/books/all', methods=['GET'])
def api_all():
    return jsonify(books)

@app.route('/resources/books/all/<int:bookId>', methods=['GET'])
def api_allByBookId(bookId):
   result = []
   for book in books:
       if book['id'] == bookId:
           result.append(book)
   if len(result) == 0:
        return ("not found")
   else:
        return jsonify(result)

@app.route('/enter_details', methods=['POST'])
def enter_details():
    data = request.get_json()
    print(data['id'])
    print(data['name'])
    print(data['age'])
    return("details revised")

if __name__ =='__main__':
    app.run(host='0.0.0.0', port = 9080, debug=True )

# if __name__ =='__main__':
#     app.run(debug=True)

# @app.route('/resources/books/all/<int:book_id>', methods=['GET'])
