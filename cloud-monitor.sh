#!/bin/bash

echo ""
echo "========================================"
echo "   MOROCCO CLOUD MONITOR - CONTROL PANEL"
echo "========================================"
echo ""

while true; do
    echo ""
    echo "Select an option:"
    echo "1. Run website check now"
    echo "2. View latest results"
    echo "3. Push to GitHub (activate cloud)"
    echo "4. Check GitHub Actions status"
    echo "5. Exit"
    echo ""
    read -p "Enter choice (1-5): " choice
    
    case $choice in
        1)
            echo ""
            echo "Running website check..."
            python3 website_checker_cloud.py
            ;;
        2)
            echo ""
            echo "Latest results:"
            if [ -d "cloud_results" ] && [ "$(ls -A cloud_results 2>/dev/null)" ]; then
                latest=$(ls -t cloud_results/*.json | head -1)
                echo "File: $latest"
                echo "Content:"
                python3 -m json.tool < "$latest"
            else
                echo "No results yet. Run check first."
            fi
            ;;
        3)
            echo ""
            echo "Pushing to GitHub..."
            git add .
            git commit -m "Update cloud monitor"
            git push origin main
            echo "✅ Pushed! Cloud monitoring will start in 1-2 minutes."
            ;;
        4)
            echo ""
            echo "GitHub Actions URL:"
            echo "https://github.com/I-FARIH/morocco-devops-monitor/actions"
            echo ""
            echo "Open in browser to see cloud runs."
            ;;
        5)
            echo "Exiting..."
            exit 0
            ;;
        *)
            echo "Invalid choice"
            ;;
    esac
done
