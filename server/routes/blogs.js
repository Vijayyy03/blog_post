const express = require('express');
const { body } = require('express-validator');
const { auth } = require('../middleware/auth');
const { 
  getAllBlogs, 
  getBlog, 
  createBlog, 
  updateBlog, 
  deleteBlog, 
  getUserBlogs 
} = require('../controllers/blogController');

const router = express.Router();

// Validation middleware
const blogValidation = [
  body('title')
    .trim()
    .isLength({ min: 3, max: 200 })
    .withMessage('Title must be between 3 and 200 characters'),
  body('content')
    .trim()
    .isLength({ min: 10 })
    .withMessage('Content must be at least 10 characters long'),
  body('excerpt')
    .optional()
    .trim()
    .isLength({ max: 300 })
    .withMessage('Excerpt cannot be more than 300 characters'),
  body('tags')
    .optional()
    .isString()
    .withMessage('Tags must be a string'),
  body('featuredImage')
    .optional()
    .isURL()
    .withMessage('Featured image must be a valid URL')
];

// Public routes
router.get('/', getAllBlogs);
router.get('/:id', getBlog);

// Protected routes
router.post('/', auth, blogValidation, createBlog);
router.put('/:id', auth, blogValidation, updateBlog);
router.delete('/:id', auth, deleteBlog);
router.get('/user/my-blogs', auth, getUserBlogs);

module.exports = router; 