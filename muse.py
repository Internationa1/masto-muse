#!/usr/bin/python3

port = 6600
host = 'localhost'
instance = 'https://cybre.space'

from mastodon import Mastodon
import musicpd

client = musicpd.MPDClient()
client.connect(host, port)
now = client.currentsong()
client.close()
client.disconnect()

nowp = ("Now Playing: %s - %s" % (now['title'],now['artist']))
print(nowp)

mast = Mastodon(client_id='masto-muse_appcred.secret',access_token='masto-muse_usercred.secret',api_base_url=instance)
mast.account_update_credentials(note=nowp)
