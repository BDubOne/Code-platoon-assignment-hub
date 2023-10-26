
let randomNum = Math.floor(Math.random() * 101)
let guessHx = []
let resultBox = document.getElementById('result')
let guessbox = document.getElementById('guess-hx')


console.log(randomNum)

function checkGuess(){
    let guessInput = document.getElementById('input-box');
    let guess = guessInput.value * 1; 
    guessHx.push(guess);
    guessbox.innerText = guessHx;
    if (guess === randomNum){
        resultBox.innerText = "Correct!";
    } else if (guess > randomNum){
        resultBox.innerText = "Too high!";
    } else {
        resultBox.innerText = "Too Low!";
    }
    guessInput.value = '';

}