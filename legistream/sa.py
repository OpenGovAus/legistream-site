from legistream_backend.sa import Stream as saStream

sa_stream = saStream()

sa_urls = []

if(sa_stream.lower_is_live):
    sa_urls.append({'url': sa_stream.lower_stream_url, 'title': 'House of Assembly', 'safe': 'house-assembly-vid'})
if(sa_stream.upper_is_live):
    sa_urls.append({'url': sa_stream.upper_stream_url, 'title': 'Legislative Council', 'safe': 'legislative-council-vid'})

parl_title = 'South Australia'