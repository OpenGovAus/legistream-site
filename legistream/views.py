from django.shortcuts import render
from . import statuscheck

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

def gen_context():
    live_parls = []
    for parliament in statuscheck.check_statuses():
        if(parliament['stat']):
            dummy = parliament
            live_parls.append(dummy)
    return {
        'dropdown_list': statuscheck.check_statuses(),
        'live_parls': grammarfy(live_parls),
    }

def home(request):
    context = gen_context()
    context['title'] = 'Home'
    return(render(request, 'legistream/homepage.html', context=context))

def act(request):
    from . import act
    context = gen_context()
    context['stream_urls'] = act.act_urls
    context['parl'] = act.parl_title
    context['title'] = 'ACT Parliament'

    return(render(request, 'legistream/stream_page.html', context=context))

def federal(request):
    from . import fed
    context = gen_context()
    context['stream_urls'] = fed.fed_urls
    context['parl'] = fed.parl_title
    context['title'] = 'Federal Parliament'

    return(render(request, 'legistream/stream_page.html', context=context))

def nsw(request):
    from . import nsw
    context = gen_context()
    context['stream_urls'] = nsw.nsw_urls
    context['parl'] = nsw.parl_title
    context['title'] = 'NSW Parliament'

    return(render(request, 'legistream/stream_page.html', context=context))

def nt(request):
    from . import nt
    context = gen_context()
    context['stream_urls'] = nt.nt_urls
    context['parl'] = nt.parl_title
    context['title'] = 'NT Parliament'

    return(render(request, 'legistream/stream_page.html', context=context))

def qld(request):
    from . import qld
    context = gen_context()
    context['stream_urls'] = qld.qld_urls
    context['parl'] = qld.parl_title
    context['title'] = 'QLD Parliament'

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
    context = gen_context()
    context['stream_urls'] = wa.wa_urls
    context['parl'] = wa.parl_title
    context['title'] = 'WA Parliament'

    return(render(request, 'legistream/stream_page.html', context=context))

def demoparl(request):
    context = gen_context()
    context['stream_urls'] = [{'url': 'http://video.parliament.act.gov.au/vod/amlst:ASSEMBLY_13-08-13_3/playlist.m3u8?DVR', 'title': 'nothin', 'safe': 'nothin'}, {'url': 'http://video.parliament.act.gov.au/vod/amlst:ASSEMBLY_20-08-20_1/playlist.m3u8?DVR', 'title': 'Stream 1', 'safe': 'strm1'}, {'url': 'http://video.parliament.act.gov.au/vod/amlst:ASSEMBLY_30-07-20_1/playlist.m3u8?DVR', 'title': 'Stream 2', 'safe': 'strm2'}]
    context['parl'] = 'Not a'
    context['title'] = 'demoparl'
    context['stream_amount'] = len(context['stream_urls'])

    return(render(request, 'legistream/stream_page.html', context=context))

def info(request):
    context = gen_context()
    return(render(request, 'legistream/info.html', context=context))