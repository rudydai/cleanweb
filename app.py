from flask import Flask, request, render_template

from parser import csv_read
from tips import main as tipper
import os
import json

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
                return render_template("graph.html", data=unicode(data), tip=tipper())
            except:
                return "Invalid PGE GreenButton file"
    return render_template("index.html")

BUFF_SIZE = 120 
buff = []

@app.route("/ravenfeed", methods=["GET","POST"])
def process2():
    global buff
    if request.method == "POST":
        print "posting data"
        time = request.form["time"]
        demand = float(request.form["demand"])
        buff.append({"kWh":demand, "time":time})
        if len(buff) > BUFF_SIZE:
            buff.pop(0)
    print list(buff)
    data = {"readings":list(buff)}
    jsdat = json.dumps(data)
    return render_template("livegraph.html", data=unicode(jsdat), tip=tipper())


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
