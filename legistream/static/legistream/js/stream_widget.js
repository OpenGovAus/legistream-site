var player = '';


var playVideo = (stream_safe) => {
    var from_backend = `vid-${stream_safe}`;
    player = videojs(from_backend);
    player.play();
};


var close_widget = (clicked_thumb) => {
    styleDict = {
        'transition': 'all 0.2s',
        'zIndex': '0'
    };
    $('#stream-widget-container').css({
        'opacity': '0.0',
        'visibility': 'hidden'
    });
    $('.dropdown').first().css(styleDict)
    $('#lower-bar').css(styleDict);
    $('#opengov-container').css(styleDict);
    $('.parliament-dropdown').first().css(styleDict);
    $(`#${clicked_thumb}`).css({
        'opacity': '1.0',
        'visibility': 'visible'
    });
    player.dispose();
};


var gen_widget = (stream_title, stream_url, stream_safe, back_btn_loc) => {
    styleDict = {
        'transition': 'all 0.0s',
        'zIndex': '-1'
    };
    $('#opengov-container').css(styleDict);
    $('.parliament-dropdown').first().css(styleDict);
    $('.dropdown').first().css(styleDict);
    $('#lower-bar').css(styleDict);
    $(`#${stream_safe}`).css({
        'opacity': '0.0',
        'visibility': 'hidden'
    });
    $('#stream-widget-container').css({
        'visibility': 'visible',
        'width': '100%',
        'opacity': '1.0',
        'height': '100%',
        'backgroundColor': 'rgba(24, 24, 24, 0.97)',
        'top': '0'
    }).html(
        `<style>
            video {
                position: absolute;
                bottom: 50pt;
            }
            #stream-text {
                padding: 30px;
                font-size: 40px;
                font-family:gilroy;
                width: 80%;
            }
            #back-btn {
                right: 40px;
                top: 52px;
                position: absolute;
            }
            #back-btn-img {
                height: 11pt;
                padding-right: 5pt;
            }
            #back-btn:hover {
                color: rgb(68, 219, 78);
                cursor: pointer;
            }
            #back-btn:hover #back-btn-img {
                padding-right: 10pt;
            }
            #vid-${stream_safe} {
                margin-top: 35pt;
            }
        </style>
        <h1 id="stream-text">${stream_title.toUpperCase()}</h1>
        <button id="back-btn" onclick="close_widget('${stream_safe}')">
            <img id="back-btn-img" src="${back_btn_loc}">
            Back
        </button>
        <div id="stream-video-container"></div>`
    );
    $('#stream-video-container').html(
        `<video id="vid-${stream_safe}" class="video-js vjs-default-skin" width="800" height="450" controls>
            <source src="${stream_url.replace('http://', 'https://')}" type="application/x-mpegURL">
        </video>`
    );
    playVideo(stream_safe);
};
