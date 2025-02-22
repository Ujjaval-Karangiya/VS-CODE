let userScore = 0;
let compScore = 0;

const choices = document.querySelectorAll(".choice");
let msg = document.querySelector("#msg");

let userScorePara = document.querySelector("#user-score");
let compScorePara = document.querySelector("#comp-score");

const genCompChoice = () => {
  let options = ["rock", "paper", "scissors"];
  let randomIdx = Math.floor(Math.random() * 3);
  return options[randomIdx];
};

const drawGame = () => {
  msg.innerText = "Game draw. play again"
  msg.style.backgroundColor = "#081b31";
};

let showWinner = (userWin, userChoice, compChoice) => {
  if(userWin){
    userScore++;
    userScorePara.innerText = userScore;
    msg.innerText = `you win! your ${userChoice} beats ${compChoice}`;
    msg.style.backgroundColor = "green";
  }
  else{
    compScore++;
    compScorePara.innerText = compScore;
    msg.innerText = `you lose. ${compChoice} beats your ${userChoice}`
    msg.style.backgroundColor = "red";
  }
}

const playGame = (userChoice) => {

  const compChoice = genCompChoice();

  if(userChoice === compChoice){
    drawGame();
  }
  else{
    let userWin = true;
    if(userChoice === "rock"){
      userWin = compChoice === "paper" ? false : true; 
    }
    else if(userChoice === "paper"){
      userWin = compChoice === "scissors" ? true : false;
    }
    else{
      userWin = compChoice === "rock" ? false : true;
    }
    showWinner(userWin, userChoice, compChoice);
  }
};

choices.forEach((choice) => {
  choice.addEventListener("click", () => {
    const userChoice = choice.getAttribute("id");
    playGame(userChoice);
  });
});