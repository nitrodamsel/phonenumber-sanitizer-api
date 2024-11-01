# Phone Number Sanitization API

This Flask application provides an API for sanitizing phone numbers, logging them, and retrieving logged entries.

## Table of Contents

- [Setup Instructions](#setup-instructions)
- [API Endpoints](#api-endpoints)
  - [POST /sanitize](#post-sanitize)
  - [GET /logs](#get-logs)


## Setup Instructions

1. **Clone the Repository**

   Clone this repository to your local machine:

   ```bash
   git clone https://github.com/nitrodamsel/phonenumber-sanitizer-api
   cd phonenumber-sanitizer-api
   ```

2. **Create a Virtual Environment**

   It is recommended to create a virtual environment to manage dependencies:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**

   Install the required packages using `pip`:

   ```bash
   pip install -r requirements.txt
   ```


4. **Run the Application**

   Start the Flask application:

   ```bash
   flask run
   ```

   The API will be available at `http://localhost:5000`.

## API Endpoints

### POST /sanitize

This endpoint accepts a phone number, sanitizes it, and logs the result.

- **Request**
  
  **URL**: `/sanitize`  
  **Method**: `POST`  
  **Content-Type**: `application/json`  

  **Request Body**:

  ```json
  {
    "phone_number": "(123) 456-7890"
  }
  ```

  **Query Parameters** (optional):
  - `novalidate`: Set to `true` to bypass validation of the phone number.

- **Response**

  - **Success (200)**:
  
    ```json
    {
      "sanitized_phone_number": "+11234567890"
    }
    ```

  - **Error (400)**:

    ```json
    {
      "error": "Missing 'phone_number' field"
    }
    ```

    ```json
    {
      "error": "(123) 456-7890 is not a valid number."
    }
    ```

### GET /logs

This endpoint retrieves all logged phone number entries from the database.

- **Request**
  
  **URL**: `/logs`  
  **Method**: `GET`  

- **Response**

  - **Success (200)**:
  
    ```json
    [
      {
        "id": 1,
        "input_number": "(123) 456-7890",
        "sanitized_number": "+11234567890",
        "validated": true,
        "timestamp": "2024-11-01T12:00:00"
      },
      ...
    ]
    ```

  - **Error (500)**:

    ```json
    {
      "error": "Database error message"
    }
    ```
