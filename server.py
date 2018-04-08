from flask import Flask, request, jsonify, Response
from flask_cors import CORS
import os
import requests
import json


app = Flask(__name__)
CORS(app)


@app.route('/endpoint', methods=['POST'])
def func():
    json_data = request.get_json(force=True)
    create_json = json.dumps(json_data, sort_keys=True, indent=4, separators=(',', ': '))
    request_info = json.loads(create_json)

    return jsonify(request_info)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run()  # local testing
    # app.run(host="0.0.0.0", port=port)  # production IP
