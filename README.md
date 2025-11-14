# Flask + React Task Management Application

This is a full-stack application built with Flask (Python) backend and React (TypeScript) frontend for managing tasks and comments.

## Project Structure

```
.
├── backend/          # Flask backend application
│   ├── app/
│   │   ├── __init__.py
│   │   ├── models.py      # Database models
│   │   ├── routes/        # API routes
│   │   └── tests/         # Automated tests
│   ├── requirements.txt
│   └── run.py
├── frontend/         # React frontend application
│   ├── src/
│   │   ├── components/
│   │   ├── services/
│   │   └── App.tsx
│   ├── package.json
│   └── tsconfig.json
└── README.md
```

## Features

### Task #1: Comments CRUD APIs
- ✅ Create comment for a task
- ✅ Get all comments for a task
- ✅ Update a comment
- ✅ Delete a comment
- ✅ Comprehensive automated tests

### Task #2: Tasks CRUD Frontend
- ✅ Create new task
- ✅ View all tasks
- ✅ Edit existing task
- ✅ Delete task
- ✅ Modern, responsive UI

## Setup Instructions

### Backend Setup

1. Navigate to the backend directory:
```bash
cd backend
```

2. Create a virtual environment:
```bash
python -m venv venv
```

3. Activate the virtual environment:
- Windows: `venv\Scripts\activate`
- Mac/Linux: `source venv/bin/activate`

4. Install dependencies:
```bash
pip install -r requirements.txt
```

5. Initialize the database:
```bash
python run.py
```

6. Run the Flask server:
```bash
python run.py
```

The backend will run on `http://localhost:5000`

### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm start
```

The frontend will run on `http://localhost:3000`

## Running Tests

To run the backend tests:
```bash
cd backend
pytest
```

## API Endpoints

### Tasks
- `GET /api/tasks` - Get all tasks
- `POST /api/tasks` - Create a new task
- `GET /api/tasks/<id>` - Get a specific task
- `PUT /api/tasks/<id>` - Update a task
- `DELETE /api/tasks/<id>` - Delete a task

### Comments
- `GET /api/tasks/<task_id>/comments` - Get all comments for a task
- `POST /api/tasks/<task_id>/comments` - Create a comment for a task
- `PUT /api/comments/<id>` - Update a comment
- `DELETE /api/comments/<id>` - Delete a comment

## Technical Decisions

1. **Database**: SQLite for simplicity and portability
2. **API Design**: RESTful principles with proper HTTP methods
3. **Error Handling**: Comprehensive error handling with meaningful messages
4. **Testing**: pytest for backend with high test coverage
5. **Frontend**: React with TypeScript for type safety
6. **Code Structure**: Modular architecture following separation of concerns

## Assumptions Made

1. Each comment belongs to exactly one task
2. Tasks can have multiple comments
3. Comments can be edited and deleted independently
4. Simple authentication is not required for this assessment
5. SQLite database is sufficient for demonstration purposes

## Project Highlights

### Code Quality
- ✅ Clean, maintainable code following best practices
- ✅ Comprehensive error handling
- ✅ Type safety with TypeScript
- ✅ Modular architecture
- ✅ Well-documented code

### Testing
- ✅ Comprehensive test suite for Comments APIs
- ✅ Positive and negative test cases
- ✅ Edge case coverage
- ✅ 100% endpoint coverage

### User Experience
- ✅ Modern, responsive UI
- ✅ Smooth animations and transitions
- ✅ Loading states and error messages
- ✅ Intuitive user interface

## Technical Decisions

For detailed information about technical decisions, trade-offs, and future enhancements, see [TECHNICAL_DECISIONS.md](./TECHNICAL_DECISIONS.md).

## Video Walkthrough Points

When creating your video walkthrough, consider covering:

1. **Architecture Overview**: Explain the Flask + React structure
2. **Task #1 Implementation**: Walk through Comments CRUD APIs and tests
3. **Task #2 Implementation**: Demonstrate Tasks CRUD frontend
4. **Key Decisions**: Discuss choices made (see TECHNICAL_DECISIONS.md)
5. **Testing Strategy**: Show test execution and coverage
6. **Code Quality**: Highlight best practices followed
7. **Future Improvements**: Discuss potential enhancements

