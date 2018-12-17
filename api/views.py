from django.shortcuts import render
import os
import json
from urllib.parse import unquote
from django.http import JsonResponse

def create_path_response(path):

  audio_extensions = ['wav', 'WAV', 'aif', 'mp3', 'AIFF']
  img_extensions = ['jpg', 'jpeg', 'tiff', 'JPEG', 'gif', 'png', 'bmp']
  
  os_path = f"./static{path}"

  contents = os.listdir(os_path)

  if contents:
    contents.sort()

  dirs = [c for c in contents if not '.' in c]
  files = [c for c in contents if '.' in c]
  audio = [f for f in files if f.split('.')[1] in audio_extensions]
  images = [f for f in files if f.split('.')[1] in img_extensions]
  
  if path[-1] != '/':
    path = f"{path}/"

  response = {
    "dirs": dirs,
    "audio": audio,
    "img": images[0] if images else None,
    "path": path,
  }
  # included to easily highlight the selected item
  # in each direcotry in the UI
  if path.split('/'):
    response['currentSelection'] = path.split('/')[-1]

  return response



def index(request):
  path = unquote(request.path)

  response = create_path_response(path)
  # add nested directory tree to response for audio file
  # so front end can display all parent directories
  if len(response['audio']):
    path_dirs = path.split('/')
    ancestor_tree = []
    current_path = ''
    for p in path_dirs:
      # hack to remove a bug
      if current_path == '/':
        current_path = ''

      next_path = f"{current_path}/{p}"
      current_path = next_path
      ancestor_tree.append(create_path_response(next_path))

    response.update({'ancestor_tree': ancestor_tree})

  return JsonResponse(response)
