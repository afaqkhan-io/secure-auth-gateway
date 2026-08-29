import datetime
import jwt
import bcrypt
from flask import Flask, request, jsonify

app = Flask(__name__)

# Security Secret Key for JWT encryption
SECRET_KEY = "enterprise_super_secure_cryptographic_token_key_123!"

# Simulated Secure Database with pre-hashed password
raw_password = "SecurePassword123"
hashed_password = bcrypt.hashpw(raw_password.encode("utf-8"), bcrypt.gensalt())

USER_DATABASE = {
    "admin_agent@enterprise.com": {
        "password": hashed_password,
        "role": "SystemAdministrator",
    }
}


@app.route("/api/v1/auth/login", methods=["POST"])
def login_agent():
    data = request.get_json()
    if not data or not data.get("email") or not data.get("password"):
        return jsonify({"error": "Missing mandatory authorization parameters."}), 400

    user = USER_DATABASE.get(data.get("email"))
    if not user:
        return jsonify(
            {"error": "Invalid enterprise identity or mismatch credentials."}
        ), 401

    # Checking plain password against secure bcrypt cryptographic hash
    if bcrypt.checkpw(data.get("password").encode("utf-8"), user["password"]):
        token_payload = {
            "sub": data.get("email"),
            "role": user["role"],
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=30),
        }
        token = jwt.encode(token_payload, SECRET_KEY, algorithm="HS256")
        return jsonify(
            {
                "status": "Authentication Successful",
                "access_token": token,
                "token_type": "Bearer",
                "expires_in_seconds": 1800,
            }
        ), 200

    return jsonify(
        {"error": "Invalid enterprise identity or mismatch credentials."}
    ), 401


@app.route("/api/v1/secure-vault/data", methods=["GET"])
def get_secure_data():
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        return jsonify(
            {"error": "Access Denied. Bearer token missing in authorization header."}
        ), 403

    token = auth_header.split(" ")[1]
    try:
        decoded_payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return jsonify(
            {
                "status": "Access Granted",
                "authorized_identity": decoded_payload["sub"],
                "role_clearance": decoded_payload["role"],
                "vault_payload": {
                    "system_status": "Operational",
                    "secure_vault_hash": "MD5-84C844E-SECURE-DATA-STREAM",
                    "active_connections": 14,
                },
            }
        ), 200
    except jwt.ExpiredSignatureError:
        return jsonify({"error": "Access Denied. Security token has expired."}), 401
    except jwt.InvalidTokenError:
        return jsonify(
            {"error": "Access Denied. Tampered or invalid cryptographic token."}
        ), 401


if __name__ == "__main__":
    print("⚡ Starting Secure Enterprise JWT Authentication Gateway Server...")
    app.run(port=5000, debug=True)
