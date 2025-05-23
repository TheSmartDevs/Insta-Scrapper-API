## SmartDev's Instagram Scraper API 🌟

![GitHub stars](https://img.shields.io/github/stars/TheSmartDevs/Insta-Scrapper-API?style=social)
![GitHub forks](https://img.shields.io/github/forks/TheSmartDevs/Insta-Scrapper-API?style=social)
![GitHub issues](https://img.shields.io/github/issues/TheSmartDevs/Insta-Scrapper-API)
![License](https://img.shields.io/github/license/TheSmartDevs/Insta-Scrapper-API)

Welcome to **SmartDev's Instagram Scraper API**! 🚀 This powerful and user-friendly API allows you to extract direct media URLs (images and videos) from Instagram posts with ease. Whether you're a developer, content creator, or data enthusiast, our API is designed to make your life simpler and your projects shine! ✨

---

## 🌟 Features

- **Fast & Reliable**: Quickly scrape media URLs from Instagram posts.
- **Easy to Use**: Simple POST request with a JSON payload.
- **Open Source**: Fully open-source and community-driven.
- **Dark/Light Mode**: Sleek UI with theme toggle for a personalized experience.
- **Responsive Design**: Works seamlessly on desktop and mobile devices.
- **Real-time Validation**: Instant feedback on Instagram URL input.
- **Success Animations**: Celebrate successful extractions with confetti! 🎉

---

## 📸 Demo

Try out the API directly on our [Live Demo](https://its-smart-dev.vercel.app/) and see it in action! Enter an Instagram post URL and get media URLs instantly.

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
   - The API will be available at `http://localhost:3000` (or your deployed URL).

---

## 📚 API Documentation

### Endpoint: `POST /download`

Extract media URLs from an Instagram post.

#### Request
```bash
curl -X POST https://your-api-url/download \
-H "Content-Type: application/json" \
-d '{"url": "https://www.instagram.com/p/XXXXX/"}'
```

#### Response (Success)
```json
{
  "status": "success",
  "message": "Media URLs extracted successfully.",
  "media_urls": [
    "https://instagram.com/.../media1.jpg",
    "https://instagram.com/.../media2.mp4"
  ]
}
```

#### Response (Error)
```json
{
  "status": "error",
  "message": "Invalid Instagram URL! Please ensure it contains a valid post code.",
  "media_urls": []
}
```

#### Notes
- Requires valid Instagram session cookies in `cookies/cookies.txt`.
- Ensure the URL is in the format `https://www.instagram.com/p/XXXXX/`.

---

## 🛠️ Usage Example

### Using JavaScript (Fetch)
```javascript
const url = "https://www.instagram.com/p/XXXXX/";
fetch("https://your-api-url/download", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({ url })
})
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error("Error:", error));
```

### Using Python (Requests)
```python
import requests

url = "https://www.instagram.com/p/XXXXX/"
response = requests.post("https://your-api-url/download", json={"url": url})
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

- **Instagram**: [@ISmartDevs](https://x.com/ISmartDevs)
- **Telegram**: [TheSmartDev](https://t.me/TheSmartDev)
- **GitHub**: [@TheSmartDevs](https://github.com/TheSmartDevs/Insta-Scrapper-API)

---

## 🏆 Acknowledgments

- Built with ❤️ by [TheSmartDevs](https://t.me/TheSmartDev).
- Powered by [Bootstrap](https://getbootstrap.com), [Font Awesome](https://fontawesome.com), and [GSAP](https://greensock.com/gsap/).
- Special thanks to our contributors! 🌟

---

## 📝 License

This project is licensed under the [MIT License](LICENSE).

---

© 2025 SmartDev's Instagram Scraper API | Powered by [TheSmartDev](https://t.me/TheSmartDev)

