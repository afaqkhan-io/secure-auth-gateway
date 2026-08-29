import requests

BASE_URL = "http://127.0.0.1:5000"

print("--- STARTING SECURITY ROUTINE TESTING ---")
print("Step 1: Attempting login with correct credentials...")
login_payload = {"email": "admin_agent@enterprise.com", "password": "SecurePassword123"}
response = requests.post(f"{BASE_URL}/api/v1/auth/login", json=login_payload)

if response.status_code == 200:
    token = response.json().get("access_token")
    print(f"✅ Token Intercepted Safely: {token[:40]}...\n")

    print("Step 2: Accessing secure data vault using Bearer Token...")
    headers = {"Authorization": f"Bearer {token}"}
    vault_response = requests.get(
        f"{BASE_URL}/api/v1/secure-vault/data", headers=headers
    )
    print("Vault Response:", vault_response.json())
else:
    print("❌ Login Failed", response.json())
