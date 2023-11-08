import { useState } from 'react'
import { Outlet } from 'react-router-dom'
import {Header} from "./components/Header"
import Container from 'react-bootstrap/Container'
import Row from 'react-bootstrap/Row'
import Column from 'react-bootstrap/Col'

import './App.css'

function App() {


  return (
    <Container id="app-container">
      <Row>
    <Header /> 
    </Row>
    <Row>
   <Outlet />
   </Row>
    </Container>
  )
}

export default App
