from flask import Flask, request, jsonify
from models import PhoneLog, Session
from utils import sanitize_phone_number, sanitize_no_validation

app = Flask(__name__)

def log_phone_number(phone_number, sanitized_number, validated):
    """Helper function to log the phone number into the database."""
    session = Session()
    try:
        log_entry = PhoneLog(input_number=phone_number, sanitized_number=sanitized_number, validated=validated)
        session.add(log_entry)
        session.commit()
    except Exception as e:
        session.rollback()  # Rollback on error
        raise e  # Re-raise the exception for handling
    finally:
        session.close()

@app.route('/sanitize', methods=['POST'])
def sanitize():
    data = request.get_json()
    
    # Check if 'phone_number' is in the request data
    phone_number = data.get('phone_number')
    if not phone_number:
        return jsonify({"error": "Missing 'phone_number' field"}), 400

    novalidate = request.args.get('novalidate', 'false').lower() == 'true'
    
    # Sanitize phone number based on validation requirement
    sanitized_number = (sanitize_no_validation(phone_number) if novalidate 
                        else sanitize_phone_number(phone_number))
    
    if not sanitized_number:
        return jsonify({"error": f"{phone_number} is not a valid number."}), 400

    # Log the sanitized phone number
    log_phone_number(phone_number, sanitized_number, not novalidate)

    return jsonify({"sanitized_phone_number": sanitized_number}), 200

@app.route('/logs', methods=['GET'])
def get_logs():
    session = Session()
    try:
        # Query all phone logs
        logs = session.query(PhoneLog).all()
        log_entries = [{"id": log.id, "input_number": log.input_number,
                        "sanitized_number": log.sanitized_number,
                        "validated": log.validated,
                        "timestamp": log.timestamp} for log in logs]

        return jsonify(log_entries), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        session.close()

if __name__ == '__main__':
    app.run(debug=True)
