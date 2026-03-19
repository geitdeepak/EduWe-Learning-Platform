from flask import Flask, render_template

app = Flask(__name__)

# 🔹 Videos (UPDATED with Python)
videos = [

{
"title": "Azure Virtual Machines Tutorial",
"description": "Learn how to deploy Azure Virtual Machines step by step.",
"category": "Azure",
"video_id": "fzrvx_1-9_o",
"link": "https://www.youtube.com/embed/fzrvx_1-9_o",
"github": "https://github.com/example/azure-vm-demo"
},

{
"title": "AWS EC2 Beginner Guide",
"description": "Understand AWS EC2 instances and cloud infrastructure.",
"category": "AWS",
"video_id": "5xc8M5WMM6s",
"link": "https://www.youtube.com/embed/5xc8M5WMM6s",
"github": "https://github.com/example/aws-ec2-demo"
},

{
"title": "AI & Machine Learning Basics",
"description": "Introduction to AI & ML.",
"category": "AI/ML",
"video_id": "JMUxmLyrhSk",
"link": "https://www.youtube.com/embed/JMUxmLyrhSk",
"github": "https://github.com/example/ml-basics"
},

{
"title": "IoT Fundamentals",
"description": "Learn IoT architecture.",
"category": "IoT",
"video_id": "LlhmzVL5bm8",
"link": "https://www.youtube.com/embed/LlhmzVL5bm8",
"github": "https://github.com/example/iot-fundamentals"
},

{
"title": "Python Basics",
"description": "Learn Python from scratch.",
"category": "Python",
"video_id": "rfscVS0vtbw",
"link": "https://www.youtube.com/embed/rfscVS0vtbw",
"github": "https://github.com/example/python-basics"
}

]


# 🔥 Learning Paths (GROUPED)
learning_paths = {
"Azure": ["fzrvx_1-9_o"],
"AWS": ["5xc8M5WMM6s"],
"AI/ML": ["JMUxmLyrhSk"],
"IoT": ["LlhmzVL5bm8"],
"Python": ["rfscVS0vtbw"]   # ✅ NEW
}


# 🔹 HOME
@app.route("/")
def home():
    return render_template("index.html", videos=videos)


# 🔥 NEW PAGE: Learning Paths
@app.route("/learning-paths")
def learning_paths_page():
    return render_template(
        "learning_paths.html",
        videos=videos,
        paths=learning_paths
    )


@app.route("/my-learning")
def my_learning():
    return render_template("saved.html")

@app.route("/about-us")
def about_us():
    return render_template("about-us.html")

@app.route("/YTChannel")
def yt_channel():
    return render_template("YTChannel.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)