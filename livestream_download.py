import os
import time
import signal
import subprocess
import urllib.request
import json

def is_live(channel_id):
    URL = 'https://www.googleapis.com/youtube/v3/search?part=snippet&channelId='
    api_key = 'AIzaSyAVxUmipnFzlobZgDtx-z_-RezMi8xM1oo'
    URL_part = '&type=video&eventType=live&key='
    #сам запрос
    response = urllib.request.urlopen(URL + channel_id + URL_part + api_key)
    #преобразуем в json формат и в словарь
    json_m = response.read().decode('utf-8')
    data = json.loads(json_m)
    if len(data['items']) != 0:
        return data['items'][0]['id']['videoId']
    else:
        return 0

random_channel_id = 'UCpDzpaUTbIkdjkCZ9pmfMrA'
video_id = is_live(random_channel_id)
work_dir = '/Users/maksimveretennikov/Desktop/Coding/Project_Vyzvon'
ytdl_cmd = 'youtube-dl -f best -o "%(title)s-%(release_date)s.%(ext)s" --no-part --hls-use-mpegts '
stream_url = 'https://www.youtube.com/watch?v=' + video_id
cmd = ytdl_cmd + stream_url


os.chdir(work_dir)
os.system(cmd)

# mp4_file = work_dir + 'test.mp4'
# mp3_file = work_dir + 'test.mp3'
# cmd = 'ffmpeg -i {} -vn {}'.format(mp4_file, mp3_file)
# os.system(cmd)
