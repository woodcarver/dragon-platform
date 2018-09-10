from flask_restplus import fields
from dragon_app.api.restplus import api

simulation = api.model("simulation",{
        'id': fields.Integer(readOnly=True, description='The unique identifier of a blog simulation'),
        'title': fields.String(required=True, description='Simulation title'),
        })
