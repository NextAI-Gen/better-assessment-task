from flask import Blueprint, request, jsonify
from app import db
from app.models import Comment, Task

comment_bp = Blueprint('comments', __name__)


@comment_bp.route('/tasks/<int:task_id>/comments', methods=['GET'])
def get_comments(task_id):
    """Get all comments for a specific task"""
    try:
        # Verify task exists
        task = Task.query.get_or_404(task_id)
        
        comments = Comment.query.filter_by(task_id=task_id).order_by(Comment.created_at.desc()).all()
        
        return jsonify({
            'success': True,
            'data': [comment.to_dict() for comment in comments]
        }), 200
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': 'Task not found' if '404' in str(e) else str(e)
        }), 404


@comment_bp.route('/tasks/<int:task_id>/comments', methods=['POST'])
def create_comment(task_id):
    """Create a new comment for a task"""
    try:
        # Verify task exists
        task = Task.query.get_or_404(task_id)
        
        data = request.get_json()
        
        # Validation
        if not data or 'content' not in data:
            return jsonify({
                'success': False,
                'error': 'Content is required'
            }), 400
        
        content = data.get('content', '').strip()
        if not content:
            return jsonify({
                'success': False,
                'error': 'Content cannot be empty'
            }), 400
        
        # Create comment
        comment = Comment(
            task_id=task_id,
            content=content
        )
        
        db.session.add(comment)
        db.session.commit()
        
        return jsonify({
            'success': True,
            'data': comment.to_dict()
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'success': False,
            'error': 'Task not found' if '404' in str(e) else str(e)
        }), 404


@comment_bp.route('/comments/<int:comment_id>', methods=['PUT'])
def update_comment(comment_id):
    """Update a comment"""
    try:
        comment = Comment.query.get_or_404(comment_id)
        data = request.get_json()
        
        if not data:
            return jsonify({
                'success': False,
                'error': 'No data provided'
            }), 400
        
        # Validation
        if 'content' in data:
            content = data['content'].strip()
            if not content:
                return jsonify({
                    'success': False,
                    'error': 'Content cannot be empty'
                }), 400
            comment.content = content
        
        db.session.commit()
        
        return jsonify({
            'success': True,
            'data': comment.to_dict()
        }), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'success': False,
            'error': 'Comment not found' if '404' in str(e) else str(e)
        }), 404


@comment_bp.route('/comments/<int:comment_id>', methods=['DELETE'])
def delete_comment(comment_id):
    """Delete a comment"""
    try:
        comment = Comment.query.get_or_404(comment_id)
        db.session.delete(comment)
        db.session.commit()
        
        return jsonify({
            'success': True,
            'message': 'Comment deleted successfully'
        }), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'success': False,
            'error': 'Comment not found' if '404' in str(e) else str(e)
        }), 404

