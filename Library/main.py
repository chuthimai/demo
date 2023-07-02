from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books-collection.db'

database = SQLAlchemy()
database.init_app(app)


class Book(database.Model):
    id = database.Column(database.INTEGER, primary_key=True, index=True)
    title = database.Column(database.String(255), unique=True, nullable=False)
    author = database.Column(database.String(255), nullable=False)
    rating = database.Column(database.FLOAT, nullable=False)

    def __repr__(self):
        return f'Book: {self.title}' \
               f'\n author = {self.author}' \
               f'\n rating = {self.rating}'


with app.app_context():
    database.create_all()


@app.route('/')
def home():
    result = database.session.execute(database.select(Book).order_by(Book.title))
    all_books = list(result.scalars())
    return render_template("index.html", books=all_books)


@app.route("/change-rating/<title>", methods=["POST", "GET"])
def change_rating(title):
    book = database.session.execute(database.select(Book).where(Book.title == title)).scalar()
    if request.method == "POST":
        book.rating = request.form["rating"]
        database.session.commit()
        return redirect(url_for('home'))
    return render_template("change-rating.html", book=book)


@app.route("/delete/<id>")
def delete(id):
    with app.app_context():
        book_to_delete = database.get_or_404(Book, id)
        database.session.delete(book_to_delete)
        database.session.commit()
        return redirect(url_for('home'))


@app.route("/add", methods=["POST", "GET"])
def add():
    if request.method == "POST":
        new_book = Book(
            title=request.form["title"],
            author=request.form["author"],
            rating=request.form["rating"]
        )
        database.session.add(new_book)
        database.session.commit()

        return redirect(url_for('home'))
    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)

