import json


from legistream.models import Streams
from .. import module_list


def write_statuses():
    parl_list = []
    for mod in module_list:
        has_live = False
        path = f'/{mod}'
        try:
            exec(f'from legistream_backend.site.{mod} import {mod.upper()}'
                 f'StreamExtractor as StreamExtractor', globals())
            stream_obj = StreamExtractor()
            parl_id = stream_obj.extractor_name
            for stream in stream_obj.streams:
                if stream.is_live:
                    has_live = True
            data_dict = {
                'parl': parl_id,
                'url': path,
                'stat': has_live
            }
            print(f'\nWriting\n{json.dumps(data_dict, indent=2)}')
            parl_list.append(data_dict)
        except Exception as e:
            parl_list.append({
                'parl': parl_id,
                'url': path,
                'stat': False
            })
            print(f'An error ocurred when trying to '
                  f'parse the {mod} module;\n\n{str(e)}')

    if len(Streams.objects.all()) > 1:
        for s in Streams.objects.all()[1:]:
            s.delete()
    elif len(Streams.objects.all()) == 1:
        stream_data = Streams.objects.all()[0]
        stream_data.streams_dict = json.dumps(parl_list)
    else:
        stream_data = Streams(
            streams_dict=json.dumps(parl_list)
        )
    stream_data.save()


def check_statuses():
    try:
        stream_data = json.loads(
            Streams.objects.all()[0].streams_dict)
    except Exception:
        write_statuses()
        stream_data = json.loads(
            Streams.objects.all()[0].streams_dict)
    return stream_data
