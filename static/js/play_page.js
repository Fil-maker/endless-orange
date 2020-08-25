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

resize_timer_line();

$("#swap-btn").on("click", function() {
    updateCard();
    swapAnimation.play();
});

$(window).on("load", function() {
    resetTimer();
    loadNewCard();
})

var nextCard;
var needsToUpdate = false;

function loadNewCard() {
    $.ajax("/ajax/get-new-card", {
        method: "post",
        dataType: "json",
        data: JSON.stringify({
            previousItemId: $(".card__item").attr("data-id"),
            previousQuestId: $(".card__quest").attr("data-id")
        }),
        contentType: "application/json; charset=utf-8",
        success: function(data) {
            nextCard = data;
            if (needsToUpdate) {
                updateCard();
            } else {
                var img = new Image();
                img.src = data.item.filename;
            }
        }
    });
}

var preloader = $(".preloader");

function updateCard() {
    console.log(nextCard);
    if (nextCard !== undefined) {
        preloader.hide()
        $(".card__img").attr("src", nextCard.item.filename);
        $(".card__item").attr("data-id", nextCard.item.id);
        $(".card__item-name").text(nextCard.item.name);
        $(".card__quest").attr("data-id", nextCard.quest.id);
        $(".card__quest").text(nextCard.quest.quest);
        nextCard = undefined;
        needsToUpdate = false;
        resetTimer();
        loadNewCard();
    } else {
        preloader.show()
        needsToUpdate = true;
    }
}

var interval;

function resetTimer() {
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
            clearInterval(interval);
            updateCard();
        } else {
            cell.addClass("empty");
            i++;
        }
    }, 60 * 1000 / cell_count)
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