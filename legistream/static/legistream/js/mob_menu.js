document.addEventListener('DOMContentLoaded', () =>{
    const btn = document.querySelector('.menucontainer');
    const btn_container = document.querySelector('.menubtncontainer');

    const site_restrict = document.querySelector('.myjobistogetintheway');

    const dropdown_flex = document.querySelector('.dropdown');

    let isOpen = false;

    var closeMenu = () => {
        $('nav').css({
            'opacity': 0.0,
            'visibility': 'hidden'
        });
        btn.classList.remove('menuopen');
        isOpen = false;
        document.getElementsByClassName('menuopencls')[0].remove();
    };

    site_restrict.addEventListener('click', () => {
        if(isOpen)
        {
            closeMenu();
        };
    });

    dropdown_flex.addEventListener('click', () => {
        if(isOpen)
        {
            closeMenu();
        };
    });

    btn_container.addEventListener('click', () => {
        if(!isOpen)
        {
            window.scrollTo(0, 0);
            $('nav').css({
                'opacity': 1.0,
                'visibility': 'visible'
            });
            btn.classList.add('menuopen');
            isOpen = true;

            var styles = `
                body {
                    overflow: hidden;
                }
                .myjobistogetintheway {
                    z-index: 4;
                    opacity: 0.8;
                    visibility: visible;
                }
            `;

            var styleSheet = document.createElement("style");
            styleSheet.innerText = styles;
            styleSheet.classList.add('menuopencls');
            document.head.appendChild(styleSheet);
        } else {
            closeMenu();
        };
    });
});
