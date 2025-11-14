import React from 'react';
import './App.css';
import TaskManager from './components/TaskManager';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Task Manager</h1>
        <p>Manage your tasks efficiently</p>
      </header>
      <main className="App-main">
        <TaskManager />
      </main>
    </div>
  );
}

export default App;

