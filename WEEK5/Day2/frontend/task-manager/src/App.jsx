import { useState, useEffect } from 'react'

import Task from "./Task.jsx"

import jsonTasks from "../tasks.json"


import './App.css'

function App() {
          //Get  //Set        //init
  // const [hello, setHello] = useState("Hello Victor")

  const [tasks, setTasks] = useState(jsonTasks);
  const [formInput, setFormInput] = useState("");

  // const [show, setShow] = useState(false)
 

  const formSubmit = (e) => {
    e.preventDefault()
    let newTask = { id: tasks.length + 1, task: formInput, completed: false }
    setTasks([...tasks, newTask])
      setFormInput("")
  }
  // useEffect(()=>{
  //   if (show) {
  //     alert("hello")
  //   }
  //   else{
  //     alert("goodbye")
  //   }
  // }, [show])
  


  return (
    <>
   
    <form onSubmit={(e) => formSubmit(e)}>
      <input placeholder="enter task"
      value={formInput}
      onChange={(e) => setFormInput(e.target.value)}
      />
     
      <button type="submit">Submit</button>
    </form>
     <ol>
      {/* {tasks.map((task) => {
      Task */}
     </ol>
    </>
  
  );
}

export default App
