from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
import smtplib

app = Flask(__name__)
app.config["SECRET KEY"] = "DAY83PROJECT"
Bootstrap5(app)


lst_cert = [
    ("Microeconomics: A Comprehensive Economics Course", 
     "Successfully completed the course Microeconomics: A Comprehensive Economics Course on 08/02/2024 as taught by Brad Cartwright on Udemy. ", 
     "August 2024", 
     "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTWd5cuxGNDOavsjMG1aoNXfJFZFVPGNEaibA&s",
     "https://www.udemy.com/certificate/UC-d0a40a97-61f8-440e-b866-e92234a1cbcd/"),
    ("Codenection Competitive Programming 2023 (Final Round)", 
     "A Competitive Programming Event by Codenection", 
     "December 2024", 
     "https://www.itscodenection.com/static/media/1050x1050%20CodeNection_Vertical_Logo_Ori%2031.7c9091fc.png",
     "https://drive.google.com/file/d/1X37-X9G6ob-dtv_gwC5SLS0PLjbuJY4y/view?usp=sharing"),
    ("Design Databases With PostgreSQL Skill Path", 
     "Design Databases With PostgreSQL by Codecademy", 
     "December 2024", 
     "https://cdn.iconscout.com/icon/free/png-256/free-codecademy-282922.png",
     "https://drive.google.com/file/d/1JPx8SPuVc2mSNnuxomy7gNkEaKJHT6Fc/view?usp=sharing")
]

@app.route('/')
def home():
    return render_template("index.html", ln_cert = lst_cert)

@app.route("/submit", methods=["POST"])
def submit():
    subject = request.form.get("subject")
    name = request.form.get("name")
    email = request.form.get("email")
    content = request.form.get("content")

    my_email = "lau010416@gmail.com"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password="gwlt aety hglo qply")
        connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=f"Subject: {subject}\n\n Message from {name}({email})\n{content}")
    return redirect(url_for("home"))






if __name__ == "__main__":
    app.run(debug=True, port=5003)
