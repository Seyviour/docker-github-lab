# app.py
from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, Docker! ENSF400 here!"

@app.route('/count')
def counter():
    try:
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
    except Exception as e:
        print(f"Error: {str(e)}")
        return f"An error occurred: {str(e)}"


if __name__ == '__main__':
    os.makedirs('/data', exist_ok=True)  # Ensure the /data directory exists
    app.run(host='0.0.0.0')
