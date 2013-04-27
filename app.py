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
            try:
                data = csv_read(file.read())
                print unicode(data)
                return render_template("graph.html", data=unicode(data))
            except:
                return "Invalid PGE GreenButton file"
    return render_template("index.html")

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
