from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import csv

class BookForm(FlaskForm):
    name = StringField('Book Name', validators=[DataRequired()])
    author = StringField('Author Name', validators=[DataRequired()])
    rating = StringField('Rating', validators=[DataRequired()])
    submit = SubmitField("Submit")

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_key'  # Secret key required for Flask-WTF

Bootstrap5(app)

@app.route('/')
def home():
    books = []
    try:
        with open("book.csv", mode="r", encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                books.append(row)
    except FileNotFoundError:
        pass
    return render_template("index.html", books=books)


@app.route("/add", methods=["GET", "POST"])
def add():
    form = BookForm()
    if form.validate_on_submit():
        with open("book.csv", mode="a", encoding='utf-8', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([form.name.data, form.author.data, form.rating.data])  # Write a new row
        return redirect(url_for("home"))
    return render_template("add.html", form=form)


@app.route("/delete/<int:book_id>")
def delete(book_id):
    books = []
    try:
        with open("book.csv", mode="r", encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file)
            books = list(reader)  # Read all books into a list
    except FileNotFoundError:
        pass

    # Remove the selected book based on its index
    if 0 <= book_id < len(books):
        books.pop(book_id)

    # Write the updated list back to the CSV file without adding extra newlines
    with open("books/book.csv", mode="w", encoding='utf-8', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(books)  # Write the remaining books back to the file

    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
