from django.shortcuts import render
from . import statuscheck

def home(request):
    def grammarfy(parl_list):
        if(len(parl_list) == 1):
            parl_list[0]['parl'] = '%s.' % (parl_list[0]['parl'])
            return(parl_list)
        try:
            for parl in parl_list[:-1]:
                parl['parl'] = '%s, ' % (parl['parl'])
            parl_list[-1]['parl'] = 'and %s.' % (parl_list[-1]['parl'])
            return(parl_list)
        except:
            return([])

    live_parls = []
    for parliament in statuscheck.check_statuses():
        if(parliament['stat']):
            live_parls.append(parliament)

    context = {
        'live_parls': grammarfy(live_parls)
    }

    return(render(request, 'legistream/homepage.html', context=context))

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