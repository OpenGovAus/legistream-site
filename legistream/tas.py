import os, json
from legistream_backend.tas import Stream as tasStream

tas_stream = tasStream()
try:
    with open(os.path.dirname(os.path.realpath(__file__)) + '/statuses/stream_stats.json', 'r') as f:
        _from_json = json.loads(f.read())[1][-3]
except:
    with open(os.path.dirname(os.path.realpath(__file__)) + '/statuses/placeholder.json', 'r') as f:
        _from_json = json.loads(f.read())[1][-3]

tas_urls = []

if(_from_json['lower_stat']):
    tas_urls.append({'url': tas_stream.lower_stream_url, 'title': 'House of Assembly', 'safe': 'house-assembly-vid', 'thumb': 'legistream/img/thumbs/tas_hoa.webp'})
if(_from_json['upper_stat']):
    tas_urls.append({'url': tas_stream.upper_stream_url, 'title': 'Legislative Council', 'safe': 'legislative-council-vid', 'thumb': 'legistream/img/thumbs/tas_lc.webp'})

parl_title = 'Tasmania'