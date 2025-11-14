from flask import Blueprint, request, jsonify
from app import db
from app.models import Task

task_bp = Blueprint('tasks', __name__)


@task_bp.route('/tasks', methods=['GET'])
def get_tasks():
    """Get all tasks"""
    try:
        tasks = Task.query.all()
        return jsonify({
            'success': True,
            'data': [task.to_dict() for task in tasks]
        }), 200
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@task_bp.route('/tasks', methods=['POST'])
def create_task():
    """Create a new task"""
    try:
        data = request.get_json()
        
        # Validation
        if not data or 'title' not in data:
            return jsonify({
                'success': False,
                'error': 'Title is required'
            }), 400
        
        title = data.get('title', '').strip()
        if not title:
            return jsonify({
                'success': False,
                'error': 'Title cannot be empty'
            }), 400
        
        # Create task
        task = Task(
            title=title,
            description=data.get('description', '').strip(),
            status=data.get('status', 'pending')
        )
        
        db.session.add(task)
        db.session.commit()
        
        return jsonify({
            'success': True,
            'data': task.to_dict()
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@task_bp.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    """Get a specific task by ID"""
    try:
        task = Task.query.get_or_404(task_id)
        return jsonify({
            'success': True,
            'data': task.to_dict()
        }), 200
    except Exception as e:
        return jsonify({
            'success': False,
            'error': 'Task not found' if '404' in str(e) else str(e)
        }), 404


@task_bp.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    """Update a task"""
    try:
        task = Task.query.get_or_404(task_id)
        data = request.get_json()
        
        if not data:
            return jsonify({
                'success': False,
                'error': 'No data provided'
            }), 400
        
        # Update fields if provided
        if 'title' in data:
            title = data['title'].strip()
            if not title:
                return jsonify({
                    'success': False,
                    'error': 'Title cannot be empty'
                }), 400
            task.title = title
        
        if 'description' in data:
            task.description = data['description'].strip()
        
        if 'status' in data:
            task.status = data['status']
        
        db.session.commit()
        
        return jsonify({
            'success': True,
            'data': task.to_dict()
        }), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'success': False,
            'error': 'Task not found' if '404' in str(e) else str(e)
        }), 404


@task_bp.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    """Delete a task"""
    try:
        task = Task.query.get_or_404(task_id)
        db.session.delete(task)
        db.session.commit()
        
        return jsonify({
            'success': True,
            'message': 'Task deleted successfully'
        }), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'success': False,
            'error': 'Task not found' if '404' in str(e) else str(e)
        }), 404

