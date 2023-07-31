#!/bin/bash

if [[ -f './namtheme.zip' ]]; then
  \rm -i './namtheme.zip'
  if [[ -f './namtheme.zip' ]]; then
    echo >&2 'Cannot continue while the old .zip exists'
    exit 1
  fi
fi

echo "Zipping..."
zip -r -q './namtheme.zip' manifest.json