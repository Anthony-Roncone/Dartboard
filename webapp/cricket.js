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

function changeFocus(mult)
{
    //console.warn("changeFocus");
    if(number[id].updated == false)
    {
        var num = document.getElementById(id); 
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
    var scores = document.getElementsByName(number[id].value);
    if(scores.length > 0)
    {
        var player;
        if(id <= 2)
            player = 0;
        else if(id >= 3)
            player = 1;

        for(var i=0; i< number[id].multiplyer; i++)
            if(!numberFinished(scores[player].innerHTML))
                scores[player].innerHTML += "X";

        if(checkVictory(player))
        {   
            var winner = document.getElementsByName("winner");
            winner[player].style.display = 'inline';
            disableInput();
            //alert("Player " + (player + 1) + " Wins!");
        }
            
    }
}

function disableInput()
{
    for(var i=0; i<6; i++)
    {
        document.getElementById(i).disabled = true;
    }
}

function clearInputs()
{
    //console.warn("clearInputs");
    document.getElementById("0").value = "";
    document.getElementById("1").value = "";
    document.getElementById("2").value = "";
    document.getElementById("3").value = "";
    document.getElementById("4").value = "";
    document.getElementById("5").value = "";

    for(var i=0; i<6; i++)
    {
        number[i].value = 0;
        number[i].multiplyer = 1;
        number[i].updated = false;
    }

    id = 0;
    document.getElementById(id).focus();
}

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

function numberFinished(word)
{   
    if(word.length < 3)
        return false;
    return true;
}

function checkVictory(player)
{
    var scores = document.getElementsByClassName("score");
    var win = true;
    for(var i = player; i<scores.length && win; i+=2)
    {
        if(!numberFinished(scores[i].innerHTML))
            win = false;
    }      

    return win;
}

function setFocus()
{
    document.getElementById(id).focus();
}