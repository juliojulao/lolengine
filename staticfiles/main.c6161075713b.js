function changeBackgroundColor(val) {
    var winOrLoss = document.getElementsByClassName("winloss");
    var color;
    if (val == "Win") {
        color = "blue";
    } else if (val == "Loss") {
        color = "red";
    }
    winOrLoss.style.color = color;
}

