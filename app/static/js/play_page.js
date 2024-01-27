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

var pauseAnimation = lottie.loadAnimation({
    container: document.getElementById("pause-btn"),
    renderer : "svg",
    loop     : false,
    autoplay : false,
    path     : $("#pause-btn").attr("data-url")
});
pauseAnimation.setSpeed(4);
//pauseAnimation.addEventListener("complete", function() {
////    pauseAnimation.playSegments([0, 39]);
////    pauseAnimation.goToAndStop(39);
//});

$("#pause-btn").on("click", function() {
    if (is_paused){
        pauseAnimation.playSegments([44, 8], true);
    } else {
        pauseAnimation.playSegments([8, 44], true);
    }
    is_paused = !is_paused;
//    pauseAnimation.play();
});


resize_timer_line();

$("#swap-btn").on("click", function() {
    updateCard();
    swapAnimation.play();
});

$(window).on("load", function() {
//    $("#pause-btn").click();
    resetTimer();
    loadNewCard();
})

var nextCard;
var needsToUpdate = false;

var preloader = $(".preloader");

var interval;
var length;
var is_paused = false;

function set_length(l){
    length = l;
}

function resetTimer() {
    clearInterval(interval);
    var cell_count = $(".timer__cell").length;
    for (var i = 1; i <= cell_count; i++) {
        $(".timer__cell:nth-child(" + i + ")").removeClass("empty");
    }
    if (length != 6){
//    setTimeout(function(){if (!is_paused)$(".timer__cell:last-child").addClass("empty");}, 100)
    var i = 1;
    interval = setInterval(function() {
        var cell = $($(".timer__cell")[cell_count - i]);
        if (!cell.length) {
            clearInterval(interval);
            updateCard();
        } else {
            if (!is_paused){
                cell.addClass("empty");
                i++;
            }
        }
    }, length * 60 * 1000 / cell_count)
    }
}

$(window).on("resize", resize_timer_line);

function resize_timer_line() {
    if (window.innerWidth <= 500) {
        $(".timer__cell:nth-child(even)").addClass("disabled");
        $(".timer__cell:nth-child(odd)").addClass("extended");
    } else {
        $(".timer__cell:nth-child(even)").removeClass("disabled");
        $(".timer__cell:nth-child(odd)").removeClass("extended");
    }
}