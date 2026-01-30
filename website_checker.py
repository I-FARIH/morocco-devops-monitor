import requests
import time
import os
from datetime import datetime

def check_website(url, name):
    """Check if a website is accessible"""
    try:
        start_time = time.time()
        response = requests.get(
            url, 
            timeout=10, 
            headers={'User-Agent': 'Morocco-DevOps-Monitor/1.0'}
        )
        elapsed_time = time.time() - start_time
        
        if response.status_code == 200:
            return f"🌐 {name}: ✅ UP ({elapsed_time:.2f}s) [{response.status_code}]", True
        else:
            return f"🌐 {name}: ⚠️ STATUS {response.status_code} ({elapsed_time:.2f}s)", False
    except requests.exceptions.RequestException as e:
        return f"🌐 {name}: ❌ ERROR: {str(e)[:50]}", False

def main():
    """Main monitoring function"""
    websites = {
        "AUI.ma": "https://www.aui.ma",
        "Hespress.com": "https://www.hespress.com", 
        "Avito.ma": "https://www.avito.ma",
        "Google.com": "https://www.google.com"
    }
    
    print("\n" + "🔄" * 10)
    print("   MOROCCAN WEBSITE MONITOR")
    print("🔄" * 10 + "\n")
    
    results = []
    up_count = 0
    
    for name, url in websites.items():
        status, is_up = check_website(url, name)
        print(status)
        results.append(status)
        
        if is_up:
            up_count += 1
    
    print("\n" + "─" * 50)
    
    # Summary
    total = len(websites)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    summary = f"📊 SUMMARY: {up_count}/{total} websites accessible"
    print(summary)
    print(f"⏰ Check time: {timestamp}")
    print("─" * 50)
    
    # Save results to file
    try:
        # Ensure results directory exists
        os.makedirs("results", exist_ok=True)
        
        filename = f"results/check_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(filename, "w") as f:
            f.write("MOROCCAN WEBSITE MONITOR - RESULTS\n")
            f.write("=" * 50 + "\n")
            f.write(f"Check performed at: {timestamp}\n")
            f.write("-" * 50 + "\n")
            for result in results:
                f.write(result + "\n")
            f.write("-" * 50 + "\n")
            f.write(f"{summary}\n")
            f.write("=" * 50 + "\n")
        
        print(f"💾 Results saved to: {filename}")
    except Exception as e:
        print(f"⚠️ Could not save results: {e}")

if __name__ == "__main__":
    main()
