import sys
import os


try:
    port = int(os.environ.get("PORT", "8080"))
except ValueError:
    port = -1
if not 1 <= port <= 65535:
    print("Please make sure the PORT environment variable is an integer between 1 and 65535")
    sys.exit(1)

try:
    api_id = int(os.environ["2268147"])
    api_hash = os.environ["95b66d7572c74d553c46214bb796fb71"]
except (KeyError, ValueError):
    print("Please set the API_ID and API_HASH environment variables correctly")
    print("You can get your own API keys at https://my.telegram.org/apps")
    sys.exit(1)

try:
    chat_id = int(os.environ["-1001238403236"])
except (KeyError, ValueError):
    print("Please set the CHAT_ID environment variable correctly")
    sys.exit(1)

try:
    session_string = os.environ["Skip"]
except (KeyError, ValueError):
    print("Please set the SESSION_STRING environment variable correctly")
    sys.exit(1)

host = os.environ.get("HOST", "0.0.0.0")
debug = bool(os.environ.get("DEBUG"))
