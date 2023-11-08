import { useState, useEffect } from 'react'
import axios from 'axios';
import CharCard from '../components/CharCard'


const AllCharactersPage = () => {
    const [characters, setCharacters] = useState([])

    const getCharacters = async () => {
        try {
            let response = await axios.get('https://thronesapi.com/api/v2/Characters')
            setCharacters(response.data)
        } catch (error) {
            console.error('Error fetching characters:', error)
        }
    }

    useEffect(() => {
        getCharacters();
    }, [])

    return (
        <>
            <h2>All Characters</h2>
            {characters.map((char, idx) => (
                <CharCard key={idx} id={char.id} name={char.fullName} image={char.imageUrl} />
            ))}
        </>
    )
}

export default AllCharactersPage