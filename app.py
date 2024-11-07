# app.py

from flask import Flask, jsonify
from locationsharinglib import Service
import os
import time

app = Flask(__name__)

@app.route('/location/<name>', methods=['GET'])
def get_location(name):
    try:
        cookies_file = 'cookies.txt'
        if not os.path.exists(cookies_file):
            return jsonify({'error': 'cookies.txt file not found'}), 400

        service = Service(cookies_file=cookies_file)

        persons = service.get_all_people()

        for person in persons:
            if person.nickname.lower() == name.lower():
                location_data = {
                    'name': person.nickname,
                    'latitude': person.latitude,
                    'longitude': person.longitude,
                    'timestamp': time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(person.datetime.timestamp()))
                }
                return jsonify(location_data), 200

        return jsonify({'error': f'Person "{name}" not found'}), 404

    except Exception as e:
        error_message = str(e)
        if 'Authentication' in error_message:
            return jsonify({'error': 'Authentication error: The cookies have expired or are invalid'}), 401
        else:
            return jsonify({'error': f'An unexpected error occurred: {error_message}'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
