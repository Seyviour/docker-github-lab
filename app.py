# app.py
from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, Docker! ENSF400 here!"

@app.route('/count')
def counter():
    count_file = '/data/count.txt'
    if not os.path.exists(count_file):
        with open(count_file, 'w') as f:
            f.write('0')
    
    with open(count_file, 'r') as f:
        count = int(f.read())
    
    count += 1
    
    with open(count_file, 'w') as f:
        f.write(str(count))
    
    return f"Hello, Docker! This page has been visited {count} times."


"""
If you have trouble running on port 5000, you can change the port in the last line to something else (e.g., 8080) and update the Dockerfile.
"""

# if __name__ == '__main__':
#     os.makedirs('/data', exist_ok=True)  # Ensure the /data directory exists
#     app.run(host='0.0.0.0')

"""
Run on Port 8080 instead of 5000 if you have trouble with port 5000:

"""

if __name__ == '__main__':
    os.makedirs('/data', exist_ok=True)  # Ensure the /data directory exists
    app.run(host='0.0.0.0', port=8000)
