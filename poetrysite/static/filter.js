function poemFilter() {
    
    var input, filter, cards, cardContainer, span, title, maxHidden;
    input = document.getElementById("filter");
    filter = input.value.toUpperCase();
    cardContainer = document.getElementById("items");
    cards = cardContainer.getElementsByClassName("card");

    var numHidden = maxHidden = cards.length;

    for (i = 0; i < cards.length; i++) {

        title = cards[i].querySelector(".card-body span.card-title");

        if (title != null && title.innerText.toUpperCase().indexOf(filter) > -1) {
            numHidden -= 1;
            cards[i].style.display = "";
        } else {
            cards[i].style.display = "none";
        }
    }
    footer = document.getElementsByTagName('footer');
    footer = footer[0];
    console.log(numHidden);
    if (numHidden == maxHidden-2)
    {
        footer.style.marginTop = "8vh";
    }
    else if (numHidden == maxHidden-1)
    {
        footer.style.marginTop = "27.1vh";
    }
    else if (numHidden == maxHidden)
    {
        footer.style.marginTop = "46.3vh";
    }
    else
    {
        footer.style.marginTop = "1vh";
    }
}
           
