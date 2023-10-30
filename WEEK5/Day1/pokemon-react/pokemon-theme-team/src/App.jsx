import { useState } from 'react'
import './App.css'
import axios from 'axios'

function App() {

  const [pokePics, setPokePics] = useState([]); //this use-state is able to set an array for urls of pokemon images to be stores
  const [pokeDeets, setPokeDeets] = useState([]);//this use-state is able to set a list of objects containing the details I want to share about the pokemon I display
  const [clickCount, setClickCount] = useState(0);//This use-state operates as a counter with a beginning value of 0, which enables my program to terminate at a set number of clicks
  const [pokeChoice, setPokeChoice] = useState(null); //This use-state is where I store the type to which I want my pokemon to conform after the first one is chosen

 

  const getPokemon = async() => { //asynchronous function operating whenever conditions are met
    if (clickCount >= 6) { //conditions being clicks
      setPokePics([]); //Here I am setting the function so that on the 7th click, we start from the beginning
      setPokeDeets([]);
      setClickCount(0);
      setPokeChoice(null);
      return;
    }

    setClickCount(clickCount + 1); //If the count was not 6, it increases by 1
    
    let randomPokemon; //variable which will either conform to a particular type or not
    if (clickCount === 0) {
      randomPokemon =  Math.floor(Math.random() * 150) + 1;
    }else {
      const typeApi = `https://pokeapi.co/api/v2/type/${pokeChoice}`;
   
     
    try {

      const typeResponse = await axios.get(typeApi);
      const pokemonOfType = typeResponse.data.pokemon;
      randomPokemon = pokemonOfType[Math.floor(Math.random() * pokemonOfType
        .length)]//here generate a random index within an array generated of pokemon conforming to a particular type

        .pokemon //here I go back to the pokemon element so I can get a url belonging to a particular pokemon

        .url //at this point, the array has one member 

        .split('/')//here I split this url with every dash so I can find the index at the end
        .slice(-2,-1)[0]; //here I slice the pokemon ID contained at the end of the array and then grab the only index of the now one-member array

      } catch (error) { //if it doesn't work, I get an error in my log
        console.error('Could not catch this type of pokemon', error);
        return;
      }
    }
    const pokeApi = `https://pokeapi.co/api/v2/pokemon/${randomPokemon}`;//generate first pokemon based on a random number
    try {
      let response = await axios.get(pokeApi);
      let pokeType = response.data.types[0].type.name;//here I get the type..useful for checking the other logic(which may be able to be refactored since it's easy to get a string for type)
      console.log(pokeType);
      
      let abilities = response.data.abilities.map((ability) => ability.ability.name); //abilities of  given pokemon. These will be concatinated in the return
      
      let newPokePics = [...pokePics, response.data.sprites.front_default];//only getting one type of image
      let newPokeDeets = [//format of the details I want to shair
        ...pokeDeets,
        {
          name: response.data.name,
          type: pokeType,
          height: response.data.height,
          abilities: abilities,
        }
      ];
      
      setPokePics(newPokePics);//setting Pics(pushing new pic)
      setPokeDeets(newPokeDeets);//setting Deets(pushing new deets object)

      if (clickCount === 0)
      {
        setPokeChoice(pokeType);//set the given type with the first one
      }
    } catch (error) {
      console.error('Could not catch the pokemon', error);
    }
  };

  const pokePicsToShow = clickCount === 0 ? pokePics : //terniary operator for either 0 or making sure the type is the same as the first one, applied to the image generation
  pokePics.filter((_, idx) => pokeDeets[idx].type === pokeChoice);
  
  const pokeDeetsToShow = clickCount === 0 ? pokeDeets :
  //same thing to make sure it's the same for the detail generation
  pokeDeets.filter((_, idx) => pokeDeets[idx].type === pokeChoice)




 


  return (
    <>
    <h1>Gotta Catch Em All!</h1>
    <button id="poke-catch" onClick={getPokemon}>
      I Choose You!
    </button>
    {pokeChoice && (
    <table> 
      {/* Setting Table so that images show on top and details show below */}

      <tbody>
      <tr id="poke-imgs">
        {/*Map function to apply a new <td> for every image */}
        {pokePicsToShow.map((pokePic, idx) => (
        <td key={idx}>

          <img src={pokePic} alt={pokeChoice} />
          
        </td>
        ))}
      </tr>
      <tr id="poke-data">
           {/*Map function to apply a new <td> for every detail object */}
        {pokeDeetsToShow.map((pokemon, idx) => (
          <td key = {idx}>
            {pokemon.name}
            <br/>
            Type: {pokemon.type}
            <br/>
            Height: {pokemon.height}
            <br/>
            Abilities: {pokemon.abilities.join(', ')}
          </td>
        ))}
      </tr>
      </tbody>
    </table>
    )}
    {clickCount === 6 && <h2>Let's Battle!</h2>}

     
  
    </>
  );
}

export default App
