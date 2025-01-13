rm -r -f public
mkdir public
cp -r static/. public

python3 src/main.py
cd public && python3 -m http.server 8888