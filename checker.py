import json

with open("sample_config.json", "r") as f:
    config = json.load(f)

print("===== Azure Security Checker =====\n")

print("Checking storage_account...")
if config["storage_account"]["https_only"] == False:
    print("FAIL - HTTPS is disabled, data can be intercepted")
else:
    print("PASS - HTTPS is enabled, data in transit is encrypted")

if config["storage_account"]["public_blob_access"] == True:
    print("FAIL - Public blob access is enabled, anyone can view your data")
else:
    print("PASS - Public blob access is disabled, data is protected")

print("\nChecking identity...")
if config["identity"]["mfa_enabled"] == False:
    print("FAIL - MFA is disabled, no extra layer of security, account is vulnerable")
else:
    print("PASS - MFA is enabled, account is protected even if password is stolen")

print("\n==================================")