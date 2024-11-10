# Overview:

This application is a simple Python API designed to handle orbital data. 
It provides endpoints for posting and retrieving state vectors, which represent the position and velocity of an object 
in space over time. The API allows clients to interact with the application via HTTP requests.

Testing the API with POSTMAN
I have used POSTMAN to test both the POST and GET endpoints of the API. I have also created an output folder where the results are stored.

POST Requests:
I submitted two POST requests first, as they are necessary to store enough state vectors for the application to calculate an interpolated vector for the GET request. These POST requests store the required state vectors, which the GET endpoint then uses for interpolation.
GET Request:
After submitting the POST requests, I tested the GET request to retrieve an interpolated state vector based on the provided time parameter.


## Directory Structure:

**app.py**  
This is the main entry point of the application. It initializes and runs the Flask web server.

**data/**  
This folder contains data files for the application. In this case, it holds a JSON file named `state_vectors.json`.

**app/**  
This folder contains several Python modules that define the API's structure and behavior:

- **__init__.py**  
  This file initializes the Flask application and registers the API routes.

- **routes.py**  
  This module defines the API endpoints for the application:  
  - `post_state_vector()`: Handles POST requests to add new state vectors.  
  - `get_state_vector()`: Handles GET requests to retrieve interpolated state vectors based on the specified time.

- **models.py**  
  This module holds state vectors in memory, allowing the application to temporarily store and manipulate data during runtime.

- **services.py**  
  This module defines functions for adding new state vectors, retrieving existing ones, and performing interpolations based on requested time parameters.

- **utils.py**  
  This file includes helper functions for tasks such as time conversion and data formatting.
