# Flask Photo Directory App

This Flask application serves an HTML page that lists entries from subdirectories. Each subdirectory should contain:
- A photo file (e.g., .jpg, .png)
- A JSON file with `firstname` and `lastname`

## Usage
1. Place your data directories inside the `data/` folder.
2. Each subdirectory should have a photo and a JSON file.
3. Run the app:
   ```bash
   python app.py
   ```
4. Open your browser at http://127.0.0.1:5000/

## Directory Structure Example
```
data/
  person1/
    photo.jpg
    info.json
  person2/
    image.png
    info.json
```

## info.json Example
```
{
  "firstname": "John",
  "lastname": "Doe"
}
```

## Notes
- Replace photo and JSON files with your actual data.
- The app will display all entries found in the `data/` directory.
