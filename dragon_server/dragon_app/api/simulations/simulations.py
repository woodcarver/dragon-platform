import os
import json

from flask import request, send_from_directory
from flask_restplus import Resource
from dragon_app import settings
from dragon_app.api.restplus import api
from dragon_app.database.models import session, Simulation, SimulationDownLog, SimulationPreview, SimulationFiles, create_down_log
from dragon_app.api.simulations.serializers import format_sql_result,format_response, format_model_result
from dragon_app.api.simulations.serializers import simulation_list,simulation_detail, file_list, preview_list
from dragon_app.api.simulations.serializers import simulation_down_log


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
        basic_info = Simulation.query.filter(Simulation.id == id).one()
        basic_info = format_model_result(simulation_detail, basic_info)
        # files_info = session.execute("select * from simulation_files")
        # basic_info['files'] = format_sql_result(files_info)
        files_info = SimulationFiles.query.filter(SimulationFiles.simulation_id == id).all()
        basic_info['files'] = format_model_result(file_list, files_info)
        return format_response(simulation_detail, basic_info)

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
        dirpath = os.path.join(settings.HDFILE_PATH, 'simulation_%s' % data['simulation_id'])
        print(dirpath)
        return send_from_directory(dirpath, data['file_name'], as_attachment=True)  # as_attachment=True 一定要写，不然会变成打开，而不是下载   

@ns.route('/downloader/<int:simulation_id>/<path:filename>')
class SimulationDownloader(Resource):
    def get(self, simulation_id, filename):
        dirpath = os.path.join(settings.HDFILE_PATH, 'simulation_%s' % simulation_id)
        print("###" + os.path.abspath(dirpath))
        return send_from_directory(dirpath, filename, as_attachment=True)  # as_attachment=True 一定要写，不然会变成打开，而不是下载   

@ns.route('/test')
class Test(Resource):
    def get(self):
        data = session.execute("select file_name,simulation_id,create_date from simulation_files")
        return format_sql_result(data)