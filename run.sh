#!/bin/sh
URL='http://localhost:5000/static/index.html#/sunburst';

# TODO: The install only needs to be run once
# This can be done in a separate script
cd frontend || { echo 'frontend directory missing'; exit 1; }
bower install;

cd ../backend || { echo 'backend directory missing'; exit 1; }


echo "Visit ${URL} in Chrome or Chromium";
# Open browser if possible
command -v xdg-open >/dev/null 2>&1 && xdg-open "${URL}";

python backend.py;
