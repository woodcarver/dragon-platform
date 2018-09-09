import logging

from flask import request
from flask_restplus import Resource
from dragon_app.api.restplus import api

log = logging.getLogger(__name__)

ns = api.namespace('simulations', description='Operations related to simulation')

@ns.route('/list/latest')
class SimulationCollection(Resource):
    #@api.marshal_list_with()
    def get(self):
        """
        Returns latest list of simulations.
        """
        simulations = [1,2,3]
        return simulations
