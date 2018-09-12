from dragon_app.database import db
from datetime import datetime

class Simulation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    profile = db.Column(db.String(80))
    rh = db.Column(db.String(255))
    imf = db.Column(db.String(255))
    q = db.Column(db.String(255))
    kick_ns = db.Column(db.String(255))
    rt = db.Column(db.String(255))
    simulation_time = db.Column(db.Integer)
    publish_date = db.Column(db.DateTime)

    #   def __init__(self, title, pub_date=None):
    #        self.title = title
    #        if pub_date is None:
    #            pub_date = datetime.utcnow()
    #        self.publish_date = pub_date
    #    def __repr__(self):
    #        return '<Simulation %r>' % self.title

class SimulationDownLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    simulation_id = db.Column(db.Integer)
    email= db.Column(db.String(80))
    create_date = db.Column(db.DateTime)

    def __init__(self, simulation_id, email, create_date=None):
         self.simulation_id = simulation_id
         self.email = email 
         if create_date is None:
             create_date = datetime.utcnow()
         self.create_date = create_date

def create_down_log(data):
    simulation_id = data.get('simulation_id')
    email = data.get('email')
    post = SimulationDownLog(simulation_id, email)
    db.session.add(post)
    db.session.commit()
