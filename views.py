from flask import jsonify
from datetime import datetime
from . import app

@app.route("/healthcheck")
def healthcheck():
    current_time = datetime.now().isoformat()

    response_data = {
        "status": "OK",
        "timestamp": current_time
    }

    return jsonify(response_data)  