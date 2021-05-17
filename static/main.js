function changeBackgroundColor() {
    var winOrLoss = document.getElementsByClassName("winloss");
    var color;
    var i;
    for (i = 0; i < winOrLoss.length; i++){
        var res = winOrLoss[i].getAttribute("result");
        if (res == "Win") {
            color = "rgba(1, 238, 238, 0.58)";
        } else if (res == "Loss") {
            color = "rgba(238, 1, 1, 0.58)";
        }
        winOrLoss[i].style.backgroundColor = color;
    }
}

function changeBackgroundColorLive() {
    var winOrLoss = document.getElementsByClassName("teamColor");
    var color;
    var i;
    for (i = 0; i < winOrLoss.length; i++){
        var res = winOrLoss[i].getAttribute("result");
        if (res == "Blue") {
            color = "rgba(1, 238, 238, 0.58)";
        } else if (res == "Red") {
            color = "rgba(238, 1, 1, 0.58)";
        }
        winOrLoss[i].style.backgroundColor = color;
    }
}

function openTabInfo(evt, tabName) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
      tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
      tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    document.getElementById(tabName).style.display = "block";
    evt.currentTarget.className += " active";
  }