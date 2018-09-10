import logging

from flask import request
from flask_restplus import Resource
from dragon_app.api.restplus import api
from dragon_app.database.models import Simulation
from dragon_app.api.simulations.serializers import simulation

log = logging.getLogger(__name__)

ns = api.namespace('simulations', description='Operations related to simulation')

@ns.route('/list/latest')
class SimulationCollection(Resource):
    @api.marshal_list_with(simulation)
    def get(self):
        """
        Returns latest list of simulations.
        """
        #simulations = [1,2,3]
        simulations = Simulation.query.all()
        return simulations
