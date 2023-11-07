
import './App.css'
import { Outlet, Link } from 'react-router-dom'
import { useState, useEffect } from 'react'
import axios from 'axios'

function App() {

  return (
    <>
    <h1>
      Hello
    </h1>
    <nav>
      <ul>
        <li>
          <Link to="/">Home</Link>
        </li>
        <li>
          <Link to ="about/">About</Link>
        </li>
        <li>
          <Link to ="characters/">Characters</Link>
        </li>
      </ul>
    </nav>
    <Outlet />
  
    </>
  )
}

export default App
