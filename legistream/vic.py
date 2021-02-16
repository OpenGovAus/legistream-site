from legistream_backend.vic import Stream as vicStream

vic_stream = vicStream()

vic_urls = []

if(vic_stream.lower_is_live):
    vic_urls.append({'url': vic_stream.lower_stream_url, 'title': 'Legislative Assembly', 'safe': 'legislative-assembly-vid', 'thumb': 'legistream/img/thumbs/vic_la.png'})
if(vic_stream.upper_is_live):
    vic_urls.append({'url': vic_stream.upper_stream_url, 'title': 'Legislative Council', 'safe': 'legislative-council-vid', 'thumbs': 'legistream/img/thumbs/vic_lc.png'})
if(vic_stream.committee_is_live):
    vic_urls.append({'url': vic_stream.committee_stream_url, 'title': 'Committee', 'safe': 'com-vid', 'thumb': 'legistream/img/thumbs/vic_com.png'})

parl_title = 'Victoria'