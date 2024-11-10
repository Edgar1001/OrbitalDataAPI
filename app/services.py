from app.models import state_vectors
from scipy.interpolate import interp1d
import numpy as np
from app.utils import iso_to_seconds

state_vectors = []  

def add_state_vector(data):
    try:

        # Set for debugging purpose, to be removed after
        print("Data received in add_state_vector:", data)

        time_sec = iso_to_seconds(data['time'])


        # Set for debugging purpose, to be removed after
        print(f"Time in seconds: {time_sec}, type: {type(time_sec)}")
        print(f"posx: {data['posx']}, type: {type(data['posx'])}")
        print(f"posy: {data['posy']}, type: {type(data['posy'])}")
        print(f"posz: {data['posz']}, type: {type(data['posz'])}")
        print(f"velx: {data['velx']}, type: {type(data['velx'])}")
        print(f"vely: {data['vely']}, type: {type(data['vely'])}")
        print(f"velz: {data['velz']}, type: {type(data['velz'])}")

        # Append new state vector to the list
        state_vectors.append({
            'time': time_sec,
            'posx': data['posx'],
            'posy': data['posy'],
            'posz': data['posz'],
            'velx': data['velx'],
            'vely': data['vely'],
            'velz': data['velz'],
            'time_iso': data['time']
        })
        return {"message": "State vector added successfully"}

    except KeyError as e:
        return {"error": f"Missing field: {e}"}

def get_interpolated_vector(time_iso):

    # Set for debugging purpose, to be removed after
    print("time_iso received:", time_iso)
    print("Type of time_iso:", type(time_iso))

    time_sec = iso_to_seconds(time_iso)

    # Set for debugging purpose, to be removed after
    print("Time in seconds:", time_sec)

    if len(state_vectors) < 2:
        return {"error": "Not enough state vectors to interpolate"}
    times = np.array([vector['time'] for vector in state_vectors])
    
    # Set for debugging purpose, to be removed after
    print("Times array:", times) 

    positions = np.array([[vector['posx'], vector['posy'], vector['posz']] for vector in state_vectors])
    velocities = np.array([[vector['velx'], vector['vely'], vector['velz']] for vector in state_vectors])

    # Interpolate positions and velocities
    pos_interp = interp1d(times, positions, axis=0, fill_value="extrapolate")
    vel_interp = interp1d(times, velocities, axis=0, fill_value="extrapolate")

    interpolated_position = pos_interp(time_sec)
    interpolated_velocity = vel_interp(time_sec)

    print("Interpolated position:", interpolated_position)
    print("Interpolated velocity:", interpolated_velocity)

    # Return the interpolated state vector
    return {
        'time': time_iso,
        'posx': interpolated_position[0],
        'posy': interpolated_position[1],
        'posz': interpolated_position[2],
        'velx': interpolated_velocity[0],
        'vely': interpolated_velocity[1],
        'velz': interpolated_velocity[2]
    }


