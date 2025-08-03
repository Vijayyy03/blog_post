# Omnify Blog Platform

A full-stack blog application built with React, Node.js, Express, and MongoDB. Features user authentication, blog creation, and management.

## 🚀 Features

- **User Authentication**: Register, login, and profile management
- **Blog Management**: Create, edit, delete, and view blogs
- **Modern UI**: Responsive design with Tailwind CSS
- **Real-time Updates**: Dynamic content loading
- **Search & Filter**: Find blogs by tags and content
- **User Profiles**: Personal blog collections

## 🛠️ Tech Stack

### Frontend
- **React 18** - UI framework
- **React Router** - Navigation
- **Tailwind CSS** - Styling
- **Axios** - HTTP client
- **React Hook Form** - Form handling
- **React Hot Toast** - Notifications

### Backend
- **Node.js** - Runtime environment
- **Express.js** - Web framework
- **MongoDB** - Database
- **Mongoose** - ODM
- **JWT** - Authentication
- **bcryptjs** - Password hashing
- **CORS** - Cross-origin requests

## 📦 Installation

### Prerequisites
- Node.js (v14 or higher)
- MongoDB (local or Atlas)
- Git

### Quick Start

1. **Clone the repository**
```bash
git clone https://github.com/Vijayyy03/blog_post.git
cd blog_post
```

2. **Install dependencies**
```bash
# Install backend dependencies
cd server
npm install

# Install frontend dependencies
cd ../client
npm install
```

3. **Set up environment variables**
```bash
# Create .env file in server directory
cd ../server
echo "PORT=5000" > .env
echo "NODE_ENV=development" >> .env
echo "JWT_SECRET=your-super-secret-jwt-key-change-this-in-production" >> .env
echo "MONGODB_URI=mongodb://localhost:27017/omnify-blog" >> .env
```

4. **Start MongoDB**
```bash
# Option 1: Use Docker (Recommended)
docker-compose up -d

# Option 2: Install MongoDB locally
# Follow the guide in MONGODB_SETUP.md
```

5. **Start the application**
```bash
# Start backend server
cd server
npm run dev

# Start frontend (in new terminal)
cd client
npm start
```

## 🌐 Access the Application

- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:5000/api
- **MongoDB Express** (if using Docker): http://localhost:8081

## 📚 API Endpoints

### Authentication
- `POST /api/auth/register` - User registration
- `POST /api/auth/login` - User login
- `GET /api/auth/me` - Get current user

### Blogs
- `GET /api/blogs` - Get all blogs
- `GET /api/blogs/:id` - Get single blog
- `POST /api/blogs` - Create blog (authenticated)
- `PUT /api/blogs/:id` - Update blog (authenticated)
- `DELETE /api/blogs/:id` - Delete blog (authenticated)
- `GET /api/blogs/user/my-blogs` - Get user's blogs (authenticated)

## 🗂️ Project Structure

```
omnify/
├── client/                 # React frontend
│   ├── src/
│   │   ├── components/    # Reusable components
│   │   ├── pages/        # Page components
│   │   ├── services/     # API services
│   │   ├── context/      # React context
│   │   └── utils/        # Utility functions
│   └── public/           # Static files
├── server/                # Node.js backend
│   ├── controllers/      # Route controllers
│   ├── models/          # Database models
│   ├── routes/          # API routes
│   ├── middleware/      # Custom middleware
│   └── utils/           # Utility functions
├── docker-compose.yml    # Docker configuration
└── README.md            # Project documentation
```

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the `server` directory:

```env
PORT=5000
NODE_ENV=development
JWT_SECRET=your-super-secret-jwt-key-change-this-in-production
MONGODB_URI=mongodb://localhost:27017/omnify-blog
```

### MongoDB Setup

See `MONGODB_SETUP.md` for detailed installation instructions.

## 🚀 Deployment

### Frontend (Vercel/Netlify)
```bash
cd client
npm run build
```

### Backend (Heroku/Railway)
```bash
cd server
# Set environment variables in your hosting platform
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License.

## 🆘 Support

If you encounter any issues:

1. Check the [MongoDB Setup Guide](MONGODB_SETUP.md)
2. Review the [Fixes Summary](FIXES_SUMMARY.md)
3. Ensure all dependencies are installed
4. Verify MongoDB is running

## 🎯 Features Roadmap

- [ ] Image upload functionality
- [ ] Rich text editor
- [ ] Comments system
- [ ] User roles and permissions
- [ ] Email notifications
- [ ] Social media sharing
- [ ] Analytics dashboard
- [ ] Mobile app

---

**Built with ❤️ by the Omnify Team** 