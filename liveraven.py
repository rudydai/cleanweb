from flask import Flask, render_template

app = Flask(__name__)
BUFF_SIZE = 120 
buff = []

@app.route("/ravenfeed", method=["GET","POST"])
def process():
    if request.method == "POST":
        time = request.form["time"]
        demand = float(request.form["demand"])
        buff.append({"kWh":demand, "time":time})
        if BUFF_SIZE > 25:
            buff.pop(0)
    data = {"readings":list(buff)}
    return render_template("graph.html", data=unicode(data))
    

