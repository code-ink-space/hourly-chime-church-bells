# Hourly Chime Church Bells

Make your Linux machine sound church bells at the top of every hour.

Requirements:
- Python
- ffplay (ffmpeg)
- XFCE

1. Change `sounds_dir` to the location of the MP3 files.
2. Add to cron.
```
0 * * * * /home/user/scripts/hourly-chime-church-bells.sh
```

The script is set to chime different bell sounds.
- a deeper bell sound at certain special hours
- an "up" bell sound at dawn to early morning
- a "down" bell sound at dusk to early evening

Bell sounds distributed under “Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)” from https://orangefreesounds.com
