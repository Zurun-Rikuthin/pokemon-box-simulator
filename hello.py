from flask import Flask, url_for
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello World!</p>"

@app.route("/user/<username>")
def show_user_profile(username):
    return f"User {escape(username)}"

@app.route("/post/<int:post_id>")
def show_post(post_id):
    return f"Post {post_id}"

@app.route("/path/<path:subpath>")
def show_subpath(subpath):
    return f"Subpath {escape(subpath)}"

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

with app.test_request_context():
    print(url_for("hello_world"))
    print(url_for("show_user_profile", username="John Doe"))
    print(url_for("show_post", post_id="13"))
