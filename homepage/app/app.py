from flask import Flask, render_template, jsonify
from k8s import get_cluster_info

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/cluster")
def cluster():
    return jsonify(get_cluster_info())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
