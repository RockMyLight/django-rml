from django.shortcuts import render
from django.http import JsonResponse
import time


# Create your views here.
def main(request):
    context = {}
    return render(request, 'rml/main.html', context)


def jam(request):
    context = {}
    return render(request, 'rml/jam.html', context)


# API part

INTERVAL = 0.5
NUM_OF_FRAMES = 120
COLORS = ['#002b36', '#073642', '#586e75', '#657b83',
          '#839496', '#93a1a1', '#eee8d5', '#fdf6e3']


def next_color(color):
    index = COLORS.index(color)
    if index + 1 == len(COLORS):
        return COLORS[0]
    return COLORS[index + 1]


def api_dj(request, session_id=1):
    data = {}
    # number of connected clients in the grid
    data['num_of_clients'] = 6
    data['frames'] = []
    start_time = int(time.time())
    color = COLORS[0]
    for frame_index in range(NUM_OF_FRAMES):
        frame = {}
        frame['timestamp'] = (start_time + frame_index * INTERVAL) * 1000
        frame['color'] = color
        color = next_color(color)
        data['frames'].append(frame)
    repsonse = JsonResponse(data)
    return repsonse
