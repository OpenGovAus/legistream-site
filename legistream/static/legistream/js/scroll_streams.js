var scrollSlide = (distance) => {
    streams = document.getElementById('streams-padding');
    streams.scrollBy({
        left: distance,
        behavior: "smooth"
    });
};


var displayTitle = (text) => {
    strong = $(`strong[onmouseover="displayTitle('${text}');"]`);
    bakText = strong.text();
    strong.text(text);
    strong.mouseleave(() => {
        strong.text(bakText);
    });
}


document.addEventListener('DOMContentLoaded', () => {
    if($('.stream-container').length < 3) {
        $('#streams-block').css({
            'flexDirection': 'column',
            'alignItems': 'center'
        });
    };
});
