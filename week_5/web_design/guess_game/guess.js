const randomNumber =Math.floor(Math.random()*100)+1;
console.log(randomNumber)
let attempt = 0;
function checkGuess(){
    const guess=parseint(document.getElementById("guessfield").value)
    attempt++;
    if(isNaN(guess)||guess<1||guess>100){
        setMessage("please enter a valid number between 1 and 100")
        return;
    }
    if (guess ===randomNumber){
            setMessage("Congratulations!You have guessed correctly")
            document.getElementById("guessfield").disabled=true;
    }else if (guess<randomNumber){
            setMessage("Too low try again")
    }else{
            setMessage("Too high guess again")
    }
        
}
function setMessage(message){
    document.getElementById("message").textContent=message
}