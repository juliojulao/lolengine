function changeBackgroundColor() {
    var winOrLoss = document.getElementsByClassName("winloss");
    var i, color;
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
    var i, color;
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

function highlightSearchedUser(user) {
    var i, participants;
    participants = document.getElementsByClassName("view_summoner")
    console.log(participants)
    for (i = 0; i < participants.length; i++){
        var part = participants[i].getAttribute("participant-ign");
        if (user == part){
            console.log("SUCCESS", user, part)
            participants[i].style.fontWeight = "bold";
        }
        else{
            console.log("FAILED", user, part)
        }
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