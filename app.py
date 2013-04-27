from flask import Flask, request, render_template

from parser import csv_read
import os
app = Flask(__name__)

ALLOWED_EXTENSIONS = ['csv', 'CSV']


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route("/", methods=['GET', 'POST'])
def process():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            print type(file.read())
            return render_template("graph.html")
    return render_template("index.html")

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
