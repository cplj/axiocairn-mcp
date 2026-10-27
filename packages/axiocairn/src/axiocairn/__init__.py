"""Connection information for the Axiocairn MCP server."""
__version__ = "0.0.1"

URL = "https://axiocairn.com/mcp"
GUIDE = "https://axiocairn.com/en/assistant"


def main() -> None:
    print("Axiocairn MCP server (hosted, account authorization required)")
    print("Endpoint: " + URL)
    print("Connection guide: " + GUIDE)
    print("This package contains no server code; it only prints connection details.")
