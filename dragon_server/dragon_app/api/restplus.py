import logging
import traceback

from flask_restplus import Api
from dragon_app import settings
from sqlalchemy.orm.exc import NoResultFound

log = logging.getLogger(__name__)

api = Api(version='1.0', title='Dragon Simulation API',
        description='A data share platform for asytronomy simulation')

@api.errorhandler
def default_error_handler(e):
    message = 'An unhandled exeception occurred.'
    log.exception(message)

    if not settings.FLASK_DEBUG:
        return {'messagae' : message}, 500

@api.errorhandler(NoResultFound)
def database_not_found_error_handler(e):
    log.warning(traceback.format_exc())
    return {'message' : 'A database result was required but none was found.'}, 404
