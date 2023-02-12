document.getElementById("0").focus();
var id = 0;
var score1 = document.getElementById("score1");
var score2 = document.getElementById("score2");
var tScore1 = score1.innerHTML;
var tScore2 = score2.innerHTML;

class scoreBox{
    constructor(value, updated)
    {
        this.value = value;
        this.updated = updated;
    }
}

var number = [];
number.push(new scoreBox(0,false));
number.push(new scoreBox(0,false));
number.push(new scoreBox(0,false));
number.push(new scoreBox(0,false));
number.push(new scoreBox(0,false));
number.push(new scoreBox(0,false));

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
        updateScore();
    }
    else if (event.key == 'Enter') 
    {
        changeFocus(1);
    }
    else if (event.key == "F1")
    {
        event.preventDefault()
        updateInput(0,"zero");
    }
    else if (event.key == "F2")
    {
        event.preventDefault()
        updateInput(1,"zero");
    }
    else if (event.key == "F3")
    {
        event.preventDefault()
        updateInput(2,"zero");
    }
    else if (event.key == "F5")
    {
        event.preventDefault()
        updateInput(3,"zero");
    }
    else if (event.key == "F6")
    {
        event.preventDefault()
        updateInput(4,"zero");
    }
    else if (event.key == "F7")
    {
        event.preventDefault()
        updateInput(5,"zero");
    }
    else if (event.key == "F8")
    {
        event.preventDefault()
        location.reload();
    }
    else if (event.altKey && event.key == "1")
    {
        event.preventDefault()
        updateInput(0,"change");
    }
    else if (event.altKey && event.key == "2")
    {
        event.preventDefault()
        updateInput(1,"change");
    }
    else if (event.altKey && event.key == "3")
    {
        event.preventDefault()
        updateInput(2,"change");
    }
    else if (event.altKey && event.key == "5")
    {
        event.preventDefault()
        updateInput(3,"change");
    }
    else if (event.altKey && event.key == "6")
    {
        event.preventDefault()
        updateInput(4,"change");
    }
    else if (event.altKey && event.key == "7")
    {
        event.preventDefault()
        updateInput(5,"change");
    }

  });

function veryifyNumber(index)
{
    if(number[index].updated == false)
    {
        var num = document.getElementById(index);
        if(num.value == "" || isNaN(parseFloat(num.value)))
            num.value=0;

        number[index].updated = true;
        number[index].value = num.value;
    }
}

function changeFocus(mult)
{
    //console.warn("changeFocus");
    if(number[id].updated == false)
    {
        var num = document.getElementById(id);
        if(num.value == "" || isNaN(parseFloat(num.value)))
            num.value=0;
        else
            num.value = num.value *= mult;
        //console.log("Value in box " + (id+1) + ": " + num.value)

        number[id].updated = true;
        number[id].value = num.value;
        updateTempScore(mult);
    }
    id = (id + 1) % 6;
    document.getElementById(id).focus();
}

function updateScore()
{
    //console.warn("updateScore");
    //console.log(parseFloat(score1.innerHTML) + 5);
    for(var i = 0; i<6; i++)
    {
        if(number[i].updated == false)
        {
            veryifyNumber(i);
        }
    }
    var num1 = parseFloat(number[0].value) + parseFloat(number[1].value) + parseFloat(number[2].value);
    var num2 = parseFloat(number[3].value) + parseFloat(number[4].value) + parseFloat(number[5].value);
    //console.log("Player 1 round score: " + num1);
    //console.log("Player 2 round score: " + num2);

    score1.innerHTML = (parseFloat(tScore1) - num1).toString();
    score2.innerHTML = (parseFloat(tScore2) - num2).toString();
    tScore1 = score1.innerHTML;
    tScore2 = score2.innerHTML;

    clearInputs();

    id = 0;
    document.getElementById(id).focus();

    //console.log(number);
}

function updateTempScore(mult)
{
    //console.warn("updateTempScore");
    var temp;
    if(id == 0 || id == 1 || id == 2)
    {
        temp = parseFloat(score1.innerHTML) - parseFloat(number[id].value)
        //console.log("Score after temp update: " + temp);
        
        if(temp < 0)
        {
            //console.log("temp score below 0 player 1");
            document.getElementById("0").value = "";
            document.getElementById("1").value = "";
            document.getElementById("2").value = "";
            clearArray("one");
            id = 2;
            //document.getElementById(id).focus();
            score1.innerHTML = "Bust";
        }
        else if(temp == 0)
        {
            if(mult == 2)
            {
                disableInput();
                score1.innerHTML = "Winner!"
            }
            else
            {
                document.getElementById("0").value = "";
                document.getElementById("1").value = "";
                document.getElementById("2").value = "";
                clearArray("one");
                id = 2;
                //document.getElementById(id).focus();
                score1.innerHTML = "Bust";
            }
        }
        else
        {
            score1.innerHTML = temp.toString();
        }

        //score1.innerHTML = (parseFloat(score1.innerHTML) - parseFloat(number[id].value)).toString();
    }
    else if(id == 3 || id == 4 || id == 5)
    {
        temp = parseFloat(score2.innerHTML) - parseFloat(number[id].value)
        
        if(temp < 0)
        {

            document.getElementById("3").value = "";
            document.getElementById("4").value = "";
            document.getElementById("5").value = "";
            clearArray("two");
            id = 5;
            //document.getElementById(id).focus();
            score2.innerHTML = "Bust";
        }
        else if(temp == 0)
        {
            if(mult == 2)
            {
                disableInput();
                score2.innerHTML = "Winner!"
            }
            else
            {
                document.getElementById("3").value = "";
                document.getElementById("4").value = "";
                document.getElementById("5").value = "";
                clearArray("two");
                id = 5;
                //document.getElementById(id).focus();
                score2.innerHTML = "Bust";
            }
        }
        else
        {
            score2.innerHTML = temp.toString();
        }
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

    clearArray("both");
}

function clearArray(type)
{
    if(type == "one")
    {
        for(var i=0; i<3; i++)
        {
            number[i].value = 0;
            number[i].updated = false;
        }
    }
    else if(type == "two")
    {
        for(var i=3; i<6; i++)
        {
            number[i].value = 0;
            number[i].updated = false;
        }
    }

    for(var i=0; i<6; i++)
    {
        number[i].value = 0;
        number[i].updated = false;
    }
}

function disableInput()
{
    for(var i=0; i<6; i++)
    {
        document.getElementById(i).disabled = true;
    }
}

function updateInput(index, type)
{
    var box = document.getElementById(index);
    var score;
    if(index == 0 || index == 1 || index == 2)
    {
        score = document.getElementById("score1");
    }
    else if(index == 3 || index == 4 || index == 5)
    {
        score = document.getElementById("score2");
    }

    score.innerHTML = parseFloat(score.innerHTML) + parseFloat(box.value);

    if(type == "zero")
    {
        //console.log("zero out score field");
        //score.innerHTML = parseFloat(score.innerHTML) + parseFloat(box.value);
        box.value = 0;
        number[index].value = 0;
    }
    else if(type == "change")
    {
        //console.log("change score field");
        //score.innerHTML = parseFloat(score.innerHTML) + parseFloat(box.value);
        box.value = "";
        id = index;
        setFocus();
        number[id].updated = false;
    }
}

function setFocus()
{
    document.getElementById(id).focus();
}

function test()
{   
    if(isNaN(parseFloat(document.getElementById("0").value)))
    {
        console.log("0");
    }
    else
    {
        console.log(document.getElementById("0").value)
    }
    
}