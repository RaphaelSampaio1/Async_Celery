# 🧠 Async Task Queue with Celery, RabbitMQ & Redis 🚀  

A simple yet powerful project demonstrating how to use **Celery** for asynchronous and distributed task processing in Python — using **RabbitMQ** as the message broker and **Redis** as the result backend.  

This setup allows you to handle background tasks (like sending emails, processing data, or complex calculations) **without blocking** your main application flow. 💡  

---

## ⚙️ Tech Stack

- 🐍 **Python 3.11+**  
- 💌 **Celery** — Distributed task queue  
- 🐇 **RabbitMQ** — Message broker  
- 💾 **Redis** — Cache & backend result storage  
- 🐳 **Docker & Docker Compose** — For containerized environment  

---

## 🧩 Project Overview

The core idea is to process time-consuming tasks **asynchronously** — letting the main program respond instantly while workers handle the heavy lifting in the background.

Example function:

```python
@app.task
def generate_random_number(max_value: int):
    """Generate a random number between 1 and the max_value after a delay."""
    time.sleep(5)
    return random.randint(1, max_value)
```

Instead of calling it directly:

```python
generate_random_number(100)
```

You can call it asynchronously:

```python
generate_random_number.delay(100)
```

💥 This sends the task to Celery workers that process it independently while your main Python app continues running.

---

## 🧠 Real Use Case Example

Imagine an e-commerce platform 🛍️:

When a user places an order:
- The main system quickly confirms the purchase ⚡  
- Meanwhile, background workers handle:
  - 📧 Sending confirmation emails  
  - 🧾 Generating invoices  
  - 📦 Updating inventory  
  - 📊 Pushing analytics events  

This architecture improves user experience and scalability 🚀  

---

## 🐳 Run the project locally

Make sure you have **Docker** and **Docker Compose** installed.  
Then just run:

```bash
docker compose up --build
```

This will start:
- 🐇 RabbitMQ (management UI on **http://localhost:15672**)  
- 💾 Redis  
- 🧩 Celery worker  
- 💻 Client app (sends tasks)

Then check your logs — you’ll see asynchronous tasks being executed in real-time 🎯  

---

## 🧰 Environment Variables

Create a `.env` file in the root folder:

```env
RABBITMQ_USER=guest
RABBITMQ_PASS=guest
CELERY_BROKER_URL=amqp://guest:guest@rabbitmq:5672//
CELERY_BACKEND_URL=redis://redis:6379/0
```

---

## 📁 Project Structure

```
.
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── worker.py
├── client.py
└── .env
```

---

## 🧠 Key Learnings

- How **Celery** orchestrates asynchronous tasks  
- How **RabbitMQ** and **Redis** communicate with background workers  
- The difference between **sync**, **async**, and **real parallel processing**  
- How to containerize a distributed system using **Docker Compose**  

---
## 👨‍💻 Author  

**Raphael Sampaio**  
💼 RPA Developer | Python Enthusiast | Building Automations & Scalable Systems  

🔗 [Connect with me on LinkedIn](https://www.linkedin.com/in/raphaelsampaio1)  
