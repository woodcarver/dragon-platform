from dragon_app.database import db

class Simulation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    publish_date = db.Column(db.DateTime)

    def __init__(self, title, pub_date=None):
        self.title = title
        if pub_date is None:
            pub_date = datetime.utcnow()
        self.publish_date = pub_date
    def __repr__(self):
        return '<Simulation %r>' % self.title
