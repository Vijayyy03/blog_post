# MongoDB Setup Guide

## Option 1: Install MongoDB Locally

### Windows Installation:
1. Download MongoDB Community Server from: https://www.mongodb.com/try/download/community
2. Run the installer and follow the setup wizard
3. MongoDB will be installed as a service and start automatically
4. The default connection string will be: `mongodb://localhost:27017/omnify-blog`

### macOS Installation (using Homebrew):
```bash
brew tap mongodb/brew
brew install mongodb-community
brew services start mongodb/brew/mongodb-community
```

### Linux Installation (Ubuntu/Debian):
```bash
# Import MongoDB public GPG key
wget -qO - https://www.mongodb.org/static/pgp/server-6.0.asc | sudo apt-key add -

# Create list file for MongoDB
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/6.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-6.0.list

# Update package database
sudo apt-get update

# Install MongoDB
sudo apt-get install -y mongodb-org

# Start MongoDB
sudo systemctl start mongod
sudo systemctl enable mongod
```

## Option 2: Use MongoDB Atlas (Cloud)

1. Go to https://www.mongodb.com/cloud/atlas
2. Create a free account
3. Create a new cluster (free tier available)
4. Get your connection string
5. Update the `.env` file in the server directory:

```env
MONGODB_URI= Paste Your URL
```

## Option 3: Use Docker (Recommended for Development)

### Install Docker Desktop:
1. Download from: https://www.docker.com/products/docker-desktop
2. Install and start Docker Desktop

### Run MongoDB with Docker:
```bash
docker run -d --name mongodb -p 27017:27017 mongo:latest
```

### Or use Docker Compose:
Create a `docker-compose.yml` file in the project root:

```yaml
version: '3.8'
services:
  mongodb:
    image: mongo:latest
    container_name: omnify-mongodb
    ports:
      - "27017:27017"
    environment:
      - MONGO_INITDB_DATABASE=omnify-blog
    volumes:
      - mongodb_data:/data/db

volumes:
  mongodb_data:
```

Then run:
```bash
docker-compose up -d
```

## Verify Installation

After installation, verify MongoDB is running:

```bash
# Check if MongoDB is running
mongosh --eval "db.runCommand('ping')"
```

## Troubleshooting

### MongoDB not starting:
1. Check if the port 27017 is available
2. Check MongoDB logs: `tail -f /var/log/mongodb/mongod.log`
3. Ensure you have proper permissions

### Connection issues:
1. Verify the connection string in `.env`
2. Check if MongoDB is running on the correct port
3. Ensure firewall allows connections to port 27017

## Quick Start

Once MongoDB is installed and running:

1. Start the backend server:
```bash
cd server
npm run dev
```

2. Start the frontend:
```bash
cd client
npm start
```

3. The application should now work with registration, login, and blog creation! 