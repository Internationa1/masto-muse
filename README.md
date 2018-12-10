# masto-muse
Push your MPD now playing to your Mastodon Profile.

![Mastodon Profile Example](https://i.imgur.com/6bcNkdo.png)

# Installation

You will require python 3, mpd, ncmpcpp, and the following python libraries:

```
Mastodon.Py
musicpd
```

Move both *auth.py* and *muse.py* to your `.ncmpcpp` folder. Run creds.py, enter your instance url, username, and password. You should only ever have to run this once. **Someone please let me know if this is bad practice, as I am unsure**

In *muse.py*, edit the variables port, host, and instance, to match your mpd port, host, and mastodon instance, respectively.

On line 18 of *muse.py*, change the file location to the direct path of your .ncmpcpp config folder.

Finally, edit `.ncmpcpp/config`, and add the following line

```
execute on song change = "~/.ncmpcpp/muse.py"
```

Every time the song changes, your mastodon bio will reflect the new song.

# For the Future

This is barely a proof of concept, and many things need to be fixed and added. I'll get around to it eventually, probably.

1. auth.py needs to be streamlined. Does each instance need a seperate application cred? I do not know, so I leave users to generate one. This is probably a gross practice, but can't be sure.

2. A better mpd library could probably be used. This one works and closes cleanly, but, eh.

3. It'd be nice to append to your bio as opposed to wiping it and writing our own. This is easy, and my next step. Which I will do. Maybe.
