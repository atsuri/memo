from crypt import methods
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
memos = []

@app.route('/')
def root_page():
    return render_template('index.html', memos=memos)

@app.route('/add', methods=["POST"])
def post():
    # HTTPリクエストで送られてきたformのデータを読み取って、それをメモに追加して保存する。
    memos.append(request.form["memo"])
    memos.sort()
    return jsonify({'message': 'created!!'}), 201

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080, threaded=True)
