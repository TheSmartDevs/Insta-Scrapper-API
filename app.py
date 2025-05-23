from flask import Flask, request, jsonify, send_file  # Added send_file import
import instaloader
import os
import re
import http.cookiejar

app = Flask(__name__)

def validate_url(url):
    pattern = r'instagram\.com/(p|reel|tv)/([A-Za-z0-9-_]+)'
    match = re.search(pattern, url)
    if match:
        return match.group(2)
    return None

def load_cookies_from_file(cookies_path):
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
    except Exception:
        return None

def get_instagram_post_urls(url, cookies_file="cookies.txt"):
    result = {
        "status": "error",
        "message": "",
        "media_urls": [],
        "title": None,
        "author": None,
        "developer": "API Developer : @ISmartDevs",
        "channel": "Updates Channel : @TheSmartDev"
    }
    
    shortcode = validate_url(url)
    if not shortcode:
        result["message"] = "Please Provide Valid URL"
        return result

    try:
        loader = instaloader.Instaloader(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
        )

        script_dir = os.path.dirname(os.path.abspath(__file__))
        cookies_path = os.path.join(script_dir, cookies_file)

        if not os.path.isfile(cookies_path):
            result["message"] = f"Cookies Missing Bro Add Cookies"
            return result

        cookies = load_cookies_from_file(cookies_path)
        if not cookies:
            result["message"] = "Invalid Cookies Provided Update Cookies"
            return result

        loader.context._session.cookies.set("sessionid", cookies["sessionid"], domain=".instagram.com")
        loader.context._session.cookies.set("csrftoken", cookies["csrftoken"], domain=".instagram.com")

        post = instaloader.Post.from_shortcode(loader.context, shortcode)

        media_urls = []
        # For videos or images
        if post.is_video:
            media_urls.append(post.video_url)
        else:
            media_urls.append(post.url)

        # If sidecar (multiple media)
        if post.typename == "GraphSidecar":
            for node in post.get_sidecar_nodes():
                media_urls.append(node.video_url if node.is_video else node.display_url)

        result["status"] = "success"
        result["message"] = "Media URLs extracted successfully."
        result["media_urls"] = media_urls
        result["title"] = post.caption if post.caption else "No caption"
        result["author"] = post.owner_username

        return result

    except instaloader.exceptions.LoginRequiredException:
        result["message"] = "Sorry Bro Private Post Need Proper Cookies"
        return result
    except instaloader.exceptions.BadResponseException as bre:
        result["message"] = f"Instagram Meta API Dead"
        return result
    except Exception as e:
        result["message"] = f"Error: {str(e)}"
        return result

@app.route('/', methods=['GET'])
def api_status():
    """
    Flask endpoint for API status page (GET request).
    Serves the status.html file.
    """
    return send_file('status.html'), 200

@app.route('/download', methods=['GET'])
def download():
    url = request.args.get("url")
    if not url:
        return jsonify({"status": "error", "message": "URL Required To Download Your Desired Media!"}), 400

    result = get_instagram_post_urls(url)
    status_code = 200 if result["status"] == "success" else 400
    return jsonify(result), status_code

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
