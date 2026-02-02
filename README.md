# 🇲🇦 Morocco DevOps Monitor

## 🚀 Project Overview
A cloud-based website monitoring system that checks 6 Moroccan/international websites every 5 minutes using GitHub Actions.

## 📊 Features
- ✅ Cloud monitoring with GitHub Actions
- ✅ Runs every 5 minutes automatically
- ✅ Monitors 6 websites (AUI, Hespress, Avito, Google, LinkedIn, GitHub)
- ✅ JSON reports with performance metrics
- ✅ Docker container support
- ✅ Free cloud hosting (no credit card)

## 🛠️ Technology Stack
- Python 3.9+ with Requests library
- GitHub Actions for CI/CD
- Docker for containerization
- Git for version control
- Bash for automation

## 🚀 Quick Start
```bash
# Local testing
python3 website_checker_cloud.py

# Docker
docker-compose up --build

# Cloud deployment (automatically runs every 5 minutes)
git add . && git commit -m "Update" && git push
```
## 📁 Project Structure
morocco-devops-monitor/
├── website_checker_cloud.py    # Main Python script
├── Dockerfile                  # Docker configuration
├── docker-compose.yml          # Docker orchestration
├── requirements.txt            # Dependencies
├── manage-monitor.sh           # Management script
└── cloud_results/              # JSON reports

## ☁️ View Cloud Results
https://github.com/I-FARIH/morocco-devops-monitor

👨‍💻 About
Student: Issam Farih
University: AUI Morocco
Target: DevOps internships in Casablanca
Status: ✅ Operational locally, ready for cloud deployment

Last updated: February 2026
