import logging
import json

from flask import request
from flask_restplus import Resource
from dragon_app.api.restplus import api
from dragon_app.database.models import Simulation, SimulationDownLog, SimulationPreview, create_down_log
from dragon_app.api.simulations.serializers import format_response, simulation_list, preview_list, simulation_down_log

log = logging.getLogger(__name__)

ns = api.namespace('simulations', description='Operations related to simulation')

@ns.route('/list/latest')
class SimulationLatest(Resource):
    #@api.marshal_list_with(simulation)
    def get(self):
        """
        Returns latest list of simulations.
        """
        datalist = Simulation.query.all()
        return format_response(simulation_list, datalist)

@ns.route('/list/popular')
class SimulationPopular(Resource):
    def get(self):
        """
        Returns popular list of simulations.
        """
        datalist = Simulation.query.all()
        return format_response(simulation_list, datalist)

@ns.route('/list/all')
class SimulationCollection(Resource):
    def get(self):
        """
        Returns list of simulations.
        """
        datalist = Simulation.query.all()
        return format_response(simulation_list, datalist)

@ns.route('/detail/<int:id>')
class SimulationCollection(Resource):
    def get(self, id):
        """
        Returns detail of one simulation.
        """
        data = Simulation.query.filter(Simulation.id == id).one()
        return format_response(simulation_list, data)

@ns.route('/preview/<int:simulation_id>/<int:time_range>/<int:stellar_type>/<int:popular_type>')
class Preview(Resource):
    def get(self, simulation_id, time_range=None, stellar_type=None, popular_type=None):
        """
        Return preview data
        """
        data = SimulationPreview.query.filter(Simulation.id == simulation_id).one()
        return format_response(preview_list, data)

@ns.route('/download')
class SimulationDownload(Resource):
    @api.response(201, 'download log successfully created.')
    @api.expect(simulation_down_log)
    def post(self):
        """
        Creates a new blog category.
        """
        data = request.json
        create_down_log(data)
        return format_response(), 201

