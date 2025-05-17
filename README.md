
# 🧰 Payfet Python SDK

**Payfet SDK** is an official Python library for integrating with [Payfet](https://payfet.vercel.app) — a multi-provider fintech infrastructure platform built for startups, SaaS companies, and cooperatives.

> **Motto: Payfet — For Everyone, By Everyone**

---

## ✨ Overview

Payfet simplifies how businesses connect with various financial providers (payments, virtual accounts, KYC, etc.) through a **single API layer**.  
This SDK provides a smooth developer experience for:

- 🔐 **Authenticating** as a Payfet tenant
- 🔗 **Managing provider connections**
- 💳 **Issuing virtual accounts and wallets**
- 📊 **Retrieving analytics & unified transaction logs**
- ⚙️ **Sending and receiving webhooks**
- 🧾 **Auditing activities across all connected services**

---

## 📦 Installation

```bash
pip install payfet
```

> Minimum Python version: `3.7+`

---

## ⚙️ Quickstart

```python
from payfet import PayfetClient

client = PayfetClient(
    tenant_token="your-tenant-token",
    business_id="your-business-id",
    secret_key="your-secret-key"
)

# Fetch balance from a connected provider
balance = client.wallets.get_balance(provider="flutterwave")
print(balance)

# View unified transaction logs
logs = client.analytics.get_transactions()
```

---

## 🔍 Core Modules

| Module         | Description                                             |
|----------------|---------------------------------------------------------|
| `wallets`      | Get balances, issue virtual accounts                    |
| `providers`    | Connect or disconnect providers                         |
| `kyc`          | Submit or retrieve KYC verification results             |
| `analytics`    | View transactions, reports, and performance summaries   |
| `logs`         | View raw activity logs by tenant                        |

---

## 📊 Unified Analytics

Get normalized transaction and balance data across all providers from one endpoint:

```python
analytics = client.analytics.get_overview()
```

You can filter by date, provider, or category.

---

## 🧾 Logs & Auditing

Payfet captures every sync, webhook event, and provider action in the logs module:

```python
logs = client.logs.get_all()
for log in logs:
    print(log["event"], log["timestamp"])
```

---

## 🌐 API Reference

Visit [docs.payfet.com](https://docs.payfet.com) (coming soon) for detailed endpoint documentation.

---

## 🤝 Contributing

We welcome community contributions! To get started:

1. Fork the repository  
2. Create a new branch (`feature/your-new-feature`)  
3. Commit your changes  
4. Submit a Pull Request

For larger features or ideas, feel free to open an issue first.

---

## 🛡️ Security

- Tenant tokens and secrets are encrypted in-memory
- All connections use TLS
- SDK does not store or log credentials locally

---

## 🙋 Support

- Issues: [GitHub Issues](https://github.com/AGASTRONICS/payfet-sdk/issues)
- Email: agastronics.dev@gmail.com
- X (Twitter): [@payfet](https://x.com/payfet)
- LinkedIn: [@payfet](https://www.linkedin.com/company/payfet)

---

## © About

Created and maintained by **Abdulsamad Opeyemi Abdulganiyu**  
**© Payfet Technologies, 2025**

---

> **“Payfet — For Everyone, By Everyone”**
>  
> Empowering developers to build inclusive financial infrastructure without the headache.
