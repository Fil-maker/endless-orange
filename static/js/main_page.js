$(".animation-trigger").on("click", function() {
    $(".menu").addClass("animated");

    if ($(this).attr("id") == "rules-button") {
        $(".rules").fadeIn(500);
    }
});

$("#rules__go-back").on("click", function() {
    $(".menu").removeClass("animated");
    $(".rules").fadeOut(500);
});