import requests
import time
import logging
from datetime import datetime
import sys
import os

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler('/app/results/monitor.log')
    ]
)

def check_website(url, timeout=10):
    """Check if a website is up and measure response time"""
    try:
        start_time = time.time()
        response = requests.get(url, timeout=timeout)
        response_time = time.time() - start_time
        is_up = response.status_code == 200
        
        logging.info(f"{url} - Status: {response.status_code} - Response Time: {response_time:.2f}s - UP: {is_up}")
        
        return url, response.status_code, response_time, is_up
    
    except requests.exceptions.Timeout:
        logging.error(f"{url} - Timeout after {timeout} seconds")
        return url, 0, timeout, False
    except requests.exceptions.ConnectionError:
        logging.error(f"{url} - Connection Error")
        return url, 0, 0, False
    except Exception as e:
        logging.error(f"{url} - Unexpected error: {str(e)}")
        return url, 0, 0, False

def save_result(result):
    """Save result to file"""
    timestamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")
    filename = f"/app/results/check_{timestamp}.txt"
    
    with open(filename, "w") as f:
        f.write(f"Morocco DevOps Monitor - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("=" * 50 + "\n")
        
        for url, status, response_time, is_up in result:
            status_text = "UP" if is_up else "DOWN"
            f.write(f"{url} - Status: {status} - Response Time: {response_time:.3f}s - {status_text}\n")
        
        f.write("=" * 50 + "\n")
    
    return filename

def main():
    """Main monitoring function - runs continuously"""
    websites = [
        "https://www.aui.ma",
        "https://www.hespress.com", 
        "https://www.avito.ma",
        "https://www.google.com"
    ]
    
    check_interval = 300  # 5 minutes between checks
    
    logging.info("=" * 60)
    logging.info("🚀 Morocco DevOps Monitor Started")
    logging.info(f"📊 Monitoring {len(websites)} websites")
    logging.info(f"⏰ Check interval: {check_interval} seconds")
    logging.info("=" * 60)
    
    check_count = 0
    
    while True:
        check_count += 1
        logging.info(f"🔍 Starting check #{check_count}")
        
        results = []
        for website in websites:
            result = check_website(website)
            results.append(result)
        
        # Save results
        result_file = save_result(results)
        logging.info(f"💾 Results saved to: {result_file}")
        
        # Count up/down
        up_count = sum(1 for _, _, _, is_up in results if is_up)
        down_count = len(websites) - up_count
        
        logging.info(f"📈 Summary: {up_count} UP, {down_count} DOWN")
        
        if down_count > 0:
            logging.warning(f"⚠️  Alert: {down_count} website(s) are DOWN!")
        
        logging.info(f"⏳ Next check in {check_interval} seconds...")
        logging.info("-" * 40)
        
        # Wait for next check
        time.sleep(check_interval)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logging.info("👋 Monitor stopped by user")
    except Exception as e:
        logging.error(f"💥 Unexpected error: {str(e)}")
        sys.exit(1)
