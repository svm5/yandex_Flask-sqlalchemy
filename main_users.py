from flask import Flask
from data import db_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

# Добавляем капитана
def main():
    db_session.global_init("db/mars_users.db")
    session = db_session.create_session()

    user = User()
    user.email = "a@a"
    user.password = "1"
    user.remember_me  = True
    session.add(user)

    user = User()
    user.email = "b@b"
    user.password = "2"
    user.remember_me  = True
    session.add(user)

    user = User()
    user.email = "c@c"
    user.password = "3"
    user.remember_me  = True
    session.add(user)
   
    session.commit()


if __name__ == '__main__':
    main()
