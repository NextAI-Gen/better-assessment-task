# Technical Decisions & Approach

This document outlines the key technical decisions made during the implementation of the Task Management application.

## Architecture Overview

### Backend (Flask)
- **Framework**: Flask with SQLAlchemy ORM
- **Database**: SQLite (for simplicity and portability)
- **Structure**: Application factory pattern with blueprints for modularity
- **API Design**: RESTful principles with proper HTTP methods and status codes

### Frontend (React + TypeScript)
- **Framework**: React 18 with TypeScript for type safety
- **State Management**: React hooks (useState, useEffect)
- **HTTP Client**: Axios for API communication
- **Styling**: CSS modules with modern, responsive design

## Task #1: Comments CRUD APIs

### Implementation Details

1. **API Endpoints**:
   - `GET /api/tasks/<task_id>/comments` - Retrieve all comments for a task
   - `POST /api/tasks/<task_id>/comments` - Create a new comment
   - `PUT /api/comments/<id>` - Update an existing comment
   - `DELETE /api/comments/<id>` - Delete a comment

2. **Key Features**:
   - Proper validation (content required, cannot be empty)
   - Error handling with meaningful messages
   - Task existence verification before comment operations
   - Comments ordered by creation date (newest first)
   - Cascade delete (comments deleted when task is deleted)

3. **Database Design**:
   - Foreign key relationship between Comments and Tasks
   - Timestamps for created_at and updated_at
   - Indexed task_id for efficient queries

### Testing Strategy

Comprehensive test suite covering:
- ✅ Successful CRUD operations
- ✅ Error cases (missing data, empty content, invalid IDs)
- ✅ Edge cases (empty lists, multiple comments)
- ✅ Cascade deletion
- ✅ Data validation

**Test Coverage**: All endpoints tested with positive and negative test cases.

## Task #2: Tasks CRUD Frontend

### Implementation Details

1. **Components Structure**:
   - `TaskManager`: Main container component managing state
   - `TaskList`: Displays list of tasks
   - `TaskCard`: Individual task display component
   - `TaskForm`: Reusable form for create/edit operations

2. **User Experience**:
   - Modern, responsive UI with smooth animations
   - Loading states and error handling
   - Confirmation dialogs for destructive actions
   - Form validation with visual feedback
   - Status indicators with color coding

3. **State Management**:
   - Local component state for simplicity
   - API calls abstracted in service layer
   - Optimistic UI updates with error rollback

### Design Decisions

1. **Single Form Component**: Reused for both create and edit to reduce code duplication
2. **Service Layer**: Separated API logic from components for maintainability
3. **TypeScript**: Used throughout for type safety and better developer experience
4. **Responsive Design**: Mobile-first approach with breakpoints

## Code Quality Practices

1. **Error Handling**:
   - Comprehensive try-catch blocks
   - User-friendly error messages
   - Proper HTTP status codes

2. **Code Organization**:
   - Separation of concerns (routes, models, services)
   - Modular component structure
   - Reusable utilities and components

3. **Documentation**:
   - Inline comments for complex logic
   - Clear function and class docstrings
   - README with setup instructions

4. **Best Practices**:
   - RESTful API design
   - Proper HTTP methods (GET, POST, PUT, DELETE)
   - Input validation on both client and server
   - SQL injection prevention via ORM
   - CORS enabled for frontend-backend communication

## Assumptions Made

1. **Authentication**: Not required for this assessment
2. **Database**: SQLite sufficient for demonstration
3. **Comments**: Belong to exactly one task
4. **Tasks**: Can have multiple comments
5. **Status Values**: Fixed set (pending, in_progress, completed)

## Trade-offs & Technical Debt

1. **SQLite Database**: 
   - Trade-off: Simple setup vs. production scalability
   - Future: Easy to migrate to PostgreSQL/MySQL

2. **No Authentication**:
   - Trade-off: Faster development vs. security
   - Future: Can add JWT or session-based auth

3. **Local State Management**:
   - Trade-off: Simplicity vs. complex state needs
   - Future: Can migrate to Redux/Context API if needed

4. **No Real-time Updates**:
   - Trade-off: Simpler architecture vs. live updates
   - Future: Can add WebSockets or polling

## Future Enhancements

1. User authentication and authorization
2. Real-time updates via WebSockets
3. Task filtering and search
4. Comment threading/replies
5. File attachments
6. Task assignments and due dates
7. Email notifications
8. Advanced analytics and reporting

## Performance Considerations

1. **Backend**:
   - Efficient database queries with proper indexing
   - Pagination ready (can be added easily)
   - Connection pooling ready for production DB

2. **Frontend**:
   - Component lazy loading possible
   - API response caching can be added
   - Optimistic updates for better UX

## Security Considerations

1. Input validation on both client and server
2. SQL injection prevention via ORM
3. XSS prevention through React's built-in escaping
4. CORS properly configured
5. Error messages don't expose sensitive information

