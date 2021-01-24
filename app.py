# pip install flask
# pip install wikipedia

from flask import  Flask ,render_template , request
import  wikipedia

app = Flask(__name__)


@app.route('/',methods=["POST","GET"])
def home():
    if request.method == "GET":
        return render_template("index.html")
    else:
        search = request.form['search']

        result = wikipedia.summary(search,sentences=10)
        context ={
            'search':search,
            'result':result
        }
        return render_template('search.html',context=context)


app.run(debug=True)