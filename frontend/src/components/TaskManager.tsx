import React, { useState, useEffect } from 'react';
import { Task, taskApi } from '../services/api';
import TaskList from './TaskList';
import TaskForm from './TaskForm';
import './TaskManager.css';

const TaskManager: React.FC = () => {
  const [tasks, setTasks] = useState<Task[]>([]);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);
  const [editingTask, setEditingTask] = useState<Task | null>(null);
  const [showForm, setShowForm] = useState<boolean>(false);

  useEffect(() => {
    fetchTasks();
  }, []);

  const fetchTasks = async () => {
    try {
      setLoading(true);
      setError(null);
      const data = await taskApi.getAll();
      setTasks(data);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to load tasks');
    } finally {
      setLoading(false);
    }
  };

  const handleCreateTask = async (taskData: { title: string; description: string; status: string }) => {
    try {
      setError(null);
      await taskApi.create(taskData);
      await fetchTasks();
      setShowForm(false);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to create task');
      throw err;
    }
  };

  const handleUpdateTask = async (id: number, taskData: { title: string; description: string; status: string }) => {
    try {
      setError(null);
      await taskApi.update(id, taskData);
      await fetchTasks();
      setEditingTask(null);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to update task');
      throw err;
    }
  };

  const handleDeleteTask = async (id: number) => {
    if (!window.confirm('Are you sure you want to delete this task?')) {
      return;
    }

    try {
      setError(null);
      await taskApi.delete(id);
      await fetchTasks();
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to delete task');
    }
  };

  const handleEditClick = (task: Task) => {
    setEditingTask(task);
    setShowForm(true);
  };

  const handleCancelEdit = () => {
    setEditingTask(null);
    setShowForm(false);
  };

  const handleNewTaskClick = () => {
    setEditingTask(null);
    setShowForm(true);
  };

  if (loading) {
    return (
      <div className="loading-container">
        <div className="spinner"></div>
        <p>Loading tasks...</p>
      </div>
    );
  }

  return (
    <div className="task-manager">
      {error && (
        <div className="error-message" role="alert">
          {error}
          <button onClick={() => setError(null)} className="error-close">×</button>
        </div>
      )}

      <div className="task-manager-header">
        <h2>Tasks</h2>
        <button 
          onClick={handleNewTaskClick} 
          className="btn btn-primary"
          disabled={showForm && !editingTask}
        >
          {showForm && !editingTask ? 'Creating...' : '+ New Task'}
        </button>
      </div>

      {showForm && (
        <TaskForm
          task={editingTask}
          onSubmit={editingTask 
            ? (data) => handleUpdateTask(editingTask.id, data)
            : handleCreateTask
          }
          onCancel={handleCancelEdit}
        />
      )}

      <TaskList
        tasks={tasks}
        onEdit={handleEditClick}
        onDelete={handleDeleteTask}
      />

      {tasks.length === 0 && !showForm && (
        <div className="empty-state">
          <p>No tasks yet. Create your first task to get started!</p>
        </div>
      )}
    </div>
  );
};

export default TaskManager;

