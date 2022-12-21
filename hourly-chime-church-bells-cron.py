#! /usr/bin/env python
import sys, os, time, subprocess

# exit if Do Not Disturb is enabled
dnd_stat = subprocess.getoutput('/usr/bin/xfconf-query -c xfce4-notifyd -p /do-not-disturb')
if dnd_stat == 'true':
    sys.exit()

# change this to where you have the mp3 files
sounds_dir = '/home/user/sounds/'

# play at 10% volume
cmd1 = '/usr/bin/ffplay -nodisp -autoexit -af "volume=0.1" '
cmd2 = ' >/dev/null 2>&1'

chimes = {
    'church_bell_single': 'Church-bell-single-hit.mp3',
    'church_bell_up': 'Large-church-bells-toll-scale-up.mp3',
    'church_bell_down': 'Large-church-bells-toll-scale-down.mp3',
    'divine_office_bell': 'Divine-Office-hourly-prayer-church-bell.mp3',
}

hour = int(time.strftime("%H"))

# hourly schedule
if hour in [3, 6, 12, 18]:
    chime = chimes['church_bell_single']
elif hour >= 4 and hour <= 8:
    chime = chimes['church_bell_up']
elif hour >= 17 and hour <= 21:
    chime = chimes['church_bell_down']
else:
    chime = chimes['divine_office_bell']

cmd = cmd1 + sounds_dir + chime + cmd2
# print(cmd)
os.system(cmd)
