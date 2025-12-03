from flask import Flask, render_template, send_from_directory, abort
import os
import json

app = Flask(__name__)

DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')

THIS BREAKS THE CODE

@app.route('/')
def index():
    entries = []
    for entry in os.listdir(DATA_DIR):
        subdir = os.path.join(DATA_DIR, entry)
        if os.path.isdir(subdir):
            json_file = None
            photo_file = None
            for f in os.listdir(subdir):
                if f.lower().endswith('.json'):
                    json_file = f
                elif f.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
                    photo_file = f
            if json_file and photo_file:
                try:
                    with open(os.path.join(subdir, json_file), 'r') as jf:
                        info = json.load(jf)
                    entries.append({
                        'firstname': info.get('firstname', ''),
                        'lastname': info.get('lastname', ''),
                        'photo_url': f'/photo/{entry}/{photo_file}'
                    })
                except Exception:
                    continue
    return render_template('index.html', entries=entries)

@app.route('/photo/<entry>/<filename>')
def photo(entry, filename):
    dir_path = os.path.join(DATA_DIR, entry)
    if os.path.exists(os.path.join(dir_path, filename)):
        return send_from_directory(dir_path, filename)
    abort(404)

if __name__ == '__main__':
    app.run(debug=True)
