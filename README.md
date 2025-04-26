# 🔍 Django Live Search App with Real-Time WebSocket Updates

A Django application that implements **live search across multiple related models** using **Django Channels** (WebSockets). The search triggers after entering 3+ characters and returns results in real-time.

---

## 📦 Features

- Search across:
  - `Company` (name, country, industry, founded year)
  - `CompanyDetails` (type, size, CEO, HQ)
  - `FinancialData` (year, revenue, net income)
- Real-time results with **Django Channels** and **WebSockets**
- Simple HTML/JS frontend

---

## 🧰 Tech Stack

- Django 4.x+
- Django Channels
- SQLite 
- HTML + JavaScript (Fetch + WebSocket)

---

## 🚀 Setup Instructions


```bash
git clone
cd django-live-search
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py shell < seed_data.py or use your own db data
python manage.py runserver
```
##  You should see the following message
```bash

Django version 4.2.20, using settings 'live_search_project.settings'
Starting ASGI/Daphne version 4.1.2 development server at http://127.0.0.1:8000/
```