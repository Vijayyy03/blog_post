import React from 'react';
import { Link } from 'react-router-dom';
import { Calendar, Clock, User, Tag } from 'lucide-react';
import { format } from 'date-fns';

const BlogCard = ({ blog }) => {
  return (
    <div className="card hover:shadow-md transition-shadow duration-200">
      {blog.featured_image && (
        <div className="mb-4">
          <img
            src={blog.featured_image}
            alt={blog.title}
            className="w-full h-48 object-cover rounded-lg"
          />
        </div>
      )}
      
      <div className="space-y-3">
        <div className="flex items-center space-x-4 text-sm text-gray-500">
          <div className="flex items-center space-x-1">
            <User className="w-4 h-4" />
            <span>{blog.author?.name}</span>
          </div>
          <div className="flex items-center space-x-1">
            <Calendar className="w-4 h-4" />
            <span>{blog.created_at ? format(new Date(blog.created_at), 'MMM dd, yyyy') : 'Unknown date'}</span>
          </div>
          <div className="flex items-center space-x-1">
            <Clock className="w-4 h-4" />
            <span>{blog.reading_time} min read</span>
          </div>
        </div>
        
        <Link to={`/blog/${blog.slug}`}>
          <h2 className="text-xl font-semibold text-gray-900 hover:text-primary-600 transition-colors line-clamp-2">
            {blog.title}
          </h2>
        </Link>
        
        {blog.excerpt && (
          <p className="text-gray-600 line-clamp-3">
            {blog.excerpt}
          </p>
        )}
        
        {blog.tags && blog.tags.length > 0 && (
          <div className="flex items-center space-x-2">
            <Tag className="w-4 h-4 text-gray-400" />
            <div className="flex flex-wrap gap-1">
              {blog.tags.slice(0, 3).map((tag, index) => (
                <span
                  key={index}
                  className="px-2 py-1 bg-gray-100 text-gray-600 text-xs rounded-full"
                >
                  {tag.name || tag}
                </span>
              ))}
              {blog.tags.length > 3 && (
                <span className="text-xs text-gray-500">
                  +{blog.tags.length - 3} more
                </span>
              )}
            </div>
          </div>
        )}
        
        <Link
          to={`/blog/${blog.slug}`}
          className="inline-flex items-center text-primary-600 hover:text-primary-700 font-medium text-sm transition-colors"
        >
          Read more →
        </Link>
      </div>
    </div>
  );
};

export default BlogCard; 