let question_type = 'tips'
let communication_type = 'host'

function loadNewCard() {
    $.ajax("/ajax/get-new-card", {
        method: "post",
        dataType: "json",
        data: JSON.stringify({
            previousItemId: $(".card__item").attr("data-id"),
            previousQuestId: $(".card__quest").attr("data-id"),
            question_type: question_type,
            communication_type: communication_type
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

function updateCard() {
    if (nextCard !== undefined) {
        preloader.hide();
        
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
        preloader.show();
        clearInterval(interval);
        needsToUpdate = true;
    }
}