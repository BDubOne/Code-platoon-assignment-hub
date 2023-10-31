import { useState } from 'react'

import './App.css'
  


function App() {  
  let [tasks, setTasks] = useState([]);
  let [taskInput, setTaskInput] = useState('');

  const addTask =(e) => {
    e.preventDefault();

  
    const taskIn = taskInput.trim();
    if (taskIn != '') {
      const newTask = {
        id: Date.now(),
        text: taskIn,
        completed: false
      };

      setTasks(prevTasks => [...prevTasks, newTask]);
      setTaskInput("");
    }
  
  }
  
  const removeTask = (taskId) => {
    setTasks(prevTasks => prevTasks.filter(task =>task.id !== taskId));

  }

  const markComplete = (taskId) => {
    setTasks(prevTasks =>
      prevTasks.map(task =>
        task.id === taskId ? {...task, completed: !task.completed } : task
        )
      );
    }


  return (
    <>
      <h1>To-Do List</h1>    
      <form onSubmit={addTask}>
        <input 
          id="inputBar"
          type="text"
          value={taskInput}
          onChange={(e) => setTaskInput(e.target.value)}
          /> 
        <button id="submitButton" type='submit'>Submit</button>
      </form>
      <ul id='taskList'>
        {tasks.map(task => (
          <li key= {task.id}>
            <input
            type="checkbox"
            checked={task.completed}
            onChange={()=> markComplete(task.id)}
            />
            {task.text}
            <button onClick={() => removeTask(task.id)}>Remove</button>
          </li>
        ))}
      </ul>

    </>
  )
}
export default App
