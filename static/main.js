function changeBackgroundColor() {
    var winOrLoss = document.getElementsByClassName("winloss")
    var color;
    var i;
    for (i = 0; i < winOrLoss.length; i++){
        var res = winOrLoss[i].getAttribute("result")
        if (res == "Win") {
            color = "rgba(1, 238, 238, 0.58)"
        } else if (res == "Loss") {
            color = "rgba(238, 1, 1, 0.58)"
        }
        winOrLoss[i].style.backgroundColor = color
    }
}