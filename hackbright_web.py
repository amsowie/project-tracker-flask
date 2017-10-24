"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, redirect, render_template

import hackbright

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github')

    first_name, last_name, github = hackbright.get_student_by_github(github)
    
    html = render_template("student_info.html",
                            first=first_name,
                            last=last_name,
                            github=github)

    return html

@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student"""

    return render_template("student_search.html")

@app.route("/add-form")
def display_add_form():
    """ Show add student form"""

    return render_template("add_student.html")


@app.route("/student-add", methods=['POST'])
def student_add():
    """Add a student"""
    first_name = request.form.get('firstname')
    last_name = request.form.get('lastname')
    git_hub = request.form.get('github')

    hackbright.make_new_student(first_name, last_name, git_hub)

    return render_template("student_info.html",
                            first=first_name,
                            last=last_name,
                            github=git_hub)

if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
