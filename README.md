# sensei
A Discord bot written in Python utilizing PyMongo and MongoDB Atlas to store data

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
