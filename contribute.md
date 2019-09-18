# Steps to contribute

## Getting the python code
---
Clone the repository to work localy  
```git clone https://github.com/Giraaaaa/Siebot```

 Create a new branch to work on localy  
```git checkout -b [name_of_your_local_branch]```

---
## Making a bot for testing purposes
---
[Log in](https://discordapp.com/login) or make a [new](https://discordapp.com/register) **discord account** if needed (you can create bots to any excisting discord account).
Don't forget to **verify your email** if you make a new account!!

Make a discord application from the [developers portal](https://discordapp.com/developers/applications).

Select you're newly made application and go to the `Bot` page in the navigation bar at the left-hand side.

Select *Add Bot* to add a bot (and give it a cool, like *'CoolBot'*)

---
## Adding the bot to the desired server 
---
Select the OAuth2 page from the left-hand navigation bar this now.

Check-off **Bot** in the `SCOPES` menu, and select the desired permissions in the now visible `BOT PERMISSIONS` menu.

Copy the generated URL, and paste it into your browser, select the desired server to add the bot by clicking "Authorise"

---
## Run the bot to be able do the magic
---
try to run the command `python bot.py` in your command line, and download the needed library's (with `pip install [libraryname]`)

Do this until you get an error about a missing file, named `stuff.json`. This file needs to contain the information related to your personal test bot.   
You should copy the contents of `exmpleStuff.json` into a new file with the name `stuff.json`.   
Fill in your own secrets in this file.  
By token, you need to fill in the token of your own discord bot, if you don't want to test reddit stuff, you don't need to fill in the reddit object.

---
## Add functions
---
Go code your ideas and when they work, send a pull request. If you encounter any problems, remember that google knows stuff (or at least acts like it does).
