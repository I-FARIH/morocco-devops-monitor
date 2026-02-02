# 🌐 Moroccan Website Monitor

## 🎯 Project Description
A Python script that monitors the availability and response time of Moroccan websites. Built as part of my DevOps learning journey at Al Akhawayn University (AUI). Now **Dockerized for production deployment**.

![Docker](https://img.shields.io/badge/Docker-✓-blue)
![Python](https://img.shields.io/badge/Python-3.9+-green)
![DevOps](https://img.shields.io/badge/DevOps-Project-orange)

## 📊 Real Monitoring Results

\`\`\`
🔄🔄🔄🔄🔄🔄🔄🔄🔄🔄
   MOROCCAN WEBSITE MONITOR
🔄🔄🔄🔄🔄🔄🔄🔄🔄🔄

🌐 AUI.ma: ✅ UP (0.54s) [200]
🌐 Hespress.com: ✅ UP (0.29s) [200]
🌐 Avito.ma: ✅ UP (0.42s) [200]
🌐 Google.com: ⚠️ STATUS 429 (0.73s)

──────────────────────────────────────────────────
📊 SUMMARY: 3/4 websites accessible
⏰ Check time: 2026-01-30 11:46:42
──────────────────────────────────────────────────
💾 Results saved to: results/check_20260130_114642.txt
\`\`\`

## 🚀 Features
- Real HTTP requests to Moroccan websites
- Response time measurement in seconds
- **Docker containerization** for portability
- **Volume mounting** for persistent results
- Automated report generation (\`website_results.txt\`)
- Error handling for timeouts and connection issues
- Summary statistics

## 🛠️ Technologies
- **Python 3.9** - Core scripting language
- **Requests library** - HTTP requests
- **Docker** - Containerization & deployment
- **Docker Compose** - Orchestration
- **Git & GitHub** - Version control
- **macOS Terminal** - Development environment

## 📁 Project Structure
\`\`\`
morocco-devops-monitor/
├── website_checker.py     # Main monitoring script
├── Dockerfile            # Docker container definition
├── docker-compose.yml    # Docker orchestration
├── requirements.txt      # Python dependencies
├── .dockerignore        # Docker build exclusions
├── docker_results/      # Persistent results (volume mounted)
│   └── check_*.txt     # Timestamped result files
├── README.md           # This documentation
└── website_results.txt # Legacy results
\`\`\`

## 🐳 Docker Deployment

### Quick Start with Docker
\`\`\`bash
# Build and run the container
docker build -t morocco-monitor:v1 .
docker run --rm morocco-monitor:v1

# Run with volume mounting (save results on host)
docker run --rm -v $(pwd)/docker_results:/app/results morocco-monitor:v1
\`\`\`

### Using Docker Compose
\`\`\`bash
# Build and run with one command
docker-compose up --build

# Run in background
docker-compose up -d

# View logs
docker-compose logs

# Stop services
docker-compose down
\`\`\`

### Dockerfile Details
\`\`\`dockerfile
FROM python:3.9-alpine          # Lightweight base image
WORKDIR /app                    # Working directory
RUN mkdir -p /app/results       # Create results directory
COPY requirements.txt .         # Copy dependencies
RUN pip install -r requirements.txt  # Install packages
COPY website_checker.py .       # Copy application
RUN adduser -D -u 1000 appuser  # Create non-root user
USER appuser                    # Switch to non-root user
CMD ["python", "./website_checker.py"]  # Default command
\`\`\`

## 🏃‍♂️ Local Development
\`\`\`bash
# Clone repository
git clone https://github.com/I-FARIH/morocco-devops-monitor.git

# Install dependency
pip3 install requests

# Run monitor
python3 website_checker.py
\`\`\`
