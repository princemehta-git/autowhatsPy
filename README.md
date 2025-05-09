# AutoWhats 🚀

**AutoWhats** is a simple desktop application for Windows built with **Python**, **Tkinter**, and **Selenium** to automate bulk WhatsApp messaging. Designed for efficiency, AutoWhats lets users send messages to multiple recipients through WhatsApp Web using contact lists in `.txt` or `.xlsx` format.

---

## 🧰 Features

- 🔁 Bulk WhatsApp messaging using Selenium and browser automation.
- 📄 Supports input from `number.txt` and Excel files (`.xlsx`).
- 🖥️ User-friendly GUI built with Tkinter.
- 🌐 Compatible with both Chrome and Firefox.
- ⚙️ Lightweight and portable – no installation needed.
- 🕵️ Error handling for unreachable contacts or invalid numbers.
- ⏱️ Option to schedule or delay messages.
- 🔒 Does **not** store any WhatsApp credentials or private data.

---

## 📁 Project Structure

AutoWhats/
│
├── AutoWhats.py        # Main GUI window using Tkinter  
├── main.py             # Core logic for message sending  
├── check_grp.py        # Group message checker  
├── chrome.py           # Chrome driver config  
├── firefox.py          # Firefox driver config  
├── config.py           # Config handler  
├── shutdown.py         # Optional system shutdown integration  
├── exceptions.py       # Custom exceptions  
├── rough.py            # Dev scratchpad (not used in prod)  
├── number.txt          # Sample list of numbers  
├── sample.xlsx         # Excel template for sending messages  
├── setting.txt         # App configuration file  
├── icon.ico / aw_icon.ico  # App icons  
└── README.md           # Project documentation  

---

## 🛠️ Installation & Setup

### 🧾 Requirements

- Python 3.7+
- Google Chrome or Mozilla Firefox
- ChromeDriver (https://sites.google.com/a/chromium.org/chromedriver/)
- GeckoDriver (https://github.com/mozilla/geckodriver/releases)
- Selenium

### 📦 Install dependencies

pip install selenium openpyxl

### 🖥️ Run the Application

python AutoWhats.py

---

## 📌 How to Use

1. Open `AutoWhats.py`.
2. Choose the browser (Chrome/Firefox).
3. Upload a list of phone numbers or select the `sample.xlsx`.
4. Type the message you want to send or load it from a `.txt` file.
5. Start sending! WhatsApp Web will open and messages will be sent automatically.

> Note: Make sure you’re logged into WhatsApp Web (https://web.whatsapp.com) before starting.

---

## ⚠️ Disclaimer

This tool is intended for **educational purposes** or **personal use**. Automating WhatsApp messages may violate WhatsApp's terms of service. Use responsibly. The creator is not responsible for any misuse or account bans.

---

## 📄 License

This project is licensed under the MIT License.

---

## 🙋‍♂️ Author

Developed by [@princemehta-git](https://github.com/princemehta-git)
