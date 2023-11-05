import { BrowserRouter, Routes, Route } from 'react-router-dom';
import './App.css'
import Layout from './components/Layout';
import About from './components/About';
import Home from './components/Home';
import Portfolio from './components/Portfolio';
import Contact from './components/Contact';
import Gratitude from './components/Gratitude';
import axios from 'axios';

import { useState, useEffect } from 'react'


function App() {

  const [userProfiles, setUserProfiles] = useState([]);


  useEffect(() => {
    
    const gitHubUserNames = [
      'adamcee',
      'blackrebelradio1992',
      'chadeqmartin',
      'andrew-hagstrom',
      'CustomDesignBuildStudios',
      'dekodac',
      'fravila08',
      'PradoJohn',
      'Ickarus75',
      'jminchew97',
      'matthew-peterson-39',
      'Poleron402',
      'seanmac-dev',
      'theQuiltingRiverOtter',
      'zimmermantr',
      'MrGmo'
    ];

    const getGithubProfiles = async() => {
      try {
        const profiles = await Promise.all(gitHubUserNames.map(async username => {
          const response = await axios.get(`https://api.github.com/users/${username}`);
          return response.data;
        }));
        setUserProfiles(profiles);
      } catch (error) {
        console.error('Error fetching profiles', error);
      }
    }

    getGithubProfiles();
  }, []);
  
  return (
  <BrowserRouter>
    <Routes>
      <Route path="/" element={
        <Layout>
          <Home />
        </Layout>
      } />
      <Route path="/about" element={
        <Layout title="About Me" subtitle="In a rapidly evolving digital landscape, I am committed to harnessing the power of technology to enhance human well-being and promote lifelong learning. Drawing from diverse experiences in theology, arts, and holistic healing, I aim to create innovative software solutions that celebrate the intersection of language, mathematics, and art. By leveraging computer science as a universal language, I aspire to build bridges among diverse communities, ensuring that technology enriches the human experience, rather than compromising it.">
          <About />
        </Layout>
      } />
      <Route path="/portfolio" element={
        <Layout title="My Projects" subtitle="deployed through netlify!">
          <Portfolio />
        </Layout>
      } />
      <Route path="/gratitude" element={
        <Layout title="Gratitude" subtitle="I am deeply grateful for the unwavering support of my wife, Anne Bartell, my family, my mentor, Roque Mesa, as well as my instructors, TAs and classmates at Code Platoon who have been so generous with their wisdom, experience, time and talent. 
        Every success I have had is a direct result of the help I have received.">
          <Gratitude userProfiles={userProfiles} />
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
