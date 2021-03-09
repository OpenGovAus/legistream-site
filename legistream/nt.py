from legistream_backend.nt import Stream as ntStream
import os, json

nt_stream = ntStream()

nt_urls = []

directory = os.path.dirname(os.path.realpath(__file__)) + '/statuses/'

'''Since celery gets the stream statuses in the background AND since the NT only uses one stream (NT is unicameral), it's safe to use the homepage status
file to check if the NT is live. This fixes some timeout issues on the backend.'''

try:
    nt_islive = json.loads(open(directory + 'stream_statuses.json', 'r').read())[1][3]['stat']
except:
    nt_islive = json.loads(open(directory + 'placeholder.json', 'r').read())[1][3]['stat']

if(nt_islive):
    nt_urls.append({'url': nt_stream.lower_stream_url, 'title': 'Legislative Assembly', 'safe': 'legislative-assembly-vid', 'thumb': 'legistream/img/thumbs/nt_la.webp'})

parl_title = 'Northern Territory'