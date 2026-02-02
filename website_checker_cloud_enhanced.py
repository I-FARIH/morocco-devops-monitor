import requests
import time
import json
import os
from datetime import datetime

class MoroccoWebsiteMonitor:
    def __init__(self):
        self.websites = {
            "AUI Morocco": "https://www.aui.ma",
            "Hespress": "https://www.hespress.com", 
            "Avito Morocco": "https://www.avito.ma",
            "Google": "https://www.google.com",
            "LinkedIn": "https://www.linkedin.com",
            "GitHub": "https://github.com"
        }
        self.results_dir = "cloud_results"
        os.makedirs(self.results_dir, exist_ok=True)
    
    def check_website(self, name, url):
        """Enhanced website check with better error handling"""
        try:
            start = time.time()
            # Use realistic browser headers
            headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.5',
                'Accept-Encoding': 'gzip, deflate',
                'Connection': 'keep-alive',
            }
            
            response = requests.get(url, headers=headers, timeout=10)
            response_time = time.time() - start
            
            # 403 might mean site is up but blocking us - not necessarily DOWN
            status = "UP" if response.status_code < 400 else "BLOCKED"
            
            return {
                "name": name,
                "url": url,
                "status": status,
                "code": response.status_code,
                "time": round(response_time, 2),
                "timestamp": datetime.now().strftime("%H:%M:%S"),
                "size": len(response.content)
            }
        except requests.exceptions.Timeout:
            return {
                "name": name,
                "url": url,
                "status": "DOWN",
                "code": 0,
                "time": 0,
                "error": "Timeout after 10 seconds",
                "timestamp": datetime.now().strftime("%H:%M:%S")
            }
        except requests.exceptions.ConnectionError:
            return {
                "name": name,
                "url": url,
                "status": "DOWN",
                "code": 0,
                "time": 0,
                "error": "Connection failed",
                "timestamp": datetime.now().strftime("%H:%M:%S")
            }
        except Exception as e:
            return {
                "name": name,
                "url": url,
                "status": "DOWN",
                "code": 0,
                "time": 0,
                "error": str(e),
                "timestamp": datetime.now().strftime("%H:%M:%S")
            }
    
    def run_check(self):
        """Main function that runs everything"""
        print("\n" + "="*60)
        print("🇲🇦 MOROCCO WEBSITE MONITOR - ENHANCED CLOUD VERSION")
        print("📍 Location: Casablanca, Morocco (via GitHub Cloud)")
        print("⏰ Time:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        print("="*60)
        
        results = []
        
        print("\n🔍 Checking websites...")
        print("-"*60)
        
        for name, url in self.websites.items():
            result = self.check_website(name, url)
            results.append(result)
            
            # Show enhanced status
            if result["status"] == "UP":
                print(f"✅ {name:20} | UP      | {result['time']:5.2f}s | Code: {result['code']} | Size: {result.get('size', 0):,} bytes")
            elif result["status"] == "BLOCKED":
                print(f"⚠️  {name:20} | BLOCKED | {result['time']:5.2f}s | Code: {result['code']} | (Site blocking bots)")
            else:
                error = result.get('error', 'Unknown error')
                print(f"❌ {name:20} | DOWN    | --.--s | Error: {error[:30]}...")
        
        # Save to JSON file
        filename = f"monitor_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        filepath = os.path.join(self.results_dir, filename)
        
        report = {
            "metadata": {
                "project": "Morocco DevOps Monitor",
                "version": "2.0",
                "generated_at": datetime.now().isoformat(),
                "location": "GitHub Actions Cloud",
                "student": "AUI Morocco - DevOps Learning"
            },
            "summary": {
                "total_websites": len(results),
                "up": sum(1 for r in results if r["status"] == "UP"),
                "blocked": sum(1 for r in results if r["status"] == "BLOCKED"),
                "down": sum(1 for r in results if r["status"] == "DOWN"),
            },
            "results": results
        }
        
        with open(filepath, 'w') as f:
            json.dump(report, f, indent=2)
        
        print("\n" + "="*60)
        print("📊 REPORT GENERATED")
        print("="*60)
        
        up_count = sum(1 for r in results if r["status"] == "UP")
        blocked_count = sum(1 for r in results if r["status"] == "BLOCKED")
        total = len(results)
        
        print(f"\n📈 SUMMARY:")
        print(f"   ✅ UP:        {up_count}/{total}")
        print(f"   ⚠️  BLOCKED:  {blocked_count}/{total}")
        print(f"   ❌ DOWN:      {total - up_count - blocked_count}/{total}")
        print(f"\n📁 Results saved to: {filepath}")
        print("="*60)
        
        return report

if __name__ == "__main__":
    monitor = MoroccoWebsiteMonitor()
    monitor.run_check()
