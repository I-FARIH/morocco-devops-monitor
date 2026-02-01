# 🌐 Moroccan Website Monitor

## 🎯 Project Description
A production-grade DevOps monitoring system that checks Moroccan websites every 5 minutes. Built as part of my DevOps learning journey at Al Akhawayn University (AUI). Now **fully automated with Docker and scheduling**.

![Docker](https://img.shields.io/badge/Docker-✓-blue)
![Python](https://img.shields.io/badge/Python-3.9+-green)
![Automation](https://img.shields.io/badge/Automation-Scheduled-purple)
![Status](https://img.shields.io/badge/Status-Operational-brightgreen)
![Checks](https://img.shields.io/badge/Checks-14%2B-success)

## 🚀 Latest Updates (Day 3 - Automation Complete!)
✅ **Automated Scheduling** - Runs every 5 minutes via macOS launchd  
✅ **Live Dashboard** - Real-time monitoring with auto-refresh  
✅ **Management Tools** - Control panel and daily reports  
✅ **14+ Checks Performed** - All websites UP in latest runs  
✅ **Production-Ready** - Fully automated system  

## 📊 Real Monitoring Results
\`\`\`bash
🔄🔄🔄🔄🔄🔄🔄🔄🔄🔄
   MOROCCAN WEBSITE MONITOR
🔄🔄🔄🔄🔄🔄🔄🔄🔄🔄

🌐 AUI.ma: ✅ UP (0.54s) [200]
🌐 Hespress.com: ✅ UP (0.29s) [200]
🌐 Avito.ma: ✅ UP (0.42s) [200]
🌐 Google.com: ✅ UP (0.22s) [200]

──────────────────────────────────────────────────
📊 SUMMARY: 4/4 websites accessible
⏰ Check time: 2026-02-01 13:43:15
──────────────────────────────────────────────────
💾 Results saved to: /app/results/check_20260201_134315.txt
\`\`\`

## 🛠️ Technologies
- **Python 3.9** - Core monitoring script
- **Docker** - Containerization & deployment
- **Docker Compose** - Orchestration
- **macOS launchd** - Automated scheduling (every 5 minutes)
- **Bash Scripting** - Management tools

## 📁 Project Structure
\`\`\`
morocco-devops-monitor/
├── website_checker.py          # Main monitoring script
├── Dockerfile                  # Docker container definition
├── docker-compose.yml          # Docker orchestration
├── requirements.txt            # Python dependencies
├── .dockerignore              # Docker build exclusions
├── .gitignore                 # Git ignore rules
├── LICENSE                    # MIT License
├── docker_results/            # 14+ timestamped results
├── README.md                  # This documentation
└── website_results.txt        # Legacy results
\`\`\`

## 🐳 Docker Deployment
\`\`\`bash
# Clone repository
git clone https://github.com/I-FARIH/morocco-devops-monitor.git
cd morocco-devops-monitor

# Quick start with Docker Compose
docker-compose up --build

# Run in background
docker-compose up -d

# View logs
docker-compose logs -f
\`\`\`

## 🤖 Automation Features (Day 3)
The system now includes complete automation:

### Management Scripts (on your Desktop):
\`\`\`bash
~/Desktop/manage-monitor.sh status    # Check system status
~/Desktop/manage-monitor.sh run       # Run check immediately
~/Desktop/monitor-dashboard.sh        # Live dashboard (auto-refresh)
~/Desktop/daily-summary.sh            # Daily activity report
\`\`\`

### Automated Scheduling:
- Runs every 5 minutes automatically
- Uses macOS launchd for scheduling
- Saves results with timestamps
- Includes error handling and logging

## 🎓 Learning Journey
### ✅ Weekend 1 Complete:
- **Day 1**: Python + GitHub (Monitoring script)
- **Day 2**: Docker + Containerization
- **Day 3**: Automation + Scheduling

### 🔜 Coming Next:
- **Weekend 2**: AWS Cloud Deployment
- **Weekend 3**: French CV + Applications

## 📊 Performance Statistics
- **Total checks**: 14+
- **Today's checks**: 11 (Feb 1, 2026)
- **Response times**: 0.2s - 1.5s
- **Uptime**: 100% in latest checks
- **Automation**: Every 5 minutes

## 👨‍💻 Developer
**Issam Farih** - DevOps Student @ AUI Morocco  
📍 Casablanca, Morocco | 🎯 Seeking DevOps Internships  
🔗 [GitHub](https://github.com/I-FARIH)

> *"Learning DevOps by building practical systems. This project evolved from basic Python script to fully automated monitoring system."*

## 📄 License
MIT License - see [LICENSE](LICENSE) file.

## 🙏 Acknowledgments
- **Al Akhawayn University (AUI)** - Learning environment
- **Moroccan Tech Community** - Inspiration
- **DevOps Community** - Knowledge sharing

---
*Project updated: February 1, 2026 | Status: ✅ Operational | Next: AWS Cloud Deployment*
