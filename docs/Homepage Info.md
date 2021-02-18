# The Legistream Homepage

The server runs Celery in the background every few minutes to go out and refresh which parliaments are live, which are then displayed on the homepage.

![Homepage Live Parliaments](/gh-images/doc-img/live-now.png)

## stream_stats.json

The stream statuses are written to `legistream/statuses/stream_stats.json`, then duplicated to `placeholder.json` in the same directory. `placeholder.json` is used to avoid a server error if the homepage attempts to read the stream stats while they're being written by Celery.

---

The actual module that handles this function can be found at `legistream/statuscheck.py`, which basically just cycles through all the parliaments and checks if any of their streams are live. If any of them are, a `Ttue` value is written to `stream_stats.json`, if not, then a `false` value is written. It's pretty self explanatory: the parliaments with `true` values are then displayed under the "Currently Live Parliaments:" heading.