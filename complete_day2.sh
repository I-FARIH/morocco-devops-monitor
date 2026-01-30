#!/bin/bash
echo "🚀 Completing Day 2: Dockerizing Your DevOps Project"
echo "=================================================="

cd ~/Desktop/devops_project

echo "1. Creating final README..."
cat > README.md << 'README_EOF'
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
README_EOF

echo "✅ README created!"

echo "2. Creating LICENSE file..."
cat > LICENSE << 'LICENSE_EOF'
MIT License

Copyright (c) 2024 Issam Farih

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
LICENSE_EOF

echo "✅ LICENSE created!"

echo "3. Creating .gitignore..."
cat > .gitignore << 'GITIGNORE_EOF'
__pycache__/
*.pyc
.DS_Store
docker_results/
GITIGNORE_EOF

echo "✅ .gitignore created!"

echo "4. Fixing docker-compose.yml..."
cat > docker-compose.yml << 'COMPOSE_EOF'
services:
  website-monitor:
    build: .
    image: morocco-monitor:latest
    container_name: morocco-devops-monitor
    volumes:
      - ./docker_results:/app/results
    restart: "no"
COMPOSE_EOF

echo "✅ docker-compose.yml fixed!"

echo "5. Committing to GitHub..."
git add .
git commit -m "Complete Day 2: Dockerized website monitor with professional documentation"
git push origin main

echo "✅ All changes pushed to GitHub!"

echo ""
echo "🎉 DAY 2 COMPLETE! 🎉"
echo "====================="
echo "Your DevOps project now includes:"
echo "✅ Docker containerization"
echo "✅ Docker Compose orchestration"
echo "✅ Volume mounting for persistence"
echo "✅ Professional README with badges"
echo "✅ MIT License"
echo "✅ Clean .gitignore"
echo ""
echo "🔗 GitHub Repository:"
echo "https://github.com/I-FARIH/morocco-devops-monitor"
echo ""
echo "🚀 Ready for Day 3: Automation, Testing & CI/CD!"
