from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap4
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
import os


MOVIE_DB_API_KEY = os.environ.get("AUTH")
MOVIE_DB_SEARCH_URL = "https://api.themoviedb.org/3/search/movie"
MOVIE_DB_INFO_URL = "https://api.themoviedb.org/3/movie"
MOVIE_DB_IMAGE_URL = "https://image.tmdb.org/t/p/w500"

AUTH = os.environ.get("AUTH")
url = "https://api.themoviedb.org/3/search/movie?query=Sing&include_adult=true&language=en-US&page=1"
headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {AUTH}"
}


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap4(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movies-collection.db"
db = SQLAlchemy()
db.init_app(app)


class Movie(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    title = db.Column(db.String(255), unique=True, nullable=False)
    year = db.Column(db.String(4), nullable=False)
    description = db.Column(db.String, nullable=False)
    rating = db.Column(db.String, nullable=False)
    ranking = db.Column(db.String, nullable=False)
    review = db.Column(db.String, nullable=False)
    img_url = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"Movie: {self.title} Ranking: {self.ranking}"


with app.app_context():
    db.create_all()


class Form(FlaskForm):
    new_rating = StringField(
        label="Your rating out of 10 e.g. 7.5",
        validators=[DataRequired()]
    )
    review = StringField(
        label="Your review",
        validators=[DataRequired()]
    )
    submit = SubmitField(label="Done")


class AddForm(FlaskForm):
    new_movie = StringField(
        label="Movie Title",
        validators=[DataRequired()]
    )
    submit = SubmitField(label="Add Movie")


@app.route("/")
def home():
    with app.app_context():
        result = db.session.execute(db.select(Movie).order_by(Movie.rating))
        all_movies = list(result.scalars())
        all_movies = all_movies[::-1]
        length = len(all_movies)
        for i in range(0, length):
            all_movies[i].ranking = str(i+1)
    return render_template("index.html", all_movies=all_movies)


@app.route("/add", methods=["GET", "POST"])
def add():
    form = AddForm()
    if form.validate_on_submit():
        movie_title = form.new_movie.data
        response = requests.get(MOVIE_DB_SEARCH_URL, headers=headers, params={"query": movie_title})
        data = response.json()["results"]
        return render_template("select.html", options=data)
    return render_template("add.html", form=form)


@app.route("/find")
def find_movie():
    movie_api_id = request.args.get("id")
    if movie_api_id:
        movie_api_url = f"{MOVIE_DB_INFO_URL}/{movie_api_id}"
        response = requests.get(movie_api_url, headers=headers, params={"language": "en-US"})
        data = response.json()
        print(data)
        new_movie = Movie(
            title=data["title"],
            year=data["release_date"].split("-")[0],
            img_url=f"{MOVIE_DB_IMAGE_URL}{data['poster_path']}",
            description=data["overview"],
            rating="None",
            ranking="None",
            review="None"
        )
        db.session.add(new_movie)
        db.session.commit()

        # Redirect to /edit route
        return redirect(url_for("edit", id=new_movie.id))


@app.route("/edit/<id>", methods=["POST", "GET"])
def edit(id):
    movie = db.session.execute(db.select(Movie).where(Movie.id == int(id))).scalar()
    form = Form()
    if request.method == "POST":
        if form.validate_on_submit():
            movie.rating = form.new_rating.data
            movie.review = form.review.data
            db.session.commit()
            return redirect(url_for('home'))
    return render_template("edit.html", form=form, movie=movie)


@app.route("/delete/<id>")
def delete(id):
    movie = db.session.execute(db.select(Movie).where(Movie.id == int(id))).scalar()
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
