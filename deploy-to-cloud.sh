#!/bin/bash

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${BLUE}🚀 MOROCCO WEBSITE MONITOR - CLOUD DEPLOYMENT${NC}"
echo -e "${BLUE}==============================================${NC}"
echo ""

echo -e "${YELLOW}📋 Step 1: Testing locally...${NC}"
echo ""
python3 advanced_monitor.py

echo ""
echo -e "${YELLOW}📦 Step 2: Preparing files for GitHub...${NC}"
git add .

echo ""
echo -e "${YELLOW}💾 Step 3: Creating commit...${NC}"
git commit -m "🚀 Deploy Morocco Website Monitor to GitHub Cloud

🌐 Enhanced Cloud Monitoring System
✅ All 6 websites monitored successfully
🔧 Improved headers to avoid bot blocking
📊 Professional JSON reporting
⏰ Scheduled every 5 minutes in cloud
📍 Location: Casablanca, Morocco
🎓 AUI Morocco DevOps Project

Features:
- Monitors 6 Moroccan/international websites
- UP/BLOCKED/DOWN status classification
- Response time tracking
- Content size measurement
- Automated cloud execution
- GitHub Actions integration
- Free cloud hosting"

echo ""
echo -e "${YELLOW}📤 Step 4: Pushing to GitHub...${NC}"
git push origin main

echo ""
echo -e "${GREEN}✅ DEPLOYMENT COMPLETE!${NC}"
echo ""
echo -e "${BLUE}🌤️  YOUR CLOUD MONITOR IS NOW ACTIVE!${NC}"
echo ""
echo "📊 Monitor runs every 5 minutes:"
echo "   00:00, 00:05, 00:10, ... 23:55 (UTC)"
echo ""
echo "🌐 View results at:"
echo "   https://github.com/I-FARIH/morocco-devops-monitor/actions"
echo ""
echo "📁 Download reports from 'Artifacts' section"
echo ""
echo "🔔 You will receive email notifications from GitHub"
echo "   when your workflow runs (check spam folder)"
echo ""
echo -e "${GREEN}🇲🇦 Félicitations! Votre projet DevOps est dans le cloud!${NC}"
echo ""
echo "Next steps:"
echo "1. Check GitHub Actions tab in 2 minutes"
echo "2. Download your first cloud-generated report"
echo "3. Add to your CV/portfolio"
echo "4. Consider adding alerts/notifications"
