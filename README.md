# ⚡ JWT Authentication API

A Flask authentication API demo that demonstrates password hashing with Bcrypt, JWT-based authentication, protected routes, and role checks.

`Python 3.x` · `Flask` · `PyJWT` · `Bcrypt` · `MIT License`

## 🚀 Features

- **Password hashing:** Uses Bcrypt rather than storing plaintext passwords.
- **JWT authentication:** Issues and validates signed JSON Web Tokens.
- **Protected routes:** Requires a valid Bearer token for protected resources.
- **Role checks:** Demonstrates authorization based on token claims.
- **API testing:** Includes a test script for authentication and protected-route flows.

## 🧩 Project Structure

- `app.py` — Flask API and authentication logic.
- `test_api.py` — API verification/demo script.
- `requirements.txt` — Python dependencies.

## 📋 Setup

```bash
git clone https://github.com/afaqkhan-io/secure-auth-gateway.git
cd secure-auth-gateway
python -m venv .venv
```

### Windows

```powershell
.venv\Scripts\activate
```

### macOS / Linux

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## ▶️ Run

```bash
python app.py
```

Use the included test script to exercise the authentication flow:

```bash
python test_api.py
```

## 🔐 Security Note

This is a learning/demo API, not a production authentication service. Do not use demo credentials or hard-coded secrets in a real deployment. Production systems should use environment-based secret management, HTTPS, secure cookie/token policies where appropriate, rate limiting, input validation, logging, and comprehensive security testing.

## 📄 License

Distributed under the **MIT License**. See `LICENSE` for details.
