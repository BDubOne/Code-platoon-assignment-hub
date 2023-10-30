import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
  let guesses = []
  const randomNumber = Math.floor(Math.random() * 50) + 1
  const takeAGuess = (e) => {
    e.preventDefault()
    let guess = Number(document.getElementById("guess").value)
    let output = document.getElementById('output')
    guesses.push(guess)
    if (guess === randomNumber) {
      output.innerHTML = "<h1>You Won!</h1>"

    }
    else if (guess > randomNumber) {
      
      output.innerHTML = "<h1>Too High!</h1>"

    }
    else {
   
      output.innerHTML = "<h1>Too Low!</h1>"

    }

    
  }
  

  return (
    <>
      <h1> Guess the Number!</h1>
      <form onSubmit={(e)=>takeAGuess(e)}>
      <input type='number' id="guess"/>
      <button type="submit">Submit</button>
      </form>
      <p id = "output"></p>
      <ul id="guess-taken"></ul>
      {guesses.map((guess) => (
        <li>(guess)</li>
      ))}
      </>
  )
}

export default App
