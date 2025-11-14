from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db = SQLAlchemy()

def create_app(config_name='development'):
    """Application factory pattern"""
    app = Flask(__name__)
    
    # Configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///task_manager.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JSON_SORT_KEYS'] = False
    
    # Initialize extensions
    db.init_app(app)
    CORS(app)  # Enable CORS for React frontend
    
    # Register blueprints
    from app.routes.index_routes import index_bp
    from app.routes.task_routes import task_bp
    from app.routes.comment_routes import comment_bp
    
    app.register_blueprint(index_bp)
    app.register_blueprint(task_bp, url_prefix='/api')
    app.register_blueprint(comment_bp, url_prefix='/api')
    
    # Create tables
    with app.app_context():
        db.create_all()
    
    return app

