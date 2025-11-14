from flask import Blueprint, jsonify

index_bp = Blueprint('index', __name__)


@index_bp.route('/', methods=['GET'])
def index():
    """Root endpoint providing API information"""
    return jsonify({
        'message': 'Task Manager API',
        'version': '1.0.0',
        'endpoints': {
            'tasks': {
                'GET /api/tasks': 'Get all tasks',
                'POST /api/tasks': 'Create a new task',
                'GET /api/tasks/<id>': 'Get a specific task',
                'PUT /api/tasks/<id>': 'Update a task',
                'DELETE /api/tasks/<id>': 'Delete a task'
            },
            'comments': {
                'GET /api/tasks/<task_id>/comments': 'Get all comments for a task',
                'POST /api/tasks/<task_id>/comments': 'Create a comment for a task',
                'PUT /api/comments/<id>': 'Update a comment',
                'DELETE /api/comments/<id>': 'Delete a comment'
            }
        },
        'status': 'running'
    }), 200

