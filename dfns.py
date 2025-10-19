# Save this script as 'malicious_script.py'

import os
import base64

# Define a malicious payload (base64 encoded for obfuscation)
malicious_payload = b"SGVsbG8sIFdvcmxkIQ=="  # This decodes to "Hello, World!"

# Decode the payload
decoded_payload = base64.b64decode(malicious_payload).decode('utf-8')

# Write the decoded payload to a file
malicious_file_path = os.path.join(os.getenv('TEMP'), 'malicious_file.txt')
with open(malicious_file_path, 'w') as f:
    f.write(decoded_payload)

print(f"Malicious file created at {malicious_file_path}")

# Additional malicious behavior: create a hidden file
hidden_file_path = os.path.join(os.getenv('TEMP'), '.hidden_file')
with open(hidden_file_path, 'w') as f:
    f.write("This is a hidden file.")

print(f"Hidden file created at {hidden_file_path}")
