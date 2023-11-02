import { useState, useEffect } from 'react'
import axios from 'axios'
import './App.css'
// import wordList from "./assets/data/words.json"


function App() {
  const [word, setWord] = useState('');
  const [displayedWord, setDisplayedWord] = useState('');
  const [guessedLetters, setGuessedLetters] = useState([]);
  const [remainingAttempts, setRemainingAttempts] = useState(6);
  const [guess, setGuess] = useState('');

  useEffect(() => {
    const fetchRandomWord = async () => {
      try {
        const response = await axios.get(
          "https://random-word-api.herokuapp.com/word?lang=en"

        );
        const newWord = response.data[0].toUpperCase();
        setWord(newWord);
        setDisplayedWord(newWord.split('').map(() => '_').join(' '));
      } catch (error) {
        console.error('could not fetch word:', error);
      }
    }
    fetchRandomWord();
  }, []);

  const handleGuess = (letter) => {
    if (!guessedLetters.includes(letter)) {

      const newGuessedLetters = [...guessedLetters, letter];
      setGuessedLetters(newGuessedLetters);

      if (word.includes(letter)) {
        const newDisplayedWord = word.split('')
        .map((char) => (newGuessedLetters.includes(char) ? char : '_'))
        .join('');
        setDisplayedWord(newDisplayedWord);

        if (!newDisplayedWord.includes('_')) {
          alert('Congratulations! You Live to Try Another Word!');
        }
      } else {
        setRemainingAttempts(remainingAttempts - 1);

          if (remainingAttempts === 1) {
            alert("Sorry. You'red dead! You should have seen " + word + " from a mile away!")
          }
        }
      } else {
        alert('You have already guessed this letter!')
      }
    };

    const handleInputChange = (event) => {
      setGuess(event.target.value.toUpperCase());
    };
    const handleSubmit = (event) => {
      event.preventDefault();
      if (guess.length === 1 && /^[A-Z]$/.test(guess)) {
        handleGuess(guess);
        setGuess('');
      } else {
        alert('Please enter a single letter to guess!')
      }
      
    }

  // https://random-word-api.herokuapp.com/word?lang=en

  return (
    <>
     <h1>Hang Man</h1>
     <p> 
      
        Guesses Remaining: {remainingAttempts}
      
      </p>
      <p>
         
        {displayedWord}

      </p>
      <p>

        Guessed Letters: {guessedLetters.join(', ')}

      </p>
      <form onSubmit={handleSubmit}>
        <label>
          Enter a Letter to Guess:
          <input type='text'
          maxLength="1"
          value={guess}
          onChange={handleInputChange}
          />
        </label>
        <button type="submit">Guess!</button>
      </form>
    </>
  )
}

export default App
