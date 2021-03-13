from legistream_backend.tas import Stream as tasStream

tas_stream = tasStream()

tas_urls = []

if(tas_stream.lower_is_live):
    tas_urls.append({'url': tas_stream.lower_stream_url, 'title': 'House of Assembly', 'safe': 'house-assembly-vid', 'thumb': 'legistream/img/thumbs/tas_hoa.webp'})
if(tas_stream.upper_is_live):
    tas_urls.append({'url': tas_stream.upper_stream_url, 'title': 'Legislative Council', 'safe': 'legislative-council-vid', 'thumb': 'legistream/img/thumbs/tas_lc.webp'})

parl_title = 'Tasmania'