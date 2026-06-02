from flask import Flask
from flask import render_template
from flask import request
from flask import redirect

import mysql.connector

app = Flask(__name__)


def get_connection():
    return mysql.connector.connect(
        host="mysql",
        user="root",
        password="root123",
        database="studentdb"
    )


@app.route("/")
def index():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("select * from students")

    students = cursor.fetchall()

    conn.close()

    return render_template(
        "index.html",
        students=students
    )


@app.route("/add", methods=["GET","POST"])
def add_student():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        course = request.form["course"]

        conn = get_connection()

        cursor = conn.cursor()

        cursor.execute(
            """
            insert into students(name,email,course)
            values(%s,%s,%s)
            """,
            (name,email,course)
        )

        conn.commit()

        conn.close()

        return redirect("/")

    return render_template("add.html")


@app.route("/edit/<id>", methods=["GET","POST"])
def edit_student(id):

    conn = get_connection()

    cursor = conn.cursor()

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        course = request.form["course"]

        cursor.execute(
            """
            update students
            set name=%s,email=%s,course=%s
            where id=%s
            """,
            (name,email,course,id)
        )

        conn.commit()

        conn.close()

        return redirect("/")

    cursor.execute(
        "select * from students where id=%s",
        (id,)
    )

    student = cursor.fetchone()

    conn.close()

    return render_template(
        "edit.html",
        student=student
    )


@app.route("/search")
def search():

    keyword = request.args.get("keyword")

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        select * from students
        where name like %s
        """,
        ("%" + keyword + "%",)
    )

    students = cursor.fetchall()

    conn.close()

    return render_template(
        "index.html",
        students=students
    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000
    )