./venv/bin/pyinstaller -D -F -n djshort -c dj_shortcut.py


echo "copying over to /usr/bin folder"
cp ./dist/djshort /usr/bin/djshort
