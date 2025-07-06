# 🚚 DeliverEase — Courier Management System API

DeliverEase is a RESTful backend API built with Django & Django REST Framework to manage a scalable Courier Management System. It supports multiple user roles (Admin, User, Delivery Man), Stripe payment integration, and role-based order tracking and control.

<br/>

![Django](https://img.shields.io/badge/built%20with-Django-092E20?logo=django&logoColor=white)
![DRF](https://img.shields.io/badge/API-REST%20Framework-red)
![Stripe](https://img.shields.io/badge/payment-Stripe-blue)
![License](https://img.shields.io/badge/license-MIT-green)

---

## 📄 Project Overview

DeliverEase enables customers to place orders, admins to assign delivery men, and delivery men to manage their assigned deliveries. The API is secured with JWT authentication and includes payment handling via Stripe. It's ideal for logistics companies, courier startups, or educational use.

---

## 🧩 Features

- 🔐 JWT Authentication (Register, Login, Profile Management)
- 🧑‍💼 Role-based Access: Admin, Delivery Man, User
- 🛒 Order Management:
  - Users: Create & view orders
  - Admins: Assign delivery personnel & monitor deliveries
  - Delivery Men: View assigned orders and update status
- 💳 Stripe Integration: Payment initialization and confirmation
- 🧪 Postman Collection for easy testing and demonstration

---

## 🛠️ Tech Stack

| Layer      | Technology                      |
|------------|----------------------------------|
| Backend    | Django + Django REST Framework   |
| Auth       | JWT (`SimpleJWT`)                |
| Database   | PostgreSQL / SQLite              |
| Payments   | Stripe                           |
| Deployment | Render / Railway                 |

---

## 🗃️ API Endpoints

### 🔐 Auth
| Endpoint              | Method | Description        |
|-----------------------|--------|--------------------|
| `/api/login/`         | POST   | Login with credentials |
| `/api/register/`      | GET    | Register user (likely should be POST) |

### 👤 User Profile
| Endpoint              | Method | Description             |
|-----------------------|--------|-------------------------|
| `/api/profile/`       | GET    | Get current user profile |
| `/api/profile/`       | PATCH  | Update user profile      |

### 📦 Orders
| Endpoint                                   | Method | Description                     |
|--------------------------------------------|--------|---------------------------------|
| `/api/orders/create/`                      | POST   | Create a new order              |
| `/api/orders/`                              | GET    | List all orders (admin/user-specific) |
| `/api/orders/<id>/assign-delivery-man/`    | PATCH  | Assign a delivery man (admin only) |
| `/api/orders/<id>/update-status/`          | PATCH  | Update order status (delivery man) |

### 💳 Payments
| Endpoint                          | Method | Description               |
|-----------------------------------|--------|---------------------------|
| `/api/payment/initialize/`       | POST   | Initialize Stripe payment |
| `/api/payment/confirm/`          | POST   | Confirm Stripe payment    |

---

## 🔗 Relation Diagram

📎 **ERD Diagram**:  
_Embed or link here if available_  
_If you don’t have one yet, you can generate one using [dbdiagram.io](https://dbdiagram.io) or [drawsql.app](https://drawsql.app) and link it here._

---

## 🔗 Links

- 📂 GitHub Repository: [https://github.com/yourusername/deliverease](https://github.com/yourusername/deliverease)
- 🌐 Live API: [https://deliverease-2.onrender.com](https://deliverease-1.onrender.com)
- 📬 Postman Collection: [View Collection](https://bold-shuttle-486769.postman.co/workspace/SM-Technoly~f1bb514e-5f69-44fb-9b56-3e27013e6a5a/collection/25281354-7faf8d08-abca-4bba-a8eb-e802101ffbf6?action=share&source=collection_link&creator=25281354)

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
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt



## ▶️ Running the Server

```bash
python manage.py migrate
python manage.py runserver



