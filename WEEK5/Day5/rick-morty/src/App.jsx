import { useState, useEffect } from 'react'

import './App.css'
import axios from 'axios';
import Cards from './components/Card';



function App() {
  const [characters, setCharacters] = useState([])
  
  const getCharacters = async() => {
    let response = await axios.get('https://rickandmortyapi.com/api/character')
    setCharacters(response.data.results)
    }

  useEffect(()=>{
    getCharacters()
  },[])



  return (
    <>
    
    <h1>Rick and Morty</h1>
    {characters.map((character, idx) =>(


     
      <Cards 
        key={idx}
        name={character.name} 
        image={character.image} 
        species={character.species} 
        status={character.status}/>
    
    ))}
 
    </>
  )
}

export default App
