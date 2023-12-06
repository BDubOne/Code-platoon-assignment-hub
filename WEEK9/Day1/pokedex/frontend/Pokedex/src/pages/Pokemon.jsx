import Row from "react-bootstrap/Row"
import { useEffect, useState } from 'react';
import axios from 'axios';
import { PokemonItem } from "../components/PokemonItem";

export const Pokemon=()=>{

    const [pokemon, setPokemon] = useState([]);

    const getAllPokemon = async () => {
        let response = await axios
        .get("http://127.0.0.1:8000/api/v1/pokemon/")
        .catch((err) =>{
            console.log(err);
            alert("something went wrong");

        });
        console.log(response.data)
        setPokemon(response.data);
    };
    useEffect(() => {
        getAllPokemon();
        console.log(pokemon)
    }, []);
    
    return (
        <Row style={{padding: "0 10vmin" }}>
            <h1 style={{ textAlign: "center" }}>Pokemon</h1>
            <ul>
                {pokemon.map((poke) => (
                    <PokemonItem key={poke.id} pokemon={poke} />
                    // <PokemonForm key={poke.id} pokemon={poke} />
            
                         
                ))}
            </ul>
        </Row>
             
    );
};