import hashlib
from string import ascii_letters, digits
import os
from flask import Flask, render_template, request
from flask_wtf import CSRFProtect

from register_form import Registration 
from models import db, User

app =  Flask(__name__)
app.config["SECRET_KEY"] = b"cb1d24e1054dfdb9a1ccabba369c3f3008964512dcb39325bdfc2849227fd153"
csrf = CSRFProtect(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///usersdatabase.db"
db.init_app(app)

alphabet_list = ascii_letters + digits
def caesar_code(text, shift):
    shift_text = ''

    for c in text:
        if c not in alphabet_list:
            shift_text += c
            continue

        i = (alphabet_list.index(c) + shift) % len(alphabet_list)
        shift_text += alphabet_list[i]

    return shift_text

@app.route("/")
def index():
    return "перейдите в /registration/"

def init_db():
    db.create_all()


@app.route("/registration/", methods=["GET", "POST"])
def registration():
    form = Registration()
    if request.method == "POST" and form.validate():
        #обработка данных из формы
        name = str(form.name.data)
        second_name = str(form.second_name.data)
        email = str(form.email.data)
        password = form.password.data
        password = str(caesar_code(str(password), shift=5))
        #print(name, second_name, email, password)
        user = User(user_name = name, user_second_name = second_name, user_email = email, 
                    user_password = password)
        db.session.add(user)
        db.session.commit()
    return render_template("registration.html", form = form)


if __name__ == "__main__":
    app.run(debug=True)
