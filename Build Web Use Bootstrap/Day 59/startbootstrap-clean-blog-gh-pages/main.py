from flask import Flask, render_template, request
import requests
import smtplib
import os


def sent_email(email:str, password:str, user_email:str, name: str, msg:str):
    connection = smtplib.SMTP(host="smtp.gmail.com")
    connection.starttls()
    connection.login(user=email, password=password)
    connection.sendmail(
        from_addr=email,
        to_addrs=user_email,
        msg=f"Subject: Successfully sent your message\n\n"
            f"Hi {name},"
            f"\nYou just send for us a message with content is:"
            f"\n{msg}".encode("utf-8")
    )
    connection.close()


blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
app = Flask(__name__)
data = requests.get(blog_url).json()


@app.route("/")
def get_all_posts():
    return render_template("index.html", data=data)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/post/<number>")
def get_post(number):
    data_post = data[int(number)-1]
    title = data_post['title']
    subtitle = data_post['subtitle']
    body = data_post['body']
    return render_template("post.html", title=title, subtitle=subtitle, body=body)


@app.route("/form-entry", methods=["POST"])
def receive_data():
    user_data = request.form
    name = user_data["name"]
    email = user_data["email"]
    phone = user_data["phone"]
    msg = user_data["message"]
    sent_email(
        email=os.environ.get("EMAIL"),
        password=os.environ.get("PASS"),
        user_email=email,
        name=name,
        msg=msg
    )
    return render_template("successfully.html")


if __name__ == "__main__":
    app.run(debug=True)




