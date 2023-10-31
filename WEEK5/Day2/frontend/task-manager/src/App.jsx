import { useState } from 'react'

import jsonTasks from "../tasks.json"


import './App.css'

function App() {
          //Get  //Set        //init
  // const [hello, setHello] = useState("Hello Victor")

  const [tasks, setTasks] = useState(jsonTasks);
  const [formInput, setFormInput] = useState("");
 

  const formSubmit = (e) => {
    e.preventDefault()
    let newTask = { id: tasks.length + 1, task: formInput, completed: false }
    setTasks([...tasks, newTask])
      setFormInput("")
  }
  

  return (
    <>
    {/* <div id="greeting"> {hello}</div>
    <button onClick ={()=>setHello("Goodbye Victor")}>Click Me</button> */}
    <form onSubmit={(e) => formSubmit(e)}>
      <input placeholder="enter task"
      value={formInput}
      onChange={(e) => setFormInput(e.target.value)}
      />
     
      <button type="submit">Submit</button>
    </form>
     <ol>
      {tasks.map((task) => {
        return <li key={task.id}>{task.task}</li>
      })}
     </ol>
    </>
  
  );
}

export default App
