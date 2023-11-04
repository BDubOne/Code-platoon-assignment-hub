import { BrowserRouter, Router, Routes, Route } from 'react-router-dom';
import './App.css'
import Layout from './components/Layout';
import About from './components/About';
import Home from './components/Home';
import Portfolio from './components/Portfolio';
import Contact from './components/Contact';
import Gratitude from './components/Gratitude';
import Navbars from './components/Navbar';

function App() {

  //usestates
  //useeffect for each api I pull from
  //pass down properties to whatever component utilizes the api

  
  return (
  <BrowserRouter>
    <Routes>
      <Route path="/" element={
        <Layout>
          <Home />
        </Layout>
      } />
      <Route path="/about" element={
        <Layout>
          <About />
        </Layout>
      } />
      <Route path="/portfolio" element={
        <Layout>
          <Portfolio />
        </Layout>
      } />
      <Route path="/gratitude" element={
        <Layout>
          <Gratitude />
        </Layout>
      } />
      <Route path="/contact" element={
        <Layout>
          <Contact />
        </Layout>
      } />
    </Routes>
  </BrowserRouter>


  )
}



export default App
