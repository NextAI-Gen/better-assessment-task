# Git Setup and Push Guide

## Step 1: Install Git

1. Download Git for Windows from: https://git-scm.com/download/win
2. Run the installer (use default settings)
3. Restart your terminal/PowerShell after installation

## Step 2: Configure Git (First Time Only)

After installing Git, open a new PowerShell window and run:

```powershell
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

## Step 3: Push Your Code to GitHub

Once Git is installed, run these commands in your project folder:

```powershell
# Navigate to your project
cd "E:\Betterment Company"

# Initialize Git
git init

# Add all files
git add .

# Create first commit
git commit -m "Initial commit: Task Manager Application"

# Add your GitHub repository as remote
git remote add origin https://github.com/NextAI-Gen/better-assessment-task.git

# Push to GitHub
git branch -M main
git push -u origin main
```

## Step 4: Create Branches for Tasks

After pushing, create separate branches for each task:

```powershell
# Create branch for Task #1
git checkout -b task-1-comments-api
git add backend/app/routes/comment_routes.py backend/app/tests/test_comment_routes.py
git commit -m "Task #1: Add Comments CRUD APIs with comprehensive tests"
git push -u origin task-1-comments-api

# Create branch for Task #2
git checkout main
git checkout -b task-2-tasks-frontend
git add frontend/
git commit -m "Task #2: Add Tasks CRUD Frontend interface"
git push -u origin task-2-tasks-frontend
```

## Step 5: Create Pull Requests

1. Go to: https://github.com/NextAI-Gen/better-assessment-task
2. Click "Pull requests" tab
3. Click "New pull request"
4. Select `task-1-comments-api` branch → `main`
5. Click "Create pull request"
6. Repeat for `task-2-tasks-frontend`

