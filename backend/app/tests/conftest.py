import pytest
from app import create_app, db
from app.models import Task, Comment


@pytest.fixture
def app():
    """Create application for testing"""
    app = create_app('testing')
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['WTF_CSRF_ENABLED'] = False
    
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()


@pytest.fixture
def client(app):
    """Create test client"""
    return app.test_client()


@pytest.fixture
def sample_task(app):
    """Create a sample task for testing"""
    with app.app_context():
        task = Task(title='Test Task', description='Test Description')
        db.session.add(task)
        db.session.commit()
        # Get the ID before the context closes
        task_id = task.id
        # Expunge to detach from session but keep the object
        db.session.expunge(task)
        # Manually set the id attribute to ensure it's accessible
        object.__setattr__(task, 'id', task_id)
        return task


@pytest.fixture
def sample_comment(app, sample_task):
    """Create a sample comment for testing"""
    with app.app_context():
        # Get task_id from the sample_task (it should have id attribute)
        task_id = getattr(sample_task, 'id', None)
        if task_id is None:
            # If id is not accessible, query for the task
            task = db.session.query(Task).first()
            task_id = task.id if task else 1
        
        comment = Comment(task_id=task_id, content='Test Comment')
        db.session.add(comment)
        db.session.commit()
        comment_id = comment.id
        db.session.expunge(comment)
        object.__setattr__(comment, 'id', comment_id)
        object.__setattr__(comment, 'task_id', task_id)
        return comment

