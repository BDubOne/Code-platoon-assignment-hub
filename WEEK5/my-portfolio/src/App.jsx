import { BrowserRouter, Routes, Route } from 'react-router-dom';
import './App.css'
import About from './components/About';
import Home from './components/Home';
import Portfolio from './components/Portfolio';
import Contact from './components/Contact';
import Navbar from './components/Navbar';

function App() {
  
  return (
    <BrowserRouter>

    <div className="app">
    <Navbar /> 
  </div>
  <Routes>
    <Route path="/" element={<Home />} />
    <Route path="about" element={<About />} />
    <Route path="portfolio" element={<Portfolio />} />
    <Route path="contact" element={<Contact />} />
  </Routes>
  </BrowserRouter>


  )
}



export default App
