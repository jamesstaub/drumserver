import os
import json
import re
import math
from urllib.parse import unquote
from django.shortcuts import render
from django.http import JsonResponse

def create_path_response(path):

  audio_extensions = ['wav', 'WAV', 'aif', 'mp3', 'AIFF']
  img_extensions = ['jpg', 'jpeg', 'tiff', 'JPEG', 'gif', 'GIF', 'png', 'bmp']
  
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


def paginate_results(result_list, page):
  page_size = 20
  page_multiply = page - 1 # assume client is sending pages with 1 index , should be 0 index
  results = result_list[page_multiply*page_size:page_multiply*page_size+page_size]
  last_page = math.ceil(len(result_list) / page_size)
  return { "results": results, "page": page, "last_page": last_page }

def search(request):
  path = unquote(request.path)
  query = path.split('/search/')[1].lower()

  page = request.GET.get('page')
  page = int(page) if page else 1
  # include_dir = request.GET['include_dir']

  results = []
  for root, dirs, files in os.walk('./static'):
    for filename in files:
      if root.startswith('./static'):
        root = root[len("./static"):]

      # TODO add a query param include_dir to include directory name in search
      # ie search filename vs filepath
      # OR smartly break the query up by spaces, and search for directory first, then file name

      filepath = os.path.join(root, filename)
      re_file_search = re.search(query, filepath.lower())
      if re_file_search and filename.endswith(".mp3"):
        results.append(filepath)
  
  return JsonResponse(paginate_results(results, page))
