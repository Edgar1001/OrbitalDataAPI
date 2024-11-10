from flask import Blueprint, request, jsonify
from app.services import add_state_vector, get_interpolated_vector
from datetime import datetime

api = Blueprint('api', __name__)

@api.route('/', methods=['GET'])
def home():
    return "<h1>Welcome to the Orbit API by Edgar Rosende</h1><p>Use /state_vector to POST or GET state vectors.</p>"

# POST endpoint 
@api.route('/state_vector', methods=['POST'])
def post_state_vector():
    data = request.get_json()

    # Set for debugging purpose, to be removed after
    print("Received Data:", data)
    print("Data Types:")
    for key, value in data.items():
        print(f"{key}: {type(value)}") 

    # Validate input
    required_fields = ["time", "posx", "posy", "posz", "velx", "vely", "velz"]
    if not all(field in data for field in required_fields):
        return jsonify({"error": "All fields are required: time, posx, posy, posz, velx, vely, velz"}), 400

    # Add state vector
    response = add_state_vector(data)
    
    return jsonify(response), 201 if response.get("message") == "State vector added successfully" else 400

# GET endpoint 
@api.route('/state_vector', methods=['GET'])
def get_state_vector():
    time_iso = request.args.get('time')

    if not time_iso:
        return jsonify({'error': 'Time parameter is required'}), 400

    try:
        # Set for debugging purpose, to be removed after
        print("Received time (ISO format):", time_iso)

        # Convert the time string to datetime object 
        time_requested = datetime.fromisoformat(time_iso.replace("Z", "+00:00"))

        # Set for debugging purpose, to be removed after
        print("Converted datetime:", time_requested)

    except ValueError:
        return jsonify({"error": "Invalid time format. Use ISO format."}), 400

    response = get_interpolated_vector(time_iso)

    if response is None:
        return jsonify({"error": "No data found for the specified time."}), 404

    return jsonify(response)

