import axios from 'axios';

const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:5000/api';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export interface Task {
  id: number;
  title: string;
  description: string;
  status: string;
  created_at: string;
  updated_at: string;
  comments_count?: number;
}

export interface Comment {
  id: number;
  task_id: number;
  content: string;
  created_at: string;
  updated_at: string;
}

export interface ApiResponse<T> {
  success: boolean;
  data?: T;
  error?: string;
  message?: string;
}

// Task API calls
export const taskApi = {
  getAll: async (): Promise<Task[]> => {
    const response = await api.get<ApiResponse<Task[]>>('/tasks');
    if (response.data.success && response.data.data) {
      return response.data.data;
    }
    throw new Error(response.data.error || 'Failed to fetch tasks');
  },

  getById: async (id: number): Promise<Task> => {
    const response = await api.get<ApiResponse<Task>>(`/tasks/${id}`);
    if (response.data.success && response.data.data) {
      return response.data.data;
    }
    throw new Error(response.data.error || 'Failed to fetch task');
  },

  create: async (task: { title: string; description?: string; status?: string }): Promise<Task> => {
    const response = await api.post<ApiResponse<Task>>('/tasks', task);
    if (response.data.success && response.data.data) {
      return response.data.data;
    }
    throw new Error(response.data.error || 'Failed to create task');
  },

  update: async (id: number, task: { title?: string; description?: string; status?: string }): Promise<Task> => {
    const response = await api.put<ApiResponse<Task>>(`/tasks/${id}`, task);
    if (response.data.success && response.data.data) {
      return response.data.data;
    }
    throw new Error(response.data.error || 'Failed to update task');
  },

  delete: async (id: number): Promise<void> => {
    const response = await api.delete<ApiResponse<void>>(`/tasks/${id}`);
    if (!response.data.success) {
      throw new Error(response.data.error || 'Failed to delete task');
    }
  },
};

// Comment API calls
export const commentApi = {
  getByTaskId: async (taskId: number): Promise<Comment[]> => {
    const response = await api.get<ApiResponse<Comment[]>>(`/tasks/${taskId}/comments`);
    if (response.data.success && response.data.data) {
      return response.data.data;
    }
    throw new Error(response.data.error || 'Failed to fetch comments');
  },

  create: async (taskId: number, content: string): Promise<Comment> => {
    const response = await api.post<ApiResponse<Comment>>(`/tasks/${taskId}/comments`, { content });
    if (response.data.success && response.data.data) {
      return response.data.data;
    }
    throw new Error(response.data.error || 'Failed to create comment');
  },

  update: async (id: number, content: string): Promise<Comment> => {
    const response = await api.put<ApiResponse<Comment>>(`/comments/${id}`, { content });
    if (response.data.success && response.data.data) {
      return response.data.data;
    }
    throw new Error(response.data.error || 'Failed to update comment');
  },

  delete: async (id: number): Promise<void> => {
    const response = await api.delete<ApiResponse<void>>(`/comments/${id}`);
    if (!response.data.success) {
      throw new Error(response.data.error || 'Failed to delete comment');
    }
  },
};

export default api;

