import { useState, useEffect } from 'react'
import axios from 'axios'

export const PokemonForm = ({pokemon})=> {
    const [name, setName] = useState();
    const [description, setDescription] = useState();
    const [ captured, setCaptured] = useState(pokemon.captured)
    const handleSubmitPokemonForm = (e) => {
        e.preventDefault();
        confirm.log('form submit');

    }
    return (
        <form onSubmit={handleSubmitPokemonForm}>
            <input 
            type="text"
            placeholder={pokemon.name}
            onChange={(e) => setName(e.target.value)}
            />
             <input 
            type="text"
            placeholder={pokemon.description}
            onChange={(e) => setDescription(e.target.value)}
            />
            <label>
                <input 
                type="checkbox" 
                id="caught"
                checked={captured}
                onChange={(e) =>setCaptured(e.target.checked)}
                >                    
                </input>
                Caught
            </label>
            <input type="submit" placeholder="Update Pokemon"/>
        </form>
    )
}
export const PokemonItem = ({pokemon}) => {
    const [nounProjectIcon, setNounProjectIcon] = useState(null)
    const [isLoading, setIsLoading] = useState(true);
    const [isLoadingImage, setIsLoadingImage] = useState(true)
    
    const getIcon = async () => {
        try {
          const response = await axios
          .get(`http://127.0.0.1:8000/api/v1/noun/${pokemon.type}/`);
  
          setNounProjectIcon(response.data.image);
        } catch (err) {
          console.log(err);
          alert("Problems getting poke-icon");
        } finally {
          setIsLoadingImage(false); // Set loading to false whether the request succeeds or fails
        }
      };
    useEffect(()=>{
        getIcon()
        setIsLoading(false);
        console.log(nounProjectIcon)
    }, [])
    

    return (
        <li 
        style={{
            margin: "3vmin",
            display: "flex",
            flexDirection: "column",
        }}
        >
            {isLoading ? (
                <div>Loading...</div>
            ) : (
                <>
            Name: {pokemon.name}
            <br /> {pokemon.level}
            <ul>
                {isLoadingImage ?(
                    <div> loading image...</div>
                ) : (
                <img style={{height:'5vmin', width:'5vmin'}} src=
                {nounProjectIcon} alt=""/>
                )}
                Moves: 
                {pokemon.moves.map((move,
                    idx)=>(
                        <li key={`${pokemon.id}${idx}`}>{move}</li>
                    ))}
                </ul>
                <div>
                    <PokemonForm pokemon={pokemon}/>
                </div>
                
                </>
                )}
                
            </li>
    )
}