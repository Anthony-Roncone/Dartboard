document.getElementById("0").focus();
var id = 0;

class scoreBox{
    constructor(value, multiplyer, updated)
    {
        this.value = value;
        this.multiplyer = multiplyer;
        this.updated = updated;
    }
}

var number = [];
number.push(new scoreBox(0,1,false));
number.push(new scoreBox(0,1,false));
number.push(new scoreBox(0,1,false));
number.push(new scoreBox(0,1,false));
number.push(new scoreBox(0,1,false));
number.push(new scoreBox(0,1,false));

document.addEventListener('keydown', event => {
    
    if(event.shiftKey && event.key == "Enter")
    {
        changeFocus(2);  
    }
    else if(event.ctrlKey && event.key == "Enter")
    {
        changeFocus(3);
    }
    else if(event.altKey && event.key == "Enter")
    {
        clearInputs();
    }
    else if (event.key == 'Enter') 
    {
        changeFocus(1);
    }
});

//moves focus to next input box after score is enterd
function changeFocus(mult)
{
    if(number[id].updated == false)//checks to see if score from input box has already been added to players score
    {
        var num = document.getElementById(id);//getting value from input box
        //adding value from input field to array to store value 
        number[id].value = num.value;
        number[id].multiplyer = mult;
        number[id].updated = true;
        num.value += " *" + mult;
        updateTempScore();
    }
    id = (id + 1) % 6;
    document.getElementById(id).focus();
}

function updateTempScore()
{
    var scores = document.getElementsByName(number[id].value);//gets score fields that correspond to value in input field for both players
    if(scores.length > 0)
    {
        //checks to see wich players score should be updtated 
        var player;
        if(id <= 2)
            player = 0;
        else if(id >= 3)
            player = 1;

        //actually upadating players score
        for(var i=0; i< number[id].multiplyer; i++)
            if(!numberFinished(scores[player].innerHTML))//makes sure no more than 3 x's appare for players score
                scores[player].innerHTML += "X";

        if(checkVictory(player))
        {   
            //makes winner text show under winning player
            var winner = document.getElementsByName("winner");
            winner[player].style.display = 'inline';
            disableInput();
        }
            
    }
}

//turns off input fields
function disableInput()
{
    for(var i=0; i<6; i++)
    {
        document.getElementById(i).disabled = true;
    }
}

function clearInputs()
{
    for(var i=0; i<6; i++)//check all input fields
    {
        if(number[i].updated == false)//updates scores from input fields if not already done
        {
            changeFocus(1);   
        }

        //clears array that holds values from input fields
        number[i].value = 0;
        number[i].multiplyer = 1;
        number[i].updated = false;
    }

    //clears input fields
    document.getElementById("0").value = "";
    document.getElementById("1").value = "";
    document.getElementById("2").value = "";
    document.getElementById("3").value = "";
    document.getElementById("4").value = "";
    document.getElementById("5").value = "";

    //sets focus on first input box
    id = 0;
    document.getElementById(id).focus();
}

/*
function updateScore(player)
{
    var name = document.getElementById(id).value;
    var scores = document.getElementsByName(name);
    for(var i=0; i< number[id].multiplyer; i++)
        if(!numberFinished(scores[player].innerHTML))
            scores[player].innerHTML += "X";
    if(checkVictory(player))
        alert("Player " + (player + 1) + " Wins!");
}
*/

//checks to see if number has been hit three times
function numberFinished(word)
{   
    if(word.length < 3)
        return false;
    return true;
}

//checks to see if passed player has won
function checkVictory(player)
{
    var scores = document.getElementsByClassName("score");//gets array of all score fields for both players
    var win = true;//assumes victory by default
    for(var i = player; i<scores.length && win; i+=2)//checks all scores for player passed to function
    {
        if(!numberFinished(scores[i].innerHTML))//as soon as 1 score field is not finished win becomes false
            win = false;
    }      

    return win;
}

//keeps focus on input box with the current ID
function setFocus()
{
    document.getElementById(id).focus();
}