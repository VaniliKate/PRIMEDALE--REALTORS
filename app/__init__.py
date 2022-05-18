from flask import Flask
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager

bootstrap = Bootstrap()
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


def create_app(config_name):
    app = Flask(__name__)
    # app = Flask(__name__, template_folder='Templates',
    #         static_folder='static', static_url_path="/static")
    app.config.from_object(config_options[config_name])

    # Initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    migrate = Migrate(app,db)
    # login_manager.init_app(app)
    # # mail.init_app(app)
   
    # configure UploadSet
    # configure_uploads(app,photos)


   # Registering the blueprint
    
    
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')
    
    db.init_app(app)
    bootstrap.init_app(app)
    login_manager.init_app(app)
    return app