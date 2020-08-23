var swapAnimation = lottie.loadAnimation({
    container: document.getElementById("swap-btn"),
    renderer : "svg",
    loop     : false,
    autoplay : false,
    path     : $("#swap-btn").attr("data-url")
});
swapAnimation.setSpeed(4);
swapAnimation.addEventListener("complete", function() {
    swapAnimation.goToAndStop(0);
});

$("#swap-btn").on("click", function() {
    loadNewCard();
    swapAnimation.play();
});

$(document).ready(function() {
    resetTimer();
})


function loadNewCard() {
    resetTimer();
    // TODO
}

var interval;

function resetTimer() {

    var t1 = new Date();
    t1 = t1.getTime();

    clearInterval(interval);
    var cell_count = $(".timer__cell").length;
    for (var i = 1; i <= cell_count; i++) {
        $(".timer__cell:nth-child(" + i + ")").removeClass("empty");
    }
    setTimeout(function(){$(".timer__cell:last-child").addClass("empty");}, 100)
    var i = 2;
    interval = setInterval(function() {
        var cell = $($(".timer__cell")[cell_count - i]);
        if (!cell.length) {
            var t2 = new Date;
            console.log((t2.getTime() - t1) / 1000);
            clearInterval(interval);
            loadNewCard();
        } else {
            cell.addClass("empty");
            i++;
        }
    }, 60 * 1000 / cell_count)
}