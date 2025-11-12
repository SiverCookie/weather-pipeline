# 🌦️ Weather Data Pipeline

A lightweight **Python data pipeline** that automatically fetches live weather information for Iași every 4 hours, stores it in a **PostgreSQL database**, and runs **automated tests** via **GitHub Actions CI**.

---

## 🚀 Project Overview

This project simulates a **DevOps automation scenario**:  
- Periodically collects public weather data (temperature, humidity, pressure, and description).  
- Stores the data in a structured PostgreSQL database.  
- Includes automated unit tests for data fetching and database operations.  
- Uses a **CI/CD workflow (GitHub Actions)** to validate every commit.  

Developed and deployed on a **Raspberry Pi 3 (32-bit Raspbian)**, with emphasis on automation, reliability, and maintainability.

---

## 🧩 Features

✅ Fetch live weather data using a REST API  
✅ Store it in a local PostgreSQL database  
✅ Modular Python codebase (with `src/` and `tests/` structure)  
✅ Unit testing with `pytest`  
✅ Continuous Integration with GitHub Actions  
✅ Configurable scheduling (e.g., via `cron` or `systemd`)  

---

## 🧠 Architecture


    ┌─────────────────────┐
    │  fetch_data.py      │
    │ (API -> JSON)       │
    └──────────┬──────────┘
               │
               ▼
    ┌─────────────────────┐
    │  db.py              │
    │ (Insert to PostgreSQL) │
    └──────────┬──────────┘
               │
               ▼
    ┌─────────────────────┐
    │  main.py            │
    │ (Pipeline Runner)   │
    └──────────┬──────────┘
               │
               ▼
    ┌─────────────────────┐
    │  GitHub Actions CI  │
    │ (pytest validation) │
    └─────────────────────┘

---

## 🧰 Tech Stack

| Category | Technology |
|-----------|-------------|
| Language | Python 3.13 |
| Database | PostgreSQL |
| Testing | pytest |
| CI/CD | GitHub Actions |
| Environment | Raspbian OS (32-bit) |
| API Source | [OpenWeatherMap API](https://openweathermap.org) |

---

## 🗄️ Database Schema

Database: `weather_data`  
Table: `measurements`

| Column | Type | Description |
|---------|------|-------------|
| id | SERIAL PRIMARY KEY | Auto-incrementing ID |
| timestamp | TIMESTAMP WITH TIME ZONE | Data fetch time |
| temperature | FLOAT | Temperature (°C) |
| humidity | FLOAT | Relative humidity (%) |
| pressure | FLOAT | Atmospheric pressure (hPa) |
| weather_description | TEXT | Weather condition summary |

---

## 🧪 Testing

Run all tests locally:
```bash
pytest -q
