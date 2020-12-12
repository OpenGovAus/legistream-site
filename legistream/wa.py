from legistream_backend.wa import Stream as waStream

wa_stream = waStream()

wa_urls = []

if(wa_stream.lower_is_live):
    wa_urls.append({'url': wa_stream.lower_stream_url, 'title': 'Legislative Assembly'})
if(wa_stream.upper_is_live):
    wa_urls.append({'url': wa_stream.upper_stream_url, 'title': 'Legislative Council'})

parl_title = 'Western Australia'