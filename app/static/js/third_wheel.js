function loadNewCard() {
    var ids = [];
    $(".card__item").each(function() {
        ids.push($(this).attr("data-id"));
    });

    $.ajax("/ajax/get-n-items", {
        method: "post",
        dataType: "json",
        data: JSON.stringify({
            cardsIDs: ids,
            countCards: $(".card").attr("data-count")
        }),
        contentType: "application/json; charset=utf-8",
        success: function(data) {
            nextCard = data;
            if (needsToUpdate) {
                updateCard();
            } else {
                for (var i = 0; i < data.items.length; i++) {
                    var img = new Image();
                    img.src = data.items[i].filename;
                }
            }
        }
    });
}

function updateCard() {
    if (nextCard !== undefined) {
        preloader.hide();

        for (var i = 0; i < nextCard.items.length; i++) {
            $($(".card__item")[i]).children(".card__img").attr("src", nextCard.items[i].filename);
            $($(".card__item")[i]).attr("data-id", nextCard.items[i].id);
            $($(".card__item")[i]).children(".card__item-name").text(nextCard.items[i].name);
        }
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