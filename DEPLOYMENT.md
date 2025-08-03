# Deployment Guide for Omnify Blog Application

This guide will help you deploy the Omnify Blog application to various cloud platforms.

## Prerequisites

- Node.js (v16 or higher)
- MongoDB database (local or cloud)
- Git repository
- Cloud platform account (Vercel, Netlify, Railway, Render, etc.)

## Deployment Options

### Option 1: Vercel + MongoDB Atlas (Recommended)

#### Backend Deployment (Vercel)

1. **Prepare the backend:**
   ```bash
   cd server
   npm install
   ```

2. **Create a Vercel account** and install Vercel CLI:
   ```bash
   npm i -g vercel
   ```

3. **Deploy to Vercel:**
   ```bash
   cd server
   vercel
   ```

4. **Set environment variables in Vercel dashboard:**
   - `MONGODB_URI`: Your MongoDB Atlas connection string
   - `JWT_SECRET`: A secure random string
   - `NODE_ENV`: production

#### Frontend Deployment (Vercel)

1. **Update API URL** in `client/src/services/authService.js` and `client/src/services/blogService.js`:
   ```javascript
   const API_URL = process.env.REACT_APP_API_URL || 'https://your-backend-url.vercel.app/api';
   ```

2. **Deploy frontend:**
   ```bash
   cd client
   vercel
   ```

3. **Set environment variable:**
   - `REACT_APP_API_URL`: Your backend URL (e.g., https://your-backend-url.vercel.app/api)

### Option 2: Railway (Full Stack)

1. **Connect your GitHub repository to Railway**

2. **Set up environment variables:**
   - `MONGODB_URI`: MongoDB Atlas connection string
   - `JWT_SECRET`: Secure random string
   - `NODE_ENV`: production

3. **Deploy both frontend and backend**

### Option 3: Render

#### Backend Deployment

1. **Create a new Web Service on Render**

2. **Connect your GitHub repository**

3. **Configure the service:**
   - **Build Command:** `cd server && npm install`
   - **Start Command:** `cd server && npm start`
   - **Root Directory:** Leave empty

4. **Set environment variables:**
   - `MONGODB_URI`: MongoDB Atlas connection string
   - `JWT_SECRET`: Secure random string
   - `NODE_ENV`: production

#### Frontend Deployment

1. **Create a new Static Site on Render**

2. **Configure the service:**
   - **Build Command:** `cd client && npm install && npm run build`
   - **Publish Directory:** `client/build`
   - **Root Directory:** Leave empty

3. **Set environment variable:**
   - `REACT_APP_API_URL`: Your backend URL

### Option 4: Netlify + Heroku

#### Backend (Heroku)

1. **Create a Heroku account and install CLI**

2. **Deploy backend:**
   ```bash
   cd server
   heroku create your-app-name
   git add .
   git commit -m "Deploy to Heroku"
   git push heroku main
   ```

3. **Set environment variables:**
   ```bash
   heroku config:set MONGODB_URI=your-mongodb-uri
   heroku config:set JWT_SECRET=your-jwt-secret
   heroku config:set NODE_ENV=production
   ```

#### Frontend (Netlify)

1. **Build the frontend:**
   ```bash
   cd client
   npm run build
   ```

2. **Deploy to Netlify** by dragging the `build` folder to Netlify

3. **Set environment variable:**
   - `REACT_APP_API_URL`: Your Heroku backend URL

## Database Setup

### MongoDB Atlas (Recommended for Production)

1. **Create a MongoDB Atlas account**

2. **Create a new cluster**

3. **Set up database access:**
   - Create a database user with read/write permissions

4. **Set up network access:**
   - Allow access from anywhere (0.0.0.0/0) for development
   - For production, whitelist your deployment IPs

5. **Get your connection string:**
   ```
   mongodb+srv://username:password@cluster.mongodb.net/omnify-blog?retryWrites=true&w=majority
   ```

### Local MongoDB

For development, you can use a local MongoDB instance:

1. **Install MongoDB locally**

2. **Start MongoDB service**

3. **Use connection string:**
   ```
   mongodb://localhost:27017/omnify-blog
   ```

## Environment Variables

### Backend (.env)
```env
PORT=5000
MONGODB_URI=your-mongodb-connection-string
JWT_SECRET=your-super-secret-jwt-key
NODE_ENV=production
```

### Frontend (.env)
```env
REACT_APP_API_URL=https://your-backend-url.com/api
```

## Security Considerations

1. **JWT Secret:** Use a strong, random string for JWT_SECRET
2. **MongoDB:** Use strong passwords and enable authentication
3. **HTTPS:** Always use HTTPS in production
4. **CORS:** Configure CORS properly for your domain
5. **Rate Limiting:** Consider implementing rate limiting for API endpoints

## Performance Optimization

1. **Enable compression** in your backend
2. **Use CDN** for static assets
3. **Implement caching** for blog posts
4. **Optimize images** before uploading
5. **Use pagination** for large datasets

## Monitoring and Logging

1. **Set up error tracking** (Sentry, LogRocket)
2. **Monitor API performance** (New Relic, DataDog)
3. **Set up uptime monitoring** (UptimeRobot, Pingdom)
4. **Configure logging** for debugging

## Backup Strategy

1. **Database backups:** Set up automated MongoDB Atlas backups
2. **Code backups:** Use Git for version control
3. **Environment backups:** Document all environment variables

## Troubleshooting

### Common Issues

1. **CORS errors:** Ensure CORS is properly configured
2. **Database connection:** Check MongoDB URI and network access
3. **Build errors:** Ensure all dependencies are installed
4. **Environment variables:** Verify all required variables are set

### Debug Steps

1. Check server logs for errors
2. Verify database connectivity
3. Test API endpoints manually
4. Check browser console for frontend errors
5. Verify environment variables are loaded correctly

## Support

For deployment issues:
1. Check the platform's documentation
2. Review error logs
3. Test locally first
4. Contact platform support if needed

## Cost Optimization

1. **Use free tiers** when possible
2. **Monitor usage** to avoid unexpected charges
3. **Optimize database queries** to reduce costs
4. **Use CDN caching** to reduce bandwidth costs 