import React from 'react';
import { Task } from '../services/api';
import './TaskCard.css';

interface TaskCardProps {
  task: Task;
  onEdit: (task: Task) => void;
  onDelete: (id: number) => void;
}

const TaskCard: React.FC<TaskCardProps> = ({ task, onEdit, onDelete }) => {
  const getStatusColor = (status: string) => {
    switch (status.toLowerCase()) {
      case 'completed':
        return '#4caf50';
      case 'in_progress':
        return '#2196f3';
      default:
        return '#ff9800';
    }
  };

  const formatDate = (dateString: string) => {
    const date = new Date(dateString);
    return date.toLocaleDateString('en-US', {
      year: 'numeric',
      month: 'short',
      day: 'numeric',
    });
  };

  return (
    <div className="task-card">
      <div className="task-card-header">
        <h3 className="task-title">{task.title}</h3>
        <span
          className="task-status"
          style={{ backgroundColor: getStatusColor(task.status) }}
        >
          {task.status.replace('_', ' ').toUpperCase()}
        </span>
      </div>

      {task.description && (
        <p className="task-description">{task.description}</p>
      )}

      <div className="task-meta">
        <div className="task-info">
          <span className="task-date">
            Created: {formatDate(task.created_at)}
          </span>
          {task.comments_count !== undefined && task.comments_count > 0 && (
            <span className="task-comments">
              {task.comments_count} {task.comments_count === 1 ? 'comment' : 'comments'}
            </span>
          )}
        </div>
      </div>

      <div className="task-actions">
        <button
          onClick={() => onEdit(task)}
          className="btn btn-edit"
          aria-label={`Edit task ${task.title}`}
        >
          Edit
        </button>
        <button
          onClick={() => onDelete(task.id)}
          className="btn btn-delete"
          aria-label={`Delete task ${task.title}`}
        >
          Delete
        </button>
      </div>
    </div>
  );
};

export default TaskCard;

