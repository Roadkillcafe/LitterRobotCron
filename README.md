# LitterRobotCron
A python file utilizing pylitterbot project to be executed by cron at a desired interval.

I am simply storing the file I've modified to run in cron here. All credit goes to those working on and maintaining https://github.com/natekspencer/pylitterbot with which this script does not work. This is for my own local environment which is a RasberryPi 4 which is also running other tasks for me.

To work you will also need to add the lines to your cron via crontab -e 

My cron file minus my username and the starting comment is below. My python is a bit odd due to my own ineptitude so your path may be different. I make no claims this will work on your environment or hardware, I also will not be providing ongoing support. if it works for you cheers! 

The first line starting with * */6 will trigger the script every 6 hours. My litterbox occasionally doesn't detect my cats and this helps keep the box clean and cats happy even when I am away.
The second line starting with 0 0 1 on line 16 of this README remove the data from litterscript.log once a month so that the file doesn't get too big if you leave this for a long time.

```
LR_USERNAME=Youremail@whatever.com
LR_PASSWORD=yoursecurepassword
0 */6 * * * /usr/local/bin/python3 -u /home/yourusername/Documents/AutoClean.py >> /home/yourusername/Documents/litterscript.log 2>&1
0 0 1 * * > /home/yourusername/Documents/litterscript.log
```

Putting your username and password in cron keeps it out of plaintext in the .py file I have located in documents. this isn't necessary for the script to function and you can instead hard code the values in the AutoClean.py script if you want instead of importing them.
