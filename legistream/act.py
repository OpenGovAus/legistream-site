from legistream_backend.act import Stream as actStream

act_stream = actStream()

act_urls = []

if(act_stream.lower_is_live):
    act_urls.append({'url': act_stream.lower_stream_url, 'title': 'Legislative Assembly', 'safe': 'legislative-assembly-vid', 'thumb': 'legistream/img/thumbs/act_la.webp'})

parl_title = 'Australian Capital Territory'