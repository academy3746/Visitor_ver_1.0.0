from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

# DB Connection
from pymongo import MongoClient
client = MongoClient('mongodb+srv://admin:1q2w3e4r!@cluster0.n5ejj.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

# Appended Variable
# 1. 닉네임: name
# 2. 응원 댓글: comment

@app.route('/')
def home():
   return render_template('index.html')

# 01 CREATE TABLE
@app.route("/homework", methods=["POST"])
def homework_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']

    # INSERT INTO BOARDS('NAME','COMMENT') VALUES(?,?)
    doc = {
        'name':name_receive,
        'comment':comment_receive
    }
    db.boards.insert_one(doc)

    return jsonify({'msg':'등록 완료!'})

# 02 READ TABLE
@app.route("/homework", methods=["GET"])
def homework_get():
    # SELECT * FROM BOARDS
    board_list = list(db.boards.find({}, {'_id': False}))
    return jsonify({'boards':board_list})

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)