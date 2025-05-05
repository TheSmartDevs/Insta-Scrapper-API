from flask import Flask, request, jsonify, send_file
import instaloader
import os
import re
import http.cookiejar

app = Flask(__name__)

def validate_url(url):
    """
    Validate and extract shortcode from Instagram URL.
    
    Args:
        url (str): Instagram post URL
    Returns:
        str: Shortcode if valid, None otherwise
    """
    pattern = r'instagram\.com/p/([A-Za-z0-9-_]+)'
    match = re.search(pattern, url)
    if match:
        return match.group(1)
    return None

def load_cookies_from_file(cookies_path):
    """
    Load Instagram cookies from a Netscape-format cookies.txt file.
    
    Args:
        cookies_path (str): Path to cookies.txt file
    Returns:
        dict: Dictionary of cookies (sessionid, csrftoken) or None if invalid
    """
    cookies = {}
    try:
        cookie_jar = http.cookiejar.MozillaCookieJar()
        cookie_jar.load(cookies_path, ignore_discard=True, ignore_expires=True)
        for cookie in cookie_jar:
            if cookie.name in ["sessionid", "csrftoken"] and cookie.domain == ".instagram.com":
                cookies[cookie.name] = cookie.value
        if "sessionid" in cookies and "csrftoken" in cookies:
            return cookies
        else:
            return None
    except Exception as e:
        return None

def get_instagram_post_urls(url, cookies_file="cookies/cookies.txt"):
    """
    Extract direct media URLs for an Instagram post.
    Requires valid cookies in cookies_file.
    
    Args:
        url (str): Instagram post URL
        cookies_file (str): Path to cookies.txt file for session authentication
    Returns:
        dict: Result with status, message, and media URLs (if successful)
    """
    result = {"status": "error", "message": "", "media_urls": []}
    
    # Validate URL
    shortcode = validate_url(url)
    if not shortcode:
        result["message"] = "Invalid Instagram URL! Please ensure it contains a valid post code (e.g., instagram.com/p/XXXXX)."
        return result

    try:
        # Initialize Instaloader with custom User-Agent
        loader = instaloader.Instaloader(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
        )

        # Resolve absolute path for cookies file relative to script directory
        script_dir = os.path.dirname(os.path.abspath(__file__))
        cookies_path = os.path.join(script_dir, cookies_file)

        # Check if cookies file exists
        if not os.path.isfile(cookies_path):
            result["message"] = f"Cookies file not found at {cookies_path}. Ensure {cookies_file} exists with valid Instagram cookies in Netscape format."
            return result

        # Load cookies
        cookies = load_cookies_from_file(cookies_path)
        if not cookies:
            result["message"] = "Failed to load session from cookies.txt: Missing required cookies (sessionid, csrftoken) or invalid format."
            return result

        # Set cookies in the Instaloader context
        loader.context._session.cookies.set("sessionid", cookies["sessionid"], domain=".instagram.com")
        loader.context._session.cookies.set("csrftoken", cookies["csrftoken"], domain=".instagram.com")

        # Get post and extract media URLs
        post = instaloader.Post.from_shortcode(loader.context, shortcode)
        media_urls = []

        if post.is_video:
            media_urls.append(post.video_url)
        else:
            media_urls.append(post.url)

        # Handle multi-media posts (sidecar)
        if post.typename == "GraphSidecar":
            for node in post.get_sidecar_nodes():
                media_urls.append(node.video_url if node.is_video else node.display_url)

        result["status"] = "success"
        result["message"] = "Media URLs extracted successfully."
        result["media_urls"] = media_urls
        return result

    except instaloader.exceptions.LoginRequiredException:
        result["message"] = f"Login required! This post may be private or requires authentication. Provide a valid {cookies_file} with active session cookies."
        return result
    except instaloader.exceptions.BadResponseException as bre:
        result["message"] = f"Instagram blocked the request (403 Forbidden): {str(bre)}. Ensure {cookies_file} contains valid, non-expired session cookies."
        return result
    except Exception as e:
        result["message"] = f"Oops! Something went wrong: {str(e)}. Check your internet connection, URL, cookies file, or try again later."
        return result

@app.route('/', methods=['GET'])
def api_status():
    """
    Flask endpoint for API status page (GET request).
    Serves the status.html file.
    """
    return send_file('status.html'), 200

@app.route('/download', methods=['POST'])
def download_post():
    """
    Flask endpoint to extract Instagram post media URLs.
    Expects JSON payload: {"url": "https://www.instagram.com/p/XXXXX/"}
    Returns JSON response with status, message, and media URLs.
    """
    data = request.get_json()
    if not data or "url" not in data:
        return jsonify({
            "status": "error",
            "message": "Invalid request. Please provide a JSON payload with a 'url' field."
        }), 400

    url = data["url"].strip()
    if not url:
        return jsonify({
            "status": "error",
            "message": "URL cannot be empty."
        }), 400

    # Get media URLs
    result = get_instagram_post_urls(url)
    status_code = 200 if result["status"] == "success" else 400
    return jsonify(result), status_code

# For Vercel serverless (WSGI export)
application = app