import flask_login

from flask import Flask, redirect, render_template
from flask_login import LoginManager
from flask_login import login_user

from data import db_session
from data.users import User
from data.login_form import LoginForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)


@app.route('/')
@app.route('/index')
def index():
    return "Привет, Яндекс!"


@login_manager.user_loader
def load_user(user_id):
    session = db_session.create_session()
    return session.query(User).get(user_id)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    db_session.global_init("db/mars_users.db")
    session = db_session.create_session()
    # print(flask_login.current_user)
    if form.validate_on_submit():
        
        user = session.query(User).filter(User.email == form.email.data).first()
        # print(session.query(User).all())
        if user.check_password(form.password.data) is True:
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template("login.html", message="Incorrect password", form=form)
    return render_template("login.html", title="Авторизация", form=form)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')