import pytest
import json
from app import db
from app.models import Task, Comment


class TestCommentRoutes:
    """Test suite for Comments CRUD APIs"""
    
    def test_get_comments_for_task_success(self, client, sample_task):
        """Test getting all comments for a task"""
        # Create a comment
        comment_data = {'content': 'First comment'}
        response = client.post(
            f'/api/tasks/{sample_task.id}/comments',
            data=json.dumps(comment_data),
            content_type='application/json'
        )
        
        # Get comments
        response = client.get(f'/api/tasks/{sample_task.id}/comments')
        assert response.status_code == 200
        
        data = json.loads(response.data)
        assert data['success'] is True
        assert len(data['data']) == 1
        assert data['data'][0]['content'] == 'First comment'
        assert data['data'][0]['task_id'] == sample_task.id
    
    def test_get_comments_for_nonexistent_task(self, client):
        """Test getting comments for a task that doesn't exist"""
        response = client.get('/api/tasks/999/comments')
        assert response.status_code == 404
        
        data = json.loads(response.data)
        assert data['success'] is False
        assert 'not found' in data['error'].lower()
    
    def test_get_comments_empty_list(self, client, sample_task):
        """Test getting comments when task has no comments"""
        response = client.get(f'/api/tasks/{sample_task.id}/comments')
        assert response.status_code == 200
        
        data = json.loads(response.data)
        assert data['success'] is True
        assert len(data['data']) == 0
    
    def test_create_comment_success(self, client, sample_task):
        """Test creating a comment successfully"""
        comment_data = {'content': 'This is a test comment'}
        
        response = client.post(
            f'/api/tasks/{sample_task.id}/comments',
            data=json.dumps(comment_data),
            content_type='application/json'
        )
        
        assert response.status_code == 201
        data = json.loads(response.data)
        assert data['success'] is True
        assert data['data']['content'] == 'This is a test comment'
        assert data['data']['task_id'] == sample_task.id
        assert 'id' in data['data']
        assert 'created_at' in data['data']
    
    def test_create_comment_missing_content(self, client, sample_task):
        """Test creating a comment without content"""
        comment_data = {}
        
        response = client.post(
            f'/api/tasks/{sample_task.id}/comments',
            data=json.dumps(comment_data),
            content_type='application/json'
        )
        
        assert response.status_code == 400
        data = json.loads(response.data)
        assert data['success'] is False
        assert 'required' in data['error'].lower()
    
    def test_create_comment_empty_content(self, client, sample_task):
        """Test creating a comment with empty content"""
        comment_data = {'content': '   '}
        
        response = client.post(
            f'/api/tasks/{sample_task.id}/comments',
            data=json.dumps(comment_data),
            content_type='application/json'
        )
        
        assert response.status_code == 400
        data = json.loads(response.data)
        assert data['success'] is False
        assert 'empty' in data['error'].lower()
    
    def test_create_comment_for_nonexistent_task(self, client):
        """Test creating a comment for a task that doesn't exist"""
        comment_data = {'content': 'Test comment'}
        
        response = client.post(
            '/api/tasks/999/comments',
            data=json.dumps(comment_data),
            content_type='application/json'
        )
        
        assert response.status_code == 404
        data = json.loads(response.data)
        assert data['success'] is False
    
    def test_update_comment_success(self, client, sample_comment):
        """Test updating a comment successfully"""
        update_data = {'content': 'Updated comment content'}
        
        response = client.put(
            f'/api/comments/{sample_comment.id}',
            data=json.dumps(update_data),
            content_type='application/json'
        )
        
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['success'] is True
        assert data['data']['content'] == 'Updated comment content'
        assert data['data']['id'] == sample_comment.id
        assert 'updated_at' in data['data']
    
    def test_update_comment_empty_content(self, client, sample_comment):
        """Test updating a comment with empty content"""
        update_data = {'content': '   '}
        
        response = client.put(
            f'/api/comments/{sample_comment.id}',
            data=json.dumps(update_data),
            content_type='application/json'
        )
        
        assert response.status_code == 400
        data = json.loads(response.data)
        assert data['success'] is False
        assert 'empty' in data['error'].lower()
    
    def test_update_comment_no_data(self, client, sample_comment):
        """Test updating a comment without providing data"""
        response = client.put(
            f'/api/comments/{sample_comment.id}',
            data=json.dumps({}),
            content_type='application/json'
        )
        
        assert response.status_code == 400
        data = json.loads(response.data)
        assert data['success'] is False
    
    def test_update_nonexistent_comment(self, client):
        """Test updating a comment that doesn't exist"""
        update_data = {'content': 'Updated content'}
        
        response = client.put(
            '/api/comments/999',
            data=json.dumps(update_data),
            content_type='application/json'
        )
        
        assert response.status_code == 404
        data = json.loads(response.data)
        assert data['success'] is False
        assert 'not found' in data['error'].lower()
    
    def test_delete_comment_success(self, client, sample_comment):
        """Test deleting a comment successfully"""
        response = client.delete(f'/api/comments/{sample_comment.id}')
        
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['success'] is True
        assert 'deleted' in data['message'].lower()
        
        # Verify comment is actually deleted
        response = client.get(f'/api/tasks/{sample_comment.task_id}/comments')
        comments = json.loads(response.data)['data']
        assert len(comments) == 0
    
    def test_delete_nonexistent_comment(self, client):
        """Test deleting a comment that doesn't exist"""
        response = client.delete('/api/comments/999')
        
        assert response.status_code == 404
        data = json.loads(response.data)
        assert data['success'] is False
        assert 'not found' in data['error'].lower()
    
    def test_multiple_comments_for_task(self, client, sample_task):
        """Test creating and retrieving multiple comments for a task"""
        # Create multiple comments
        comments = ['First comment', 'Second comment', 'Third comment']
        for content in comments:
            client.post(
                f'/api/tasks/{sample_task.id}/comments',
                data=json.dumps({'content': content}),
                content_type='application/json'
            )
        
        # Get all comments
        response = client.get(f'/api/tasks/{sample_task.id}/comments')
        assert response.status_code == 200
        
        data = json.loads(response.data)
        assert data['success'] is True
        assert len(data['data']) == 3
        
        # Comments should be ordered by created_at desc
        contents = [c['content'] for c in data['data']]
        assert 'Third comment' in contents
        assert 'Second comment' in contents
        assert 'First comment' in contents
    
    def test_comment_cascade_delete(self, client, sample_task):
        """Test that comments are deleted when task is deleted"""
        # Create a comment
        comment_data = {'content': 'Comment to be deleted'}
        response = client.post(
            f'/api/tasks/{sample_task.id}/comments',
            data=json.dumps(comment_data),
            content_type='application/json'
        )
        comment_id = json.loads(response.data)['data']['id']
        
        # Verify comment exists
        response = client.get(f'/api/tasks/{sample_task.id}/comments')
        assert len(json.loads(response.data)['data']) == 1
        
        # Delete the task
        client.delete(f'/api/tasks/{sample_task.id}')
        
        # Verify comment is also deleted by checking task comments (should 404)
        response = client.get(f'/api/tasks/{sample_task.id}/comments')
        assert response.status_code == 404

