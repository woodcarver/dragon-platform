from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def reset_datebase():
    db.drop_all()
    db.create_all()
