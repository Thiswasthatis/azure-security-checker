# Azure Security Checker 🔒

Azure subscriptions can have misconfigurations that expose sensitive data
or leave accounts vulnerable. This tool helps administrators check their
Azure resource configurations against security best practices, making it
easier to catch and fix issues before they become threats.

## Checks Performed
- **HTTPS Only** — Ensures data in transit is encrypted and cannot be intercepted
- **Public Blob Access** — Ensures storage data is not publicly accessible to everyone
- **MFA Enabled** — Ensures accounts have a second layer of protection beyond passwords

## How to Run

### Requirements
- Python 3.x installed on your machine

### Steps
1. Clone the repository
   git clone https://github.com/yourusername/azure-security-checker.git

2. Navigate into the folder
   cd azure-security-checker

3. Run the checker
   python checker.py

## Sample Output

===== Azure Security Checker =====

Checking storage_account...
❌ FAIL - HTTPS is disabled, data can be intercepted
✅ PASS - Public blob access is disabled, data is protected

Checking identity...
✅ PASS - MFA is enabled, account is protected even if password is stolen

==================================

## Skills Demonstrated
- Python scripting
- JSON parsing
- Cloud security concepts (AZ-900)
- Azure resource configuration best practices