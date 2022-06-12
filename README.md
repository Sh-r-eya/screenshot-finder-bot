# screenshot-finder-bot
A discord bot which helps you manage your screenshots.
Helps you keep track of your screenshots by adding them to an sqlite3 database.

## features
- Automatically saves screenchots when an image is posted with a caption
- Notifies you if you forget to add a caption so the image won't be saved. You will have to post the image again with a caption if you want it to be saved.
- Allows you to search for an image from the saved database using the command `botsearch`. 
-For example 
```txt
botsearch math homework
``` 
will return all the links to screenshots which were titled math homework.

The bot's reply will look like
```txt
https://discord.com/channels/Guild_id/Channel_id/Message_id
```
clicking on the link will take you to the message where the image was originally sent.

## License
MIT


