from mastodon import Mastodon
from os import path

instance = str(input("What is your Mastodon Instance URL [i.e. https://mastodon.social]: "))

if path.isfile('masto-muse_appcred.secret') is False:
	Mastodon.create_app(
			'masto-muse',
			api_base_url = instance,
			to_file = 'masto-muse_appcred.secret',
			website = 'https://github.com/Internationa1/masto-muse'
	)

if path.isfile('masto-muse_usercred.secret') is False:
	user = str(input("Tell me your login email: "))
	password = str(input("Tell me your super great password: "))
	mat = Mastodon(client_id = 'masto-muse_appcred.secret', api_base_url = instance)
	mat.log_in(user,password,to_file = 'masto-muse_usercred.secret')
