import os
import json
import time
from django.shortcuts import render
from django.http import JsonResponse


# Create your views here.
def main(request):
    context = {}
    return render(request, 'rml/main.html', context)


def jam(request, session_id=1):
    context = {
        'session_id': session_id,
        'jam': get_the_jam(session_id),
    }
    return render(request, 'rml/jam.html', context)


# API part
JUMP_TO_FUTURE = 6  # s
INTERVAL = 0.5
NUM_OF_FRAMES = 120
COLORS = ['#002b36', '#073642', '#586e75', '#657b83',
          '#839496', '#93a1a1', '#eee8d5', '#fdf6e3']


def next_color(color):
    index = COLORS.index(color)
    if index + 1 == len(COLORS):
        return COLORS[0]
    return COLORS[index + 1]


def get_the_jam(session_id):
    d = os.path.dirname
    jam_path = os.path.join(d(d(__file__)), 'static', 'jams', str(session_id))
    if not os.path.exists(jam_path):
        return None
    intervals_path = os.path.join(jam_path, 'intervals.txt')
    jam = {}
    jam['intervals'] = [float(line.strip().strip(','))
                        for line in open(intervals_path)]
    logo_path = os.path.join(jam_path, 'logo.png')
    if os.path.exists(logo_path):
        jam['logo_path'] = logo_path
    song_path = os.path.join(jam_path, 'song.mp3')
    if os.path.exists(song_path):
        jam['song_path'] = song_path
    meta_path = os.path.join(jam_path, 'meta.json')
    if os.path.exists(meta_path):
        with open(meta_path) as json_file:
            jam['meta'] = json.load(json_file)
    return jam


def api_dj(request, session_id=1):
    data = {}
    # number of connected clients in the grid
    data['num_of_clients'] = 6
    data['frames'] = []
    start_time = int(time.time()) + JUMP_TO_FUTURE
    color = COLORS[0]
    # num_of_frames = NUM_OF_FRAMES
    # for frame_index in range(num_of_frames):jam
    jam = get_the_jam(session_id)
    if not jam:
        return JsonResponse(data)
    intervals = jam['intervals']
    the_time = start_time * 1000
    for interval in intervals:
        frame = {}
        # interval = frame_index * INTERVAL
        the_time += interval * 1000
        frame['timestamp'] = the_time
        frame['color'] = color
        color = next_color(color)
        data['frames'].append(frame)
    repsonse = JsonResponse(data)
    return repsonse
