from django.shortcuts import render

def home(request):
    ''' Notes so I don't forget things:
    from . import fed
    from . import act
    from . import wa
    from . import nt
    from . import nsw
    from . import qld

    This alone takes 7 - 13 seconds (with no-cache refresh) and is completely left to the mercy of the
    speed of parliament(s)' servers. 
    Can I get this to run in the background every [2 mins] somehow? If the server doesn't have to slow down
    to return a boolean live value, UX would probably be - for lack of a better term - better...
    Goal: run through each parliament, check if it's live, and return data like this:

    {
        parl: 'parl-title (QLD or something)',
        live: True/False
    }
    '''

    return(render(request, 'legistream/homepage.html'))

def act(request):
    from . import act
    context = {
        'stream_urls': act.act_urls,
        'parl': act.parl_title,
        'title': 'ACT'
    }

    return(render(request, 'legistream/stream_page.html', context=context))

def federal(request):
    from . import fed
    context = {
        'stream_urls': fed.fed_urls,
        'parl': fed.parl_title,
        'title': 'Federal'
    }

    return(render(request, 'legistream/stream_page.html', context=context))

def nsw(request):
    from . import nsw
    context = {
        'stream_urls': nsw.nsw_urls,
        'parl': nsw.parl_title,
        'title': 'NSW'
    }

    return(render(request, 'legistream/stream_page.html', context=context))

def nt(request):
    from . import nt
    context = {
        'stream_urls': nt.nt_urls,
        'parl': nt.parl_title,
        'title': 'NT'
    }

    return(render(request, 'legistream/stream_page.html', context=context))

def qld(request):
    from . import qld
    context = {
        'stream_urls': qld.qld_urls,
        'parl': qld.parl_title,
        'title': 'QLD'
    }

    return(render(request, 'legistream/stream_page.html', context=context))

def sa(request):
    #from . import sa
    #context = {
    #    'stream_urls': sa.sa_urls,
    #    'parl': sa.parl_title,
    #    'title': 'SA'
    #}

    context = {}

    return(render(request, 'legistream/vic_tas.html', context=context))

def tas(request):
    #from . import tas
    #context = {
    #    'stream_urls': tas.tas_urls,
    #    'parl': tas.parl_title,
    #    'title': 'Tasmania'
    #}

    context = {}

    return(render(request, 'legistream/vic_tas.html', context=context))

def vic(request):
    #from . import vic
    #context = {
    #    'stream_urls': vic.vic_urls,
    #    'parl': vic.parl_title,
    #    'title': 'Victoria'
    #}

    context = {}

    return(render(request, 'legistream/vic_tas.html', context=context))

def wa(request):
    from . import wa
    context = {
        'stream_urls': wa.wa_urls,
        'parl': wa.parl_title,
        'title': 'WA'
    }

    return(render(request, 'legistream/stream_page.html', context=context))