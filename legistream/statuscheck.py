import os
import json
import time

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
    if(stream_object.lower_is_live or stream_object.upper_is_live or stream_object.committee_is_live):
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
    from legistream_backend.wa import Stream as waStream
    streams.append(__act_stream(actStream()))
    streams.append(__fed_stream(fedStream()))
    streams.append(__nsw_stream(nswStream()))
    streams.append(__nt_stream(ntStream()))
    streams.append(__qld_stream(qldStream()))
    streams.append(__wa_stream(waStream()))
    return(streams)

def write_json(current_time):
    with open(filepath, 'w') as file:
        data = [current_time, write_parl_stats()]
        file.write(json.dumps(data, indent=2))
    with open(filepath, 'r') as file:
        return(json.loads(file.read()))

def check_statuses():
    now = int(time.time())
    try:
        with open(filepath, 'r') as file:
            parsed_data = json.loads(file.read())
            if(now - parsed_data[0] >= 180):
                return(write_json(now)[1])
            else:
                return(parsed_data[1])
    except:
        return(write_json(now)[1])