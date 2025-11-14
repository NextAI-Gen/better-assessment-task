# Push Your Code to GitHub - Step by Step

## Important: Restart PowerShell First!

After installing Git, you MUST close and reopen PowerShell for it to work.

## Step 1: Open a NEW PowerShell Window

1. Close your current PowerShell/terminal
2. Open a NEW PowerShell window
3. Navigate to your project:
   ```powershell
   cd "E:\Betterment Company"
   ```

## Step 2: Verify Git is Working

```powershell
git --version
```

You should see something like: `git version 2.51.2`

## Step 3: Configure Git (First Time Only)

If you haven't configured Git before, run:

```powershell
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

Replace with your actual name and email.

## Step 4: Initialize and Push Your Code

Run these commands one by one:

```powershell
# Initialize Git repository
git init

# Add all files
git add .

# Create first commit
git commit -m "Initial commit: Task Manager Application - Flask + React"

# Add your GitHub repository
git remote add origin https://github.com/NextAI-Gen/better-assessment-task.git

# Push to GitHub
git branch -M main
git push -u origin main
```

**Note:** When you run `git push`, GitHub will ask for your username and password. 
- Username: Your GitHub username
- Password: Use a **Personal Access Token** (not your GitHub password)

### How to Create Personal Access Token:
1. Go to: https://github.com/settings/tokens
2. Click "Generate new token" → "Generate new token (classic)"
3. Give it a name like "Better Assessment"
4. Select scopes: Check "repo" (this gives full repository access)
5. Click "Generate token"
6. Copy the token (you'll only see it once!)
7. Use this token as your password when pushing

## Step 5: Create Branches for Tasks

After pushing, create branches for each task:

```powershell
# Create branch for Task #1 (Comments API)
git checkout -b task-1-comments-api
git add backend/app/routes/comment_routes.py backend/app/tests/test_comment_routes.py backend/app/models.py
git commit -m "Task #1: Add Comments CRUD APIs with comprehensive tests"
git push -u origin task-1-comments-api

# Create branch for Task #2 (Tasks Frontend)
git checkout main
git checkout -b task-2-tasks-frontend
git add frontend/
git commit -m "Task #2: Add Tasks CRUD Frontend interface"
git push -u origin task-2-tasks-frontend
```

## Step 6: Create Pull Requests on GitHub

1. Go to: https://github.com/NextAI-Gen/better-assessment-task
2. Click "Pull requests" tab
3. Click "New pull request"
4. For Task #1:
   - Base: `main` ← Compare: `task-1-comments-api`
   - Click "Create pull request"
   - Title: "Task #1: Comments CRUD APIs"
   - Description: "Implements Comments CRUD APIs with comprehensive automated tests"
5. Repeat for Task #2:
   - Base: `main` ← Compare: `task-2-tasks-frontend`
   - Title: "Task #2: Tasks CRUD Frontend"
   - Description: "Implements Tasks CRUD Frontend interface with React and TypeScript"

## Troubleshooting

If Git still doesn't work after restarting PowerShell:
1. Check if Git is installed: Look for "Git Bash" in Start menu
2. Try using Git Bash instead of PowerShell
3. Or manually add Git to PATH (usually: `C:\Program Files\Git\cmd`)

