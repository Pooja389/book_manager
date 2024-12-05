from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import csv
'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

class bookform(FlaskForm):
    name = StringField('book name', validators=[DataRequired()])
    author = StringField('author name',validators=[DataRequired()])
    rating = StringField('rating',validators=[DataRequired()])

    submit = SubmitField("submit")


app = Flask(__name__)
app.config['SECRET_KEY'] = 'pooja_Saini'  # Secret key required for Flask-WTF

all_books = []

Bootstrap5(app)
@app.route('/')
def home():
    books = []
    # Read the CSV file and get all book entries
    try:
        with open("book.csv", mode="r", encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                books.append(row)
    except FileNotFoundError:
        pass 
    return render_template("index.html",books = books)



@app.route("/add",methods=["GET","POST"])
def add():
    form = bookform()
    if form.validate_on_submit():

        with open("book.csv", mode="a", encoding='utf-8') as csv_file:
            csv_file.write(f"\n{form.name.data},"
                    f"{form.author.data},"
                    f"{form.rating.data},")
        return redirect(url_for("home"))    
                       

    return render_template("add.html",form=form)


if __name__ == "__main__":
    app.run(debug=True)

