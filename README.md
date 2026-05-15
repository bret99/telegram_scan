# telegram_scan (Telegram OSINT & Analytics Framework)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.9%20%7C%203.10%20%7C%203.11%20%7C%203.12-blue.svg)](https://www.python.org/)
[![Framework: Pyrogram](https://img.shields.io/badge/framework-Pyrogram-blue.svg)](https://github.com/pyrogram/pyrogram)

`telegram_scan` is an advanced, highly extensible OSINT (Open Source Intelligence) and reconnaissance framework designed for deep analysis of Telegram users, public/private channels, and group chats. Equipped with 16 specialized modules, it enables security researchers, threat intelligence analysts, and data scientists to extract, correlate, and audit metadata, message history, and user activity profiles.

The architecture is entirely decoupled, making it effortless for developers to build and integrate custom assessment modules.

## 🧩 Features & Capabilities

The framework incorporates 16 native modules engineered for comprehensive Telegram data harvesting:
- **User Profiling**: Extract unique IDs, historical usernames, bio metadata, and profile photo changes.
- **Chat & Channel Enumeration**: Audit group member lists, administrator privileges, and restriction statuses.
- **Activity & Content Scraping**: Analyze message velocity, forward patterns, and extract embedded metadata.
- **Extensible Architecture**: Programmatic design allowing seamless creation of custom modular plug-ins.

## 🚀 Prerequisites

### API Credentials
To interact with the Telegram MTProto API, you must obtain a development API ID and Hash:
1. Authenticate at the official [Telegram Development Portal](https://my.telegram.org/auth).
2. Navigate to **API development tools**.
3. Create a new application entry to generate your `api_id` and `api_hash`.

### System Dependencies
This framework leverages the high-performance MTProto library `pyrogram`.

## 🛠️ Installation & Configuration

1. **Clone the Repository:**
   ```bash
   git clone [https://github.com/bret99/telegram_scan.git](https://github.com/bret99/telegram_scan.git)
   cd telegram_scan
   ```

2. **Install Required Packages:**
   ```bash
   python3 -m pip install pyrogram
   ```

3. **Configure Access Credentials:**
   Copy the provided template configuration file and populate it with your Telegram API keys:
   ```bash
   cp access_creds.py.template access_creds.py
   ```
   Open `access_creds.py` and input your credentials:
   ```python
   api_id = "your_api_id"
   api_hash = "your_api_hash"
   ```

## 💻 Usage

Run the primary entry point to launch the interactive framework shell. Upon the first execution, `pyrogram` will prompt you to enter your phone number and authorization code (or 2FA password) to generate a secure local session file (`.session`).

```bash
python3 telegram_scan.py
```

> ⚠️ **Security Notice:** Never commit your generated `.session` files or `access_creds.py` to public repositories. These files grant full programmatic access to your Telegram account.

## 💎 Support the Project

If this tool helps protect your infrastructure, consider supporting the developer! 

### Crypto Wallets
| Asset | Network | Address |
| :--- | :--- | :--- |
| **BTC** | Bitcoin | `bc1qjwl80sv06xj2yhumn6k6xemchryem923wwts5x` |
| **USDT / ETH** | Ethereum (ERC20) | `0xc01b996c7b08ccfad463f27e54f1e74e6ac6f9ff` |
| **USDT / SOL** | Solana | `D7a5CdLaDwkKehnH82y6VJEF3hADWuupuhWCXecHvEnt` |
| **TON** | TON Network | `UQBhPLwdFiJdh6sZ96sZfxrxD9Lu6NFtaUecWeoHSM-EPc0P` |
| **LTC** | Litecoin | `ltc1qkm58ks5kuc64rjwd74sfalc5xsn7h6sr4vt45w` |
| **SOL** | Solana | `D7a5CdLaDwkKehnH82y6VJEF3hADWuupuhWCXecHvEnt` |

---

📜 License

This project is licensed under the MIT License - see the LICENSE file for details.
