document.getElementById("score").focus();

function updateScore(player)
{
    var name = document.getElementById("score").value;
    var scores = document.getElementsByName(name);
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
    document.getElementById("score").focus();
}