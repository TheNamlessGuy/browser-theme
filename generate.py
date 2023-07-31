#!/usr/bin/python3

import os
import json

with open('./manifest.template.json', 'r') as f:
  data = json.loads(f.read())

map = {
  '--blackish': 'rgb(23, 21, 41)',

  '--red': 'rgb(200, 0, 0)',

  '--bright-purple': 'rgb(220, 0, 220)',
  '--purple-pink': 'rgb(100, 0, 100)',
  '--purple':      'rgb(179, 0, 179)',
  '--faded-purple':  'rgb(42, 33, 57)',
  '--dark-purple':   'rgb(34, 26, 46)',

  '--light-pink': 'rgb(255, 126, 216)',

  '--white':       'rgb(255, 255, 255)',
  '--faded-white': 'rgb(148, 157, 173)',
}

for key in data['theme']['colors']:
  value = data['theme']['colors'][key]
  alpha = None

  if '@' in value:
    [value, alpha] = value.split('@')

  if value in map:
    value = map[value]

    if alpha is not None:
      value = value.replace('rgb(', 'rgba(').replace(')', ', {0})'.format(alpha))

    data['theme']['colors'][key] = value

with open('./manifest.json', 'w') as f:
  f.write(json.dumps(data))