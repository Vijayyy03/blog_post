import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useForm } from 'react-hook-form';
import { blogService } from '../services/blogService';
import { ArrowLeft, Save, Image, Tag } from 'lucide-react';
import toast from 'react-hot-toast';

const CreateBlog = () => {
  const navigate = useNavigate();
  const [isLoading, setIsLoading] = useState(false);
  const [content, setContent] = useState('');

  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm();

  const onSubmit = async (data) => {
    if (!content.trim()) {
      toast.error('Blog content is required');
      return;
    }

    setIsLoading(true);
    try {
      const blogData = {
        ...data,
        content,
        tags: data.tags ? data.tags.split(',').map(tag => tag.trim()) : [],
      };

      await blogService.createBlog(blogData);
      toast.success('Blog created successfully!');
      navigate('/');
    } catch (error) {
      toast.error(error.message);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="max-w-4xl mx-auto">
      <div className="mb-8">
        <button
          onClick={() => navigate(-1)}
          className="flex items-center space-x-2 text-gray-600 hover:text-gray-900 transition-colors"
        >
          <ArrowLeft className="w-5 h-5" />
          <span>Back</span>
        </button>
        <h1 className="text-3xl font-bold text-gray-900 mt-4">Create New Blog</h1>
        <p className="text-gray-600 mt-2">Share your thoughts and ideas with the world</p>
      </div>

      <form onSubmit={handleSubmit(onSubmit)} className="space-y-6">
        <div className="card">
          <div className="space-y-6">
            {/* Title */}
            <div>
              <label htmlFor="title" className="block text-sm font-medium text-gray-700 mb-2">
                Blog Title *
              </label>
              <input
                type="text"
                id="title"
                {...register('title', {
                  required: 'Title is required',
                  minLength: {
                    value: 3,
                    message: 'Title must be at least 3 characters',
                  },
                  maxLength: {
                    value: 200,
                    message: 'Title cannot exceed 200 characters',
                  },
                })}
                className="input-field"
                placeholder="Enter your blog title"
              />
              {errors.title && (
                <p className="mt-1 text-sm text-red-600">{errors.title.message}</p>
              )}
            </div>

            {/* Featured Image */}
            <div>
              <label htmlFor="featuredImage" className="block text-sm font-medium text-gray-700 mb-2">
                Featured Image URL
              </label>
              <div className="relative">
                <input
                  type="url"
                  id="featuredImage"
                  {...register('featuredImage', {
                    pattern: {
                      value: /^https?:\/\/.+/,
                      message: 'Please enter a valid URL',
                    },
                  })}
                  className="input-field pl-10"
                  placeholder="https://example.com/image.jpg"
                />
                <Image className="absolute left-3 top-1/2 transform -translate-y-1/2 w-5 h-5 text-gray-400" />
              </div>
              {errors.featuredImage && (
                <p className="mt-1 text-sm text-red-600">{errors.featuredImage.message}</p>
              )}
            </div>

            {/* Tags */}
            <div>
              <label htmlFor="tags" className="block text-sm font-medium text-gray-700 mb-2">
                Tags
              </label>
              <div className="relative">
                <input
                  type="text"
                  id="tags"
                  {...register('tags')}
                  className="input-field pl-10"
                  placeholder="technology, programming, web development"
                />
                <Tag className="absolute left-3 top-1/2 transform -translate-y-1/2 w-5 h-5 text-gray-400" />
              </div>
              <p className="mt-1 text-sm text-gray-500">
                Separate tags with commas
              </p>
            </div>

            {/* Excerpt */}
            <div>
              <label htmlFor="excerpt" className="block text-sm font-medium text-gray-700 mb-2">
                Excerpt
              </label>
              <textarea
                id="excerpt"
                rows={3}
                {...register('excerpt', {
                  maxLength: {
                    value: 300,
                    message: 'Excerpt cannot exceed 300 characters',
                  },
                })}
                className="input-field"
                placeholder="A brief summary of your blog post..."
              />
              {errors.excerpt && (
                <p className="mt-1 text-sm text-red-600">{errors.excerpt.message}</p>
              )}
            </div>
          </div>
        </div>

        {/* Content */}
        <div className="card">
          <label htmlFor="content" className="block text-sm font-medium text-gray-700 mb-2">
            Blog Content *
          </label>
          <textarea
            id="content"
            rows={15}
            value={content}
            onChange={(e) => setContent(e.target.value)}
            className="input-field font-mono"
            placeholder="Write your blog content here..."
          />
          <div className="mt-2 flex justify-between items-center text-sm text-gray-500">
            <span>{content.length} characters</span>
            <span>{content.split(' ').filter(word => word.length > 0).length} words</span>
          </div>
        </div>

        {/* Submit Button */}
        <div className="flex justify-end space-x-4">
          <button
            type="button"
            onClick={() => navigate('/')}
            className="btn-secondary"
          >
            Cancel
          </button>
          <button
            type="submit"
            disabled={isLoading || !content.trim()}
            className="btn-primary flex items-center space-x-2"
          >
            {isLoading ? (
              <div className="animate-spin rounded-full h-5 w-5 border-b-2 border-white"></div>
            ) : (
              <Save className="w-5 h-5" />
            )}
            <span>{isLoading ? 'Creating...' : 'Create Blog'}</span>
          </button>
        </div>
      </form>
    </div>
  );
};

export default CreateBlog; 