## SmartDev's Instagram Scraper API 🌟

![GitHub stars](https://img.shields.io/github/stars/TheSmartDevs/Insta-Scrapper-API?style=social)
![GitHub forks](https://img.shields.io/github/forks/TheSmartDevs/Insta-Scrapper-API?style=social)
![GitHub issues](https://img.shields.io/github/issues/TheSmartDevs/Insta-Scrapper-API)
![License](https://img.shields.io/github/license/TheSmartDevs/Insta-Scrapper-API)

Welcome to **SmartDev's Instagram Scraper API**! 🚀 This API allows developers to extract direct media URLs (images and videos) from Instagram posts and reels using a simple and reliable endpoint. Designed for developers and data enthusiasts, this open-source project provides clear documentation to integrate Instagram media scraping into your applications.

---

## 🌟 Features

- **Fast & Reliable**: Extract media URLs from Instagram posts and reels quickly.
- **Simple Endpoint**: Use a single GET request with a URL query parameter.
- **Open Source**: Fully open-source and community-driven.
- **Comprehensive Documentation**: Clear examples and notes for easy integration.

---

## 🚀 Getting Started

### Prerequisites
- A valid Instagram account with session cookies (`sessionid` and `csrftoken`).
- Basic knowledge of HTTP requests and JSON.
- Node.js or any HTTP client for testing (e.g., Postman, cURL).

### Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/TheSmartDevs/Insta-Scrapper-API.git
   cd Insta-Scrapper-API
   ```

2. **Install Dependencies**:
   ```bash
   npm install
   ```

3. **Configure Cookies**:
   - Add your Instagram session cookies in `cookies/cookies.txt` in Netscape format.
   - Example:
     ```
     # Netscape HTTP Cookie File
     .instagram.com	TRUE	/	FALSE	0	sessionid	your_session_id
     .instagram.com	TRUE	/	FALSE	0	csrftoken	your_csrf_token
     ```

4. **Run the API**:
   ```bash
   npm start
   ```

5. **Access the API**:
   - The API will be available at `http://localhost:3000` (or your deployed URL, e.g., `https://its-smart-dev.vercel.app`).

---

## 📚 API Documentation

### Endpoint: `GET /download`

Extract media URLs from an Instagram post or reel.

#### Request
```bash
curl -X GET "https://your-api-url/download?url=https://www.instagram.com/p/XXXXX/"
curl -X GET "https://your-api-url/download?url=https://www.instagram.com/reel/XXXXX/"
```

#### Response (Success)
```json
{
  "status": "success",
  "message": "Media URLs extracted successfully.",
  "media_urls": [
    "https://instagram.com/.../media1.jpg",
    "https://instagram.com/.../media2.mp4"
  ],
  "title": "Post caption",
  "author": "username",
  "developer": "API Developer : @ISmartDevs",
  "channel": "Updates Channel : @TheSmartDev"
}
```

#### Response (Error)
```json
{
  "status": "error",
  "message": "URL Required To Download Your Desired Media!",
  "media_urls": [],
  "title": null,
  "author": null,
  "developer": "API Developer : @ISmartDevs",
  "channel": "Updates Channel : @TheSmartDev"
}
```

#### Notes
- Requires valid Instagram session cookies in `cookies/cookies.txt` with `sessionid` and `csrftoken`.
- The URL must be in the format `https://www.instagram.com/p/XXXXX/` for posts or `https://www.instagram.com/reel/XXXXX/` for reels.
- Query parameters (e.g., `?igsh=...`) are ignored by the API.

---

## 🛠️ Usage Example

### Using JavaScript (Fetch)
```javascript
const url = "https://www.instagram.com/p/XXXXX/";
fetch(`https://your-api-url/download?url=${encodeURIComponent(url)}`)
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error("Error:", error));
```

### Using Python (Requests)
```python
import requests

url = "https://www.instagram.com/reel/XXXXX/"
response = requests.get(f"https://your-api-url/download?url={url}")
print(response.json())
```

---

## 🌍 Contributing

We love contributions! 💖 Follow these steps to contribute:

1. **Fork the Repository** 🍴
2. **Create a Branch**:
   ```bash
   git checkout -b feature-branch
   ```
3. **Commit Changes**:
   ```bash
   git commit -m "Add new feature"
   ```
4. **Push to Branch**:
   ```bash
   git push origin feature-branch
   ```
5. **Open a Pull Request** 📬

Check out the repository on [GitHub](https://github.com/TheSmartDevs/Insta-Scrapper-API).

---

## 📬 Contact Us

Join our community and stay updated:

- **Instagram**: [@ISmartDevs](https://x.com/abirxdhackz)
- **Telegram**: [TheSmartDev](https://t.me/TheSmartDev)
- **GitHub**: [@TheSmartDevs](https://github.com/TheSmartDevs/Insta-Scrapper-API)

---

## 🏆 Acknowledgments

- Built with ❤️ by [TheSmartDevs](https://t.me/TheSmartDev).
- Powered by [Bootstrap](https://getbootstrap.com), [Font Awesome](https://fontawesome.com), and [GSAP](https://greensock.com/gsap/) for the documentation site.
- Special thanks to our contributors! 🌟

---

## 📝 License

This project is licensed under the [MIT License](LICENSE).

---

© 2025 SmartDev's Instagram Scraper API | Powered by [TheSmartDev](https://t.me/TheSmartDev)
