import { useState } from 'react'
import './App.css'
import { Outlet } from 'react-router-dom'
import Container from 'react-bootstrap/Container'
import Row from 'react-bootstrap/Row'
import NavBar from './components/Nav.jsx'

function App() {

  return (
   <Container>
    <NavBar />
    <Outlet />
   </Container>
  )
}

export default App
