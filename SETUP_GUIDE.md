# Quick Setup Guide

This guide will help you get the application up and running quickly.

## Prerequisites

- Python 3.8 or higher
- Node.js 16 or higher and npm
- Git (for version control)

## Step-by-Step Setup

### 1. Backend Setup

```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python run.py
```

The backend will start on `http://localhost:5000`

### 2. Frontend Setup

Open a new terminal window:

```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Start development server
npm start
```

The frontend will start on `http://localhost:3000` and automatically open in your browser.

### 3. Running Tests

In the backend directory (with virtual environment activated):

```bash
# Run all tests
pytest

# Run with verbose output
pytest -v

# Run specific test file
pytest app/tests/test_comment_routes.py
```

## Verifying the Setup

### Backend Verification

1. Check if the server is running: Visit `http://localhost:5000/api/tasks`
2. You should see: `{"success":true,"data":[]}`

### Frontend Verification

1. Open `http://localhost:3000` in your browser
2. You should see the Task Manager interface
3. Try creating a new task

### Test Verification

Run the test suite and verify all tests pass:

```bash
cd backend
pytest -v
```

You should see all tests passing with green checkmarks.

## Common Issues

### Backend Issues

**Issue**: `ModuleNotFoundError`
- **Solution**: Make sure virtual environment is activated and dependencies are installed

**Issue**: `Port already in use`
- **Solution**: Change the port in `run.py` or kill the process using port 5000

### Frontend Issues

**Issue**: `npm install` fails
- **Solution**: Make sure Node.js version is 16 or higher. Try `npm cache clean --force`

**Issue**: CORS errors
- **Solution**: Make sure backend is running and CORS is enabled (already configured)

**Issue**: Cannot connect to API
- **Solution**: Verify backend is running on port 5000 and check the proxy setting in `package.json`

## Next Steps

1. **Fork the Repository**: Fork the original template repository to your GitHub account
2. **Create Feature Branches**: Create separate branches for Task #1 and Task #2
3. **Make Commits**: Follow good commit practices (see PR etiquette guide)
4. **Create PRs**: Create separate PRs for each task
5. **Record Video**: Create a walkthrough video explaining your approach

## Development Tips

1. **Backend Development**:
   - Use Flask's debug mode (already enabled) for auto-reload
   - Check terminal for error messages
   - Use Postman or curl to test APIs directly

2. **Frontend Development**:
   - React dev server auto-reloads on file changes
   - Check browser console for errors
   - Use React DevTools for debugging

3. **Testing**:
   - Run tests frequently during development
   - Write tests before fixing bugs (TDD approach)
   - Keep test coverage high

## Project Structure Reference

```
.
├── backend/
│   ├── app/
│   │   ├── __init__.py          # App factory
│   │   ├── models.py            # Database models
│   │   ├── routes/              # API routes
│   │   │   ├── task_routes.py
│   │   │   └── comment_routes.py
│   │   └── tests/               # Test suite
│   │       ├── conftest.py
│   │       └── test_comment_routes.py
│   ├── requirements.txt
│   ├── pytest.ini
│   └── run.py
├── frontend/
│   ├── src/
│   │   ├── components/          # React components
│   │   ├── services/            # API service layer
│   │   ├── App.tsx
│   │   └── index.tsx
│   ├── package.json
│   └── tsconfig.json
├── README.md
├── TECHNICAL_DECISIONS.md
└── SETUP_GUIDE.md
```

## Need Help?

If you encounter any issues:
1. Check the error messages carefully
2. Review the README.md for detailed documentation
3. Check TECHNICAL_DECISIONS.md for implementation details
4. Ensure all prerequisites are installed correctly

