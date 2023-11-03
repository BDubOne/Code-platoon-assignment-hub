import { useState } from 'react'
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import './App.css'


function App() {
  const [show, setShow] = useState(false);

  return (
    <>
    <Container>
      <Row className="a-row">Header</Row>
      <Row className="a-row">
        <Col xs={6}>Left</Col>
        <Col>News feed
        </Col>
        <Col> Right</Col>
      </Row>
      <Row className="a-row">Footer</Row>
    </Container>
{/*     
    <div id="bg-orange-500">
    <p className={show ? "bg-green-200" : "bg-red-200"}>Going to the store is more than a chore. We can remember who we are by looking at what we've done.</p>
    <button 
    className=" text-blue-500 bg-blue-200 border-blue-500 hover:bg-green-500 px-5 py-1 ml-10 border-2"
    onClick={()=> setShow(!show)}>Click</button>
    {/* <p className='text-purple-500 text-bg bg-gray-300'>Hello Victor</p>
    <div className=" m-10 mt-20 border-2">
      I'm a box
  </div>*/}
{/*     
     <div className="w-full h-full flex justify-evenly items-center">
      <p>Hello Victor</p>
      <br/>
      <p>Goodbye Victor</p>
    </div> 
    </div> */} 
    
    </>
  );
}

export default App
