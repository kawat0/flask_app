from flask import Flask, render_template
import os
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("home.html")

if __name__=="__main__":

    #app.debug = True
    #app.run()
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
