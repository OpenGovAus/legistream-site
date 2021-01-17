var player = '';

function playVideo(stream_safe)
{
    var from_backend = `vid-${stream_safe}`;
    player = videojs(from_backend);
    player.play();
}

function close_widget(clicked_thumb)
{
    widget_container = document.getElementById('stream-widget-container')
    widget_container.style.opacity = '0.0'
    widget_container.style.visibility = 'hidden'

    gh_hook = document.getElementById('lower-bar')
    gh_hook.style.transition = 'all 0.2s'
    gh_hook.style.zIndex = '0'

    opengov_container = document.getElementById('opengov-container')
    opengov_container.style.transition = 'all 0.2s'
    opengov_container.style.zIndex = '0'

    parl_dropdown = document.getElementsByClassName('parliament-dropdown')[0]
    parl_dropdown.style.transition = 'all 0.2s'
    parl_dropdown.style.zIndex = '0'

    clicked = document.getElementById(clicked_thumb)
    clicked.style.opacity = '1.0'
    clicked.style.visibility = 'visible'
    player.dispose()
}

function gen_widget(stream_title, stream_url, stream_safe, back_btn_loc)
{
    widget_container = document.getElementById('stream-widget-container')
    widget_container.style.visibility = 'visible'
    widget_container.style.width = '100%'
    widget_container.style.opacity = '1.0'
    widget_container.style.height = '100%'
    widget_container.style.backgroundColor = 'rgba(24, 24, 24, 0.97)'
    widget_container.style.top = '0'

    opengov_container = document.getElementById('opengov-container')
    opengov_container.style.transition = 'all 0.0s'
    opengov_container.style.zIndex = '-1'
    
    parl_dropdown = document.getElementsByClassName('parliament-dropdown')[0]
    parl_dropdown.style.transition = 'all 0.0s'
    parl_dropdown.style.zIndex = '-1'
    
    gh_hook = document.getElementById('lower-bar')
    gh_hook.style.transition = 'all 0.0s'
    gh_hook.style.zIndex = '-1'

    clicked = document.getElementById(stream_safe)
    clicked.style.opacity = '0.0'
    clicked.style.visibility = 'hidden'

    widget_container.innerHTML = `<style>video {position: absolute; bottom: 50pt;} #stream-text {padding: 30px; font-size: 55pt; font-family: gilroy;} #back-btn {right: 40px; top: 52px; position: absolute;} #back-btn-img {height: 18pt; padding-right: 5pt;} #back-btn:hover {color: rgb(68, 219, 78); cursor: pointer;} #back-btn:hover #back-btn-img {padding-right: 10pt;} #vid-${stream_safe} {margin-top: 35pt;}</style><h1 id="stream-text">${stream_title.toUpperCase()}</h1><button id="back-btn" onclick="close_widget('${stream_safe}')"><img id="back-btn-img" src="${back_btn_loc}">Back</button><div id="stream-video-container"></div>`
    document.getElementById('stream-video-container').innerHTML = `<video id="vid-${stream_safe}" class="video-js vjs-default-skin" width="800" height="450" controls><source src="${stream_url}" type="application/x-mpegURL"></video>`
    playVideo(stream_safe)
}