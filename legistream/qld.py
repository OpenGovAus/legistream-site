from legistream_backend.qld import Stream as qldStream

qld_stream = qldStream()

qld_urls = []

if(qld_stream.is_live):
    qld_urls.append({'url': qld_stream.stream_url, 'title': qld_stream.stream_title})

parl_title = 'Queensland'