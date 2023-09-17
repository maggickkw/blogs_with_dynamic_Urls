from flask import Flask, render_template
import requests

blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
response = requests.get(blog_url)
all_posts = response.json()

app = Flask(__name__)

@app.route('/')
def get_all_post():
    return render_template("index.html", posts=all_posts)

@app.route('/post/<int:num>')
def show_post(num):
    posts_id = all_posts
    requested_post = None
    for blog_post in posts_id:
        if blog_post['id'] == num:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)



if __name__ == "__main__":
    app.run(debug=True)
