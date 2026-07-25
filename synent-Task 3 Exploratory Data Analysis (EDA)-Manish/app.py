from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        task = request.form["task"]

        conn = sqlite3.connect("database.db")

        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO tasks(task) VALUES(?)",
            (task,)
        )

        conn.commit()
        conn.close()

    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)