from legistream_backend.nt import Stream as ntStream

nt_stream = ntStream()

nt_urls = []

if(nt_stream.lower_is_live):
    nt_urls.append({'url': nt_stream.lower_stream_url, 'title': 'Legislative Assembly', 'safe': 'legislative-assembly-vid', 'thumb': 'legistream/img/thumbs/nt_la.png'})

parl_title = 'Northern Territory'