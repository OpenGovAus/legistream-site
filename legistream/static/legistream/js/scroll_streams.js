var scrollSlide = (distance) => {
    streams = document.getElementById('streams-padding');
    streams.scrollBy({
        left: distance,
        behavior: "smooth"
    });
};

document.addEventListener('DOMContentLoaded', () => {
    if($('.stream-container').length < 3) {
        $('#streams-block').css({
            'flexDirection': 'column',
            'alignItems': 'center'
        })
    }
})
