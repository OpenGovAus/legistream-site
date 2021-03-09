from legistream_backend.wa import Stream as waStream

wa_stream = waStream()

wa_urls = []

if(wa_stream.lower_is_live):
    wa_urls.append({'url': wa_stream.lower_stream_url, 'title': 'Legislative Assembly', 'safe': 'legislative-assembly-vid', 'thumb': 'legistream/img/thumbs/wa_la.webp'})
if(wa_stream.upper_is_live):
    wa_urls.append({'url': wa_stream.upper_stream_url, 'title': 'Legislative Council', 'safe': 'legislative-council-vid', 'thumb': 'wa_lc.webp'})

parl_title = 'Western Australia'