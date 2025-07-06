# 🚚 DeliverEase — Courier Management System API

DeliverEase is a RESTful backend API built with Django & Django REST Framework to manage a scalable Courier Management System. It supports multiple user roles (Admin, User, Delivery Man), Stripe payment integration, and role-based order tracking.

<br/>

![Django](https://img.shields.io/badge/built%20with-Django-092E20?logo=django&logoColor=white)
![DRF](https://img.shields.io/badge/API-REST%20Framework-red)
![Stripe](https://img.shields.io/badge/payment-Stripe-blue)
![License](https://img.shields.io/badge/license-MIT-green)

---

## 🧩 Features

- 🔐 JWT Authentication (Register, Login, Profile)
- 🧑‍💼 Role-based Access: Admin, Delivery Man, User
- 🛒 Order Management
  - Users: Create & track orders
  - Admins: Assign delivery men & manage all orders
  - Delivery Men: View and update assigned orders
- 💳 Stripe Payment Integration (Pay on order or later)
- 🔒 Role-based Permissions (Admin-only, Owner-only, etc.)
- 🧪 Postman Collection for easy testing

---

## 🛠️ Tech Stack

| Layer         | Technology              |
|---------------|--------------------------|
| Backend       | Django + Django REST Framework |
| Auth          | JWT (`SimpleJWT`)        |
| Database      | PostgreSQL / SQLite      |
| Payments      | Stripe                   |
| Deployment    | Render / Railway         |

---

## 🚀 Getting Started

### 🔧 Requirements
- Python 3.8+
- pip / venv
- Stripe account (for API keys)

### 📦 Installation

```bash
git clone https://github.com/yourusername/deliverease.git
cd deliverease
python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows
pip install -r requirements.txt
