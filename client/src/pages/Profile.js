import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import { blogService } from '../services/blogService';
import { format } from 'date-fns';
import { 
  User, 
  Mail, 
  Calendar, 
  Edit, 
  Trash2, 
  Plus,
  FileText
} from 'lucide-react';
import BlogCard from '../components/BlogCard';
import toast from 'react-hot-toast';

const Profile = () => {
  const { user } = useAuth();
  const [blogs, setBlogs] = useState([]);
  const [loading, setLoading] = useState(true);
  const [deleting, setDeleting] = useState(null);

  useEffect(() => {
    fetchUserBlogs();
  }, []);

  const fetchUserBlogs = async () => {
    try {
      setLoading(true);
      const userBlogs = await blogService.getUserBlogs();
      setBlogs(userBlogs);
    } catch (error) {
      toast.error(error.message);
    } finally {
      setLoading(false);
    }
  };

  const handleDelete = async (blogSlug) => {
    if (!window.confirm('Are you sure you want to delete this blog?')) {
      return;
    }

    setDeleting(blogSlug);
    try {
      await blogService.deleteBlog(blogSlug);
      toast.success('Blog deleted successfully');
      fetchUserBlogs(); // Refresh the list
    } catch (error) {
      toast.error(error.message);
    } finally {
      setDeleting(null);
    }
  };

  return (
    <div className="max-w-6xl mx-auto">
      {/* Profile Header */}
      <div className="card mb-8">
        <div className="flex items-center space-x-6">
          <div className="w-20 h-20 bg-primary-600 rounded-full flex items-center justify-center">
            <User className="w-10 h-10 text-white" />
          </div>
          <div className="flex-1">
            <h1 className="text-3xl font-bold text-gray-900 mb-2">{user.name}</h1>
            <div className="flex items-center space-x-4 text-gray-600">
              <div className="flex items-center space-x-1">
                <Mail className="w-4 h-4" />
                <span>{user.email}</span>
              </div>
              <div className="flex items-center space-x-1">
                <FileText className="w-4 h-4" />
                <span>{blogs.length} blog{blogs.length !== 1 ? 's' : ''}</span>
              </div>
            </div>
          </div>
          <Link
            to="/create-blog"
            className="btn-primary flex items-center space-x-2"
          >
            <Plus className="w-5 h-5" />
            <span>Create Blog</span>
          </Link>
        </div>
      </div>

      {/* User's Blogs */}
      <div>
        <div className="flex items-center justify-between mb-6">
          <h2 className="text-2xl font-bold text-gray-900">Your Blogs</h2>
          {blogs.length > 0 && (
            <span className="text-sm text-gray-600">
              {blogs.length} blog{blogs.length !== 1 ? 's' : ''} published
            </span>
          )}
        </div>

        {loading ? (
          <div className="flex items-center justify-center py-12">
            <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-primary-600"></div>
          </div>
        ) : blogs.length === 0 ? (
          <div className="text-center py-12">
            <div className="text-gray-400 mb-4">
              <FileText className="w-16 h-16 mx-auto" />
            </div>
            <h3 className="text-xl font-semibold text-gray-900 mb-2">
              No blogs yet
            </h3>
            <p className="text-gray-600 mb-6">
              Start sharing your thoughts and ideas with the world
            </p>
            <Link to="/create-blog" className="btn-primary">
              Create Your First Blog
            </Link>
          </div>
        ) : (
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {blogs.map((blog) => (
              <div key={blog.id} className="relative">
                <BlogCard blog={blog} />
                <div className="absolute top-4 right-4 flex items-center space-x-2">
                  <Link
                    to={`/edit-blog/${blog.slug}`}
                    className="p-2 bg-white rounded-full shadow-md hover:shadow-lg transition-shadow"
                    title="Edit blog"
                  >
                    <Edit className="w-4 h-4 text-primary-600" />
                  </Link>
                  <button
                    onClick={() => handleDelete(blog.slug)}
                    disabled={deleting === blog.slug}
                    className="p-2 bg-white rounded-full shadow-md hover:shadow-lg transition-shadow disabled:opacity-50"
                    title="Delete blog"
                  >
                    {deleting === blog.slug ? (
                      <div className="animate-spin rounded-full h-4 w-4 border-b-2 border-red-600"></div>
                    ) : (
                      <Trash2 className="w-4 h-4 text-red-600" />
                    )}
                  </button>
                </div>
              </div>
            ))}
          </div>
        )}
      </div>

      {/* Account Information */}
      <div className="mt-12">
        <h3 className="text-xl font-semibold text-gray-900 mb-4">Account Information</h3>
        <div className="card">
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                Full Name
              </label>
              <p className="text-gray-900">{user.name}</p>
            </div>
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                Email Address
              </label>
              <p className="text-gray-900">{user.email}</p>
            </div>
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                Member Since
              </label>
              <p className="text-gray-900">
                {format(new Date(user.date_joined || Date.now()), 'MMMM yyyy')}
              </p>
            </div>
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                Total Blogs
              </label>
              <p className="text-gray-900">{blogs.length}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Profile; 