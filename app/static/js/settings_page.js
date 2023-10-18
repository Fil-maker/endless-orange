// Выбор режима игры
$(".game-mode").on("click", function() {
    $(".game-mode").removeClass("selected");
    $(this).addClass("selected");

    var n = $(".game-mode").index(this);
    $(".settings.active").removeClass("active");
    $(".settings:nth-child(" + (n + 1) + ")").addClass("active");
});

// Управление выбранным (focused) элементом с помощью клавиатуры
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

// Ввод времени раунда
var timeValue = $("#time-value");
var timeInput = $("#time-input");
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

var wheel_timeValue = $("#wheel-time-value");
var wheel_timeInput = $("#wheel-time-input");
wheel_timeInput.on("input", updateWheelTimeValue);

function updateWheelTimeValue() {
    n = wheel_timeInput.val();
    if (n == 1) {
        wheel_timeValue.text(n + " минута");
    } else if (n < 5) {
        wheel_timeValue.text(n + " минуты");
    } else {
        wheel_timeValue.text(n + " минут");
    }
}

// Ввод количества раундов
var roundsValue = $("#rounds-value");
var roundsInput = $("#rounds-input");
roundsInput.on("input", updateRoundsValue)

function updateRoundsValue() {
    n = roundsInput.val();
    roundsValue.text(n);
}

var wheel_roundsValue = $("#wheel-rounds-value");
var wheel_roundsInput = $("#wheel-rounds-input");
wheel_roundsInput.on("input", updateWheelRoundsValue)

function updateWheelRoundsValue() {
    n = wheel_roundsInput.val();
    wheel_roundsValue.text(n);
}

var questionTypeValue = $("#question-type-value");
updateQuestionTypeValue();
var communicationTypeValue = $("#communication-type-value");
updateCommunicationTypeValue();

function updateQuestionTypeValue() {
    var checked = $(".question-types .toggle-switch-radio:checked");
    questionTypeValue.text(checked.attr("data-name"));
    questionTypeValue.attr("data-tooltip", checked.attr("data-fullname"));
}

function updateCommunicationTypeValue() {
    var checked = $(".communication-types .toggle-switch-radio:checked");
    communicationTypeValue.text(checked.attr("data-name"));

}

// Управление переключателями (toggle switches)
$(".toggle-switch-radio").on("change", function() {
    var toggler = $(this).parent().siblings(".toggler");
    toggler.attr("class", "toggler");
    toggler.addClass($(this).attr("data-position"));

    updateQuestionTypeValue();
    updateCommunicationTypeValue();
});

$(".toggle-switch.double").on("click", function() {
    $(this).children("label").children(".toggle-switch-radio:not(:checked)").prop("checked", true).change();
});

// Всплывающие подсказки
$("[data-tooltip]").mousemove(function (eventObject) {

    var data_tooltip = $(this).attr("data-tooltip");
    var tooltip = $("#tooltip");
    tooltip.text(data_tooltip);
    if (window.innerWidth - eventObject.pageX < 300) {
        tooltip.css({
            "top": eventObject.pageY + 5,
            "right": window.innerWidth - eventObject.pageX - 5,
            "left": "unset"
        });
    } else {
        tooltip.css({ 
            "top": eventObject.pageY + 5,
            "left": eventObject.pageX + 5,
            "right": "unset"
        });
    }
    tooltip.fadeIn(200);
}).mouseout(function () {

    $("#tooltip").fadeOut(200, function() {
        $(this).text("")
            .css({
                "top": 0,
                "left": 0,
                "right": "unset"
            });
    });
});

$("#play-button").on("click", function() {
    $("form.active").submit();
})