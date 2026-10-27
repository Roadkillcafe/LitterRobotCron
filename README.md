# LitterRobotCron
A python file utilizing pylitterbot project to be executed by cron at a desired interval.

I am simply storing the file I've modified to run in cron here. All credit goes to those working on and maintaining https://github.com/natekspencer/pylitterbot with which this script does not work. This is for my own local environment which is a RasberryPi 4 which is also running other tasks for me.

To work you will also need to add the lines to your cron via crontab -e 

My full cron file minus removing my username is below. My python is a bit odd due to my own ineptitude so your path may be different. I make no claims this will work on your environment or hardware, I also will not be providing ongoing support. if it works for you cheers! 

The first line starting with * */6 will trigger the script every 6 hours. My litterbox occasionally doesn't detect my cats and this helps keep the box clean and cats happy even when I am away.
The second line starting with 0 0 1 on line 39 of this README remove the data from litterscript.log once a month so that the file doesn't get too big if you leave this for a long time.

# Edit this file to introduce tasks to be run by cron.
#
# Each task to run has to be defined through a single line
# indicating with different fields when the task will be run
# and what command to run for the task
#
# To define the time you can provide concrete values for
# minute (m), hour (h), day of month (dom), month (mon),
# and day of week (dow) or use '*' in these fields (for 'any').
#
# Notice that tasks will be started based on the cron's system
# daemon's notion of time and timezones.
#
# Output of the crontab jobs (including errors) is sent through
# email to the user the crontab file belongs to (unless redirected).
#
# For example, you can run a backup of all your user accounts
# at 5 a.m every week with:
# 0 5 * * 1 tar -zcf /var/backups/home.tgz /home/
#
# For more information see the manual pages of crontab(5) and cron(8)
#
# m h  dom mon dow   command
LR_USERNAME=Youremail@whatever.com
LR_PASSWORD=yoursecurepassword
* */6 * * * /usr/local/bin/python3 -u /home/yourusername/Documents/AutoClean.py >> /home/yourusername/Documents/litterscript.log 2>&1
0 0 1 * * > /home/yourusername/Documents/litterscript.log
