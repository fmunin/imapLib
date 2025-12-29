import imaplib
import base64
import socket
import ssl

# --- Helper function to generate the OAuth2 token string ---
# You need a function that uses your client_id, client_secret, and refresh_token
# to obtain a current, valid access_token, and formats it correctly.
# A common format for the auth_string is 'user=<user_email>\\001auth=Bearer <access_token>\\001\\001'
# The google-api-python-client library can help manage token refreshing automatically.

def generate_oauth2_string(username, access_token):
    """Generates a correctly formatted XOAUTH2 authentication string."""
    auth_string = f'user={username}\x01auth=Bearer {access_token}\x01\x01'
    return base64.b64encode(auth_string.encode('utf-8')).decode('utf-8')

# --- Main IMAP connection code ---

# Replace with your Gmail address and a valid, *current* access token
GMAIL_USER = 'your_email@gmail.com'
GMAIL_ACCESS_TOKEN = 'your_current_oauth2_access_token' # Must be a valid, non-expired token

auth_bytes = generate_oauth2_string(GMAIL_USER, GMAIL_ACCESS_TOKEN)

try:
    # Connect to the Gmail IMAP server over SSL
    imap_conn = imaplib.IMAP4_SSL(host='imap.gmail.com', port=993)
    
    # Authenticate using the XOAUTH2 mechanism
    # The lambda function provides the auth string as a byte string
    imap_conn.authenticate('XOAUTH2', lambda x: auth_bytes.encode('utf-8'))
    
    print(f"Authentication successful for {GMAIL_USER}!")

    # Select the INBOX
    imap_conn.select('INBOX')

    # You can now perform IMAP operations, e.g., listing folders
    status, folders = imap_conn.list()
    print("Folders:", folders)

    # Logout
    imap_conn.logout()

except imaplib.IMAP4.error as e:
    print(f"Authentication failed: {e}")
except Exception as e:
    print(f"An error occurred: {e}")

