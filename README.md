### Setting Up

Generate your twitter API keys from, copy `config.py.example` to `config.py` and update it with the generated twitter keys.

TWDL depends on tweepy so you would need to install it using `pip install tweepy`.

Once tweepy is installed, all you need to do is run `python twdl.py --url=tweet_url`  and voila! your tweet media gets downloaded (of course, that only happens if the tweet contains a gif or media).

### Flags

twdl accepts two CLI arguments:

```bash
--url: This is the complete link to the tweet (not just the tweet ID)
--filename: By default, twdl stores the file with same name as the name it gets from twitter. Use the --filename flag to override this with your preferred file name.
```
#### Feeling generous?

Star the project and do share!

