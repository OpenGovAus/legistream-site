import os
import json
import time
from time import sleep

filepath = os.path.dirname(os.path.realpath(__file__)) + '/statuses/stream_stats.json'
PARL_ID = 'parl'
STREAM_STAT = 'stat'
URL = 'url'

def __act_stream(stream_object):
    data_dict = {PARL_ID: 'ACT'}
    data_dict[URL] = '/act'
    data_dict['radius'] = '10px 10px 0px 0px'
    if(stream_object.lower_is_live):
        data_dict[STREAM_STAT] = True
        
    else:
        data_dict[STREAM_STAT] = False
    return data_dict

def __nt_stream(stream_object):
    data_dict = {PARL_ID: 'NT'}
    data_dict[URL] = '/nt'
    if(stream_object.lower_is_live):
        data_dict[STREAM_STAT] = True
    else:
        data_dict[STREAM_STAT] = False
    return data_dict

def __qld_stream(stream_object):
    data_dict = {PARL_ID: 'QLD'}
    data_dict[URL] = '/qld'
    if(stream_object.is_live):
        data_dict[STREAM_STAT] = True
    else:
        data_dict[STREAM_STAT] = False
    return data_dict

def __fed_stream(stream_object):
    data_dict = {PARL_ID: 'Federal'}
    data_dict[URL] = '/federal'
    try: # This is my stupid solution to the site-breaking error that happens if no extra committees are detected
        stream_object.stream_urls['extra_committees']
        extra_comms = True
    except:
        extra_comms = False

    if(stream_object.lower_is_live or stream_object.upper_is_live or stream_object.committee_is_live or extra_comms):
        data_dict[STREAM_STAT] = True
    else:
        data_dict[STREAM_STAT] = False
    return data_dict

def __nsw_stream(stream_object):
    data_dict = {PARL_ID: 'NSW'}
    data_dict[URL] = '/nsw'
    if(stream_object.lower_is_live or stream_object.upper_is_live or stream_object.committee_is_live or stream_object.jubilee_is_live):
        data_dict[STREAM_STAT] = True
    else:
        data_dict[STREAM_STAT] = False
    return data_dict

def __tas_stream(stream_object):
    data_dict = {PARL_ID: 'Tasmania', 'lower_stat': stream_object.lower_is_live, 'upper_stat': stream_object.upper_is_live}
    data_dict[URL] = '/tas'
    if(data_dict['lower_stat'] or data_dict['upper_stat']):
        data_dict[STREAM_STAT] = True
    else:
        data_dict[STREAM_STAT] = False
    return data_dict

def __vic_stream(stream_object):
    data_dict = {PARL_ID: 'Victoria', URL: '/vic'}

    if(stream_object.lower_is_live or stream_object.upper_is_live or stream_object.committee_is_live):
        data_dict[STREAM_STAT] = True
    else:
        data_dict[STREAM_STAT] = False
    return data_dict

def __wa_stream(stream_object):
    data_dict = {PARL_ID: 'WA'}
    data_dict[URL] = '/wa'
    data_dict['radius'] = '0px 0px 10px 10px'
    if(stream_object.lower_is_live or stream_object.upper_is_live):
        data_dict[STREAM_STAT] = True
    else:
        data_dict[STREAM_STAT] = False
    return data_dict

def write_parl_stats():
    streams = []
    print('Writing stream_stats.json...')
    from legistream_backend.act import Stream as actStream
    from legistream_backend.federal import Stream as fedStream
    from legistream_backend.nsw import Stream as nswStream
    from legistream_backend.nt import Stream as ntStream
    from legistream_backend.qld import Stream as qldStream
    from legistream_backend.tas import Stream as tasStream
    from legistream_backend.vic import Stream as vicStream
    from legistream_backend.wa import Stream as waStream
    streams.append(__act_stream(actStream()))
    streams.append(__fed_stream(fedStream()))
    streams.append(__nsw_stream(nswStream()))
    streams.append(__nt_stream(ntStream()))
    streams.append(__qld_stream(qldStream()))
    streams.append(__tas_stream(tasStream()))
    streams.append(__vic_stream(vicStream()))
    streams.append(__wa_stream(waStream()))
    return(streams)

def write_json():
    with open(filepath, 'w') as file:
        data = [int(time.time()), write_parl_stats()]
        file.write(json.dumps(data, indent=2))
    with open(filepath, 'r') as file:
        return(json.loads(file.read()))

def check_statuses():
    try:
        with open(filepath, 'r') as file:
            parsed_data = json.loads(file.read())
            open(os.path.dirname(os.path.realpath(__file__)) + '/statuses/placeholder.json', 'w').write(json.dumps(parsed_data, indent=2))
            print('Using written JSON...')
            return(parsed_data[1])
    except:
        print('Using placeholder JSON...')
        return json.loads(open(os.path.dirname(os.path.realpath(__file__)) + '/statuses/placeholder.json', 'r').read())[1]