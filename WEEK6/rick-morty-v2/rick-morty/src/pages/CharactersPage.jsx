import CharacterCard from '../components/CharacterCard'
import axios from 'axios'
import { useState, useEffect } from 'react'



const CharactersPage = () => {
    const [characters, setCharacters] = useState([]);
    const [isLoading, setIsLoading] = useState(true);

   useEffect(() => {
    const getCharacters = async () => {
        try {
            const response = await axios.get('https://rickandmortyapi.com/api/character');
            const totalPages = response.data.info.pages;
            const allCharacters = [];
            for (let page=1; page <= totalPages; page++) {
                const pageResponse = await axios.get(`https://rickandmortyapi.com/api/character?page=${page}`);
                allCharacters.push(...pageResponse.data.results);
            }
            setCharacters(allCharacters);
            setIsLoading(false);
        } catch (error) {
            console.error('Error fetching characters', error)
            setIsLoading(false);
        }
    };

    getCharacters();
   }, [])


    return (
        <div>
        {isLoading ? (
            <p>Loading...</p>
        ) : (
      
        <>
        <h1>
            Characters
        </h1>
        <div className="row">
        {characters.map((character, idx) =>(
        <div key={idx} className="col-md-4 mb-4">
        <CharacterCard
        key={idx}
        name={character.name}
        image={character.image}
        species={character.species}
        />
        </div>
        ))}
        </div>
        </>
        )}
        </div>
    )
}

export default CharactersPage