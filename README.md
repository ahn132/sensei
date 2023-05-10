# sensei
A Discord bot written in Python utilizing PyMongo and MongoDB Atlas to store data

To use this bot, please follow the instructions on https://discord.com/developers/docs/getting-started to create your bot and get its token. Then copy and paste your token into the last line of main.py. Then, follow the instructions on https://www.mongodb.com/docs/atlas/getting-started/ to create a cluster in MongoDB Atlas. When you get your connection string, copy it into line 8 of db.py. After that, you should be good to go!

## Commands

`/hello` 
Says "Hello!" back

`/inspire` Says a random inspirational quote

`\quote <author>` Says a random quote from the given author. Note that the quote and author must be previously stored using `\new quote <content> -<author>`

`\hook git <user/repo>` Creates github and discord webhooks so that the channel receives updates when changes are made to the given repository. The user must have a token saved beforehand using `\set token <token>`

`\set token <token>` Saves the user's github token

`\new sad_word <word>` Saves the word to the list of sad words. Any time someone says a sad word, the bot will respond with an encouraging phrase

`\new angry_word <word>` Saves the word to the list of angry words. Any time someone says an angry word, the bot will repond with a calming phrase

`\new encouraging_phrase <phrase>` Saves the phrase to the list of encouraging phrases.

`\new calming_phrase <phrase>` Saves the phrase to the list of calming phrases

`\new quote <content> -<author>` Saves the quote which can later be retrieved using `\quote <author>`
