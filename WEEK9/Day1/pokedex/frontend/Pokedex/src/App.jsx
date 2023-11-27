import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import Container from 'react-bootstrap/Container'
import Row from 'react-bootstrap/Row'
import Navbar from './components/Navbar.jsx'
import { Outlet } from "react-router-dom"

function App() {


  return (
    <Container>
      <Row style={{ textAlign: "center"}}>
        <h1>POKEDEX</h1>
      </Row>
      <Navbar />
      <Outlet />
    </Container>
    
  );
}

export default App
