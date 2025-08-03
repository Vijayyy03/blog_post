# Railway Deployment Guide

## 🚀 Deploy to Railway

### Step 1: Connect to Railway
1. Go to [Railway.app](https://railway.app)
2. Sign up with GitHub
3. Click "New Project" → "Deploy from GitHub repo"
4. Select your repository: `Vijayyy03/blog_post`

### Step 2: Configure Project
1. Set **Root Directory** to: `server`
2. Set **Build Command** to: `npm install`
3. Set **Start Command** to: `npm start`

### Step 3: Add Environment Variables
Add these environment variables in Railway dashboard:

```
MONGODB_URI=mongodb+srv://VijayJagdale:vijay10032003@cluster0.yw2pyek.mongodb.net/omnify-blog?retryWrites=true&w=majority&appName=Cluster0
PORT=5000
NODE_ENV=production
JWT_SECRET=your-super-secret-jwt-key-change-this-in-production
```

### Step 4: Deploy
1. Click "Deploy Now"
2. Wait for deployment to complete
3. Copy the generated URL (e.g., `https://your-app.railway.app`)

### Step 5: Update Frontend
Update the frontend API URL to use your Railway backend URL.

## 🔧 Environment Variables Explained

- **MONGODB_URI**: Your MongoDB Atlas connection string
- **PORT**: Railway will set this automatically
- **NODE_ENV**: Set to production for deployment
- **JWT_SECRET**: Secret key for JWT tokens (change in production)

## 📡 API Endpoints

Your deployed API will be available at:
- `https://your-app.railway.app/api`

## 🎯 Next Steps

After Railway deployment:
1. Deploy frontend to Vercel
2. Update frontend API URL
3. Test the complete application

## 🔍 Troubleshooting

If deployment fails:
1. Check environment variables are set correctly
2. Verify MongoDB Atlas connection
3. Check Railway logs for errors
4. Ensure all dependencies are in package.json 