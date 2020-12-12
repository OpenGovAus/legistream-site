from legistream_backend.tas import Stream as tasStream

tas_stream = tasStream()

tas_urls = []

if(tas_stream.lower_is_live):
    tas_urls.append({'url': tas_stream.lower_stream_url, 'title': 'House of Assembly'})
if(tas_stream.upper_is_live):
    tas_urls.append({'url': tas_stream.upper_stream_url, 'title': 'Legislative Council'})

parl_title = 'Tasmania'