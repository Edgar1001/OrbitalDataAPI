# OrbitalDataAPI

**This project**  
A Python API for managing and interpolating orbital state vectors, enabling clients to retrieve position and velocity data via HTTP requests.

---

# Overview

This application is a simple Python API designed to handle orbital data.  
It provides endpoints for posting and retrieving state vectors, which represent the position and velocity of an object in space over time. The API allows clients to interact with the application via HTTP requests.

### Testing the API with Postman

I used Postman to test both the POST and GET endpoints of the API. Results from testing are stored in an output folder.

- **POST Requests**:  
  I initially submitted two POST requests to store enough state vectors, allowing the application to calculate an interpolated vector for the GET request. These POST requests are necessary to provide the data required for interpolation.

- **GET Request**:  
  After the POST requests, I tested the GET request to retrieve an interpolated state vector based on a provided time parameter.

---

## Directory Structure

- **app.py**  
  This is the main entry point of the application. It initializes and runs the Flask web server.

- **data/**  
  Contains data files for the application. It currently includes a JSON file named `state_vectors.json`.

- **app/**  
  Contains Python modules that define the API's structure and behavior:
  
  - **`__init__.py`**  
    Initializes the Flask application and registers the API routes.
  
  - **`routes.py`**  
    Defines the API endpoints:
    - `post_state_vector()`: Handles POST requests to add new state vectors.
    - `get_state_vector()`: Handles GET requests to retrieve interpolated state vectors based on a specified time.
  
  - **`models.py`**  
    Stores state vectors in memory, allowing the application to temporarily manage and manipulate data during runtime.
  
  - **`services.py`**  
    Contains functions for adding new state vectors, retrieving existing ones, and performing interpolations based on the requested time parameter.
  
  - **`utils.py`**  
    Includes helper functions for tasks such as time conversion and data formatting.

---

