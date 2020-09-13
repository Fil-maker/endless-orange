$(".game-mode").on("click", function() {
    $(".game-mode").removeClass("selected");
    $(this).addClass("selected");

    var n = $(".game-mode").index(this);
    $(".settings.active").removeClass("active");
    $(".settings:nth-child(" + (n + 1) + ")").addClass("active");
});

$(document).on("keydown", function(e) {
    if (e.which == 13) { // enter
        $(":focus").click();
    } else if (e.which == 37) { // left
        var radio = $(".toggle-switch.triple:focus .toggler-label .toggle-switch-radio").slice(0, 2);
        if (radio.length && !radio[0].checked) {
            radio = radio.not(":checked");
            radio = $(radio[radio.length - 1]);
            radio.prop("checked", true).change();
        }
    } else if (e.which == 39) { // right
        var radio = $(".toggle-switch.triple:focus .toggler-label .toggle-switch-radio").slice(1);
        if (radio.length && !radio[radio.length - 1].checked) {
            radio = radio.not(":checked");
            radio = $(radio[0]);
            radio.prop("checked", true).change();
        }
    }
});


var timeValue = $("#time-value");
var timeInput = $("#time-input");
updateTimeValue();
timeInput.on("input", updateTimeValue);

function updateTimeValue() {
    n = timeInput.val();
    if (n == 1) {
        timeValue.text(n + " минута");
    } else if (n < 5) {
        timeValue.text(n + " минуты");
    } else {
        timeValue.text(n + " минут");
    }
}

var roundsValue = $("#rounds-value");
var roundsInput = $("#rounds-input");
updateRoundsValue();
roundsInput.on("input", updateRoundsValue)

function updateRoundsValue() {
    n = roundsInput.val();
    roundsValue.text(n);
}

$(".toggle-switch-radio").on("change", function() {
    var toggler = $(this).parent().siblings(".toggler");
    toggler.attr("class", "toggler");
    toggler.addClass($(this).attr("data-position"));
});

$(".toggle-switch.double").on("click", function() {
    $(this).children("label").children(".toggle-switch-radio:not(:checked)").prop("checked", true).change();
})