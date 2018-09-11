import logging
import json

from flask import request
from flask_restplus import Resource
from dragon_app.api.restplus import api
from dragon_app.database.models import Simulation
from dragon_app.api.simulations.serializers import format_response, simulation

log = logging.getLogger(__name__)

ns = api.namespace('simulations', description='Operations related to simulation')

@ns.route('/list/latest')
class SimulationCollection(Resource):
    #@api.marshal_list_with(simulation)
    def get(self):
        """
        Returns latest list of simulations.
        """
        datalist = Simulation.query.all()
        return format_response(simulation, datalist)


@ns.route('/detail/<int:id>')
class SimulationCollection(Resource):
    def get(self, id):
        """
        Returns detail of one simulation.
        """
        data = Simulation.query.filter(Simulation.id == id).one()
        return format_response(simulation, data)
