from flask import Flask, render_template, url_for, redirect
import json
import random
from dotenv import load_dotenv
from forms.form import ContestantForm
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField

app = Flask(__name__, template_folder='templates')
import os
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

@app.route('/distribution')
def distribution():
    with open("dist.json", "r", encoding="utf-8") as f:
        dist_list = json.load(f)
    print(dist_list)
    return render_template('distribution.html', distribution=dist_list)

@app.route("/table/<gender>/<int:age>")
def table(gender, age):
    if gender == "female":
        img_f = url_for("static", filename="img/pink.jpg")
    elif gender == "male":
        img_f = url_for("static", filename="img/dark_blue.jpg")

    if int(age) < 21:
        img_a = url_for("static", filename="img/kid.jpg")
    elif int(age) >= 21:
        img_a = url_for("static", filename="img/adult.jpg")
    return render_template("table.html", gender=gender, age=int(age), path_to_image1=img_f, path_to_image2=img_a )


@app.route("/carousel")
def carousel():
    pat = url_for("static", filename="img/adult.jpg")
    return render_template("carousel.html", pat = pat)

@app.route("/member")
def member():
    with open("members.json", "r") as f:
        members = json.load(f)
    n = random.randrange(0, len(members["members"]), 1)
    rand_member = members["members"][n]
    fullname = rand_member["name"] + " " +rand_member["surname"]
    job = rand_member["job"]
    photo = url_for("static", filename=rand_member["photo"])
    print(photo)
    return render_template("members.html", fname=fullname, path_to_photo=photo, job = job)

@app.route("/contestant_form", methods=["GET", "POST"])
def contestant():
    contestant_form = ContestantForm()
    st = url_for('static', filename='css/style.css')
    if contestant_form.validate_on_submit():
        return redirect("/success")
    return render_template("contestant.html", title="Отбор участников", contestant_form=contestant_form, style = st)

@app.route("/results/<nickname>/<int:level>/<float:rating>")
def result(nickname,level,rating):
    print("FCCG")
    return render_template("result.html", name=nickname, lvl=level, rating=rating)

class LoadImageForm(FlaskForm):
    file = FileField()
    submit = SubmitField('Войти')

@app.route("/gallery", methods=['GET', 'POST'])
def web3():
    form = LoadImageForm()
    if form.validate_on_submit():
        raw_data = form.file.data
        with open(f"./static/img/mars{len(os.listdir('./static/img/')) + 1}.jpg", "wb") as out_file:
            out_file.write(raw_data.read())
        return redirect("gallery")
    return render_template("carousel.html", images=list(map(lambda x: url_for('static', filename=x),
                                                        map(lambda t: "gallery/" + t,
                                                            os.listdir("./static/gallery/")))), form=form)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')