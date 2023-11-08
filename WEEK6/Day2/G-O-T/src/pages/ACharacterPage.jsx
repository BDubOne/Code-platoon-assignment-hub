import { useState, useEffect } from 'react';
import axios from 'axios';
import { useParams } from 'react-router-dom'

const ACharacterPage = () => {
    const [character, setCharacter] = useState(null); // Initialize character as null
    const {id} = useParams()

    const getCharacter = async () => {
        try {
            // Replace '1' with the actual ID of the character you want to fetch
            const response = await axios.get(`https://thronesapi.com/api/v2/Characters/${id}`);
            setCharacter(response.data);
        } catch (error) {
            console.error('Error fetching character:', error);
        }
    };

    useEffect(() => {
        getCharacter();
    }, []);

    return (
        <div>
            <h2>Character</h2>
            {character && (
                <div>
                    <h3>Name: {character.fullName}</h3>
                    <p>Other information about the character goes here...</p>
                </div>
            )}
        </div>
    );
};

export default ACharacterPage;