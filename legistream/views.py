from hashlib import md5
from django.urls import resolve
from django.shortcuts import render


from .status_checker import statuscheck


def grammarfy(parl_list):
    if(len(parl_list) == 1):
        parl_list.append({'parl': '.', 'url': None})
        return(parl_list)
    try:
        new_list = []
        for parl in parl_list[:-1]:
            new_list.append(parl)
            new_list.append({'parl': ', ', 'url': None})
        new_list.append({'parl': 'and ', 'url': None})
        new_list.append(parl_list[-1])
        return(new_list)
    except Exception:
        return([])


def gen_context():
    live_parls = []
    for parliament in statuscheck.check_statuses():
        if(parliament['stat']):
            live_parls.append(parliament)
    return {
        'dropdown_list': statuscheck.check_statuses(),
        'live_parls': grammarfy(live_parls),
    }


def home(request):
    context = gen_context()
    context['title'] = 'Home'
    return(render(request, 'legistream/homepage.html', context=context))


def watch(request):
    context = gen_context()
    parl_mod = resolve(request.path_info) \
        .url_name.replace('-parliament', '')

    try:
        exec(f'from legistream_backend.site.{parl_mod} import '
             f'{parl_mod.upper()}StreamExtractor as StreamExtr'
             f'actor', globals())

        stream_obj = StreamExtractor()
        streams = stream_obj.streams

        context['stream_urls'] = [
            {
                'url': stream.url,
                'title': stream.title,
                'safe': md5(stream.title.lower()
                            .replace(' ', '-').encode()).hexdigest(),
                'thumb': f'/legistream/img/thumbs/{stream.thumb}'
            } for stream in streams if stream.is_live
        ]
        context['parl'] = stream_obj.extractor_name
        context['title'] = f'{stream_obj.extractor_name} Parliament'
        context['stream_amount'] = len(context['stream_urls'])

        return render(request, 'legistream/stream_page.html', context=context)
    except Exception as e:
        raise Exception(f'\nAn error ocurred when trying to render the'
                        f' {parl_mod.upper} page;\n\n{str(e)}.')
