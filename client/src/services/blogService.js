import axios from 'axios';

const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:5000/api';

// Create axios instance with default config
const api = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Add token to requests if available
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

export const blogService = {
  async getAllBlogs(page = 1, limit = 10, search = '', tag = '') {
    try {
      const params = new URLSearchParams({
        page: page.toString(),
        limit: limit.toString(),
      });
      
      if (search) params.append('search', search);
      if (tag) params.append('tag', tag);
      
      const response = await api.get(`/blogs/?${params.toString()}`);
      return response.data;
    } catch (error) {
      throw new Error(error.response?.data?.message || 'Failed to fetch blogs');
    }
  },

  async getBlog(id) {
    try {
      const response = await api.get(`/blogs/${id}`);
      return response.data;
    } catch (error) {
      throw new Error(error.response?.data?.message || 'Failed to fetch blog');
    }
  },

  async createBlog(blogData) {
    try {
      const response = await api.post('/blogs', blogData);
      return response.data;
    } catch (error) {
      throw new Error(error.response?.data?.message || 'Failed to create blog');
    }
  },

  async updateBlog(id, blogData) {
    try {
      const response = await api.put(`/blogs/${id}`, blogData);
      return response.data;
    } catch (error) {
      throw new Error(error.response?.data?.message || 'Failed to update blog');
    }
  },

  async deleteBlog(id) {
    try {
      const response = await api.delete(`/blogs/${id}`);
      return response.data;
    } catch (error) {
      throw new Error(error.response?.data?.message || 'Failed to delete blog');
    }
  },

  async getUserBlogs() {
    try {
      const response = await api.get('/blogs/user/my-blogs');
      return response.data.blogs;
    } catch (error) {
      throw new Error(error.response?.data?.message || 'Failed to fetch user blogs');
    }
  },
}; 