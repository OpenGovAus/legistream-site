from legistream_backend.act import Stream as actStream

act_stream = actStream()

act_urls = []

if(act_stream.lower_is_live):
    act_urls.append({'url': act_stream.lower_stream_url, 'title': 'Legislative Assembly'})

parl_title = 'Australian Capital Territory'