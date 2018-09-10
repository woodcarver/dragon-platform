# Flask_settings
FLASK_SERVER_NAME = 'localhost:7777'
FLASK_DEBUG = True  # Do not use debug mode in production

# Flask-Restplus settings
RESTPLUS_SWAGGER_UI_DOC_EXPANSION = 'list'
RESTPLUS_VALIDATE = True
RESTPLUS_MASK_SWAGGER = False                                        
RESTPLUS_ERROR_404_HELP = False

# SQLAlchemy settings
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost:3306/dragon?charset=utf8'
SQLALCHEMY_TRACK_MODIFICATIONS = False
