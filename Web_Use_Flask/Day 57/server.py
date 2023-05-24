from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route("/")
def home():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(url=blog_url)
    all_posts = response.json()
    return render_template("index.html", posts=all_posts)


@app.route("/blog/<number>")
def get_blog(number):
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(url=blog_url)
    all_posts = response.json()
    number = int(number)
    post = all_posts[number-1]
    return render_template("post.html", title=post["title"], subtitle=post["subtitle"], body=post["body"])


if __name__ == "__main__":
    app.run(debug=True)


