import requests
import time
from datetime import datetime
import os


def check_website(url, name):
    """Check if a website is accessible"""
    try:
        start_time = time.time()
        response = requests.get(
            url, timeout=10, headers={"User-Agent": "Morocco-DevOps-Monitor/1.0"}
        )
        elapsed_time = time.time() - start_time

        if response.status_code == 200:
            return (
                f"🌐 {name}: ✅ UP ({elapsed_time:.2f}s) [{response.status_code}]",
                True,
            )
        else:
            return (
                f"🌐 {name}: ⚠️ STATUS {response.status_code} ({elapsed_time:.2f}s)",
                False,
            )
    except requests.exceptions.RequestException as e:
        return f"🌐 {name}: ❌ ERROR: {str(e)[:50]}", False


def main():
    """Main monitoring function"""
    websites = {
        "AUI.ma": "https://www.aui.ma",
        "Hespress.com": "https://www.hespress.com",
        "Avito.ma": "https://www.avito.ma",
        "Google.com": "https://www.google.com",
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
    print(f"📊 SUMMARY: {up_count}/{len(websites)} websites accessible")
    print(f"⏰ Check time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("─" * 50)

    # Save to file - try Docker path first, then local
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Try Docker path first
    results_dir = "/app/results"
    if not os.path.exists(results_dir):
        # Fall back to local path
        results_dir = "docker_results"

    os.makedirs(results_dir, exist_ok=True)
    filename = f"{results_dir}/check_{timestamp}.txt"

    with open(filename, "w") as f:
        f.write("\n" + "🔄" * 10 + "\n")
        f.write("   MOROCCAN WEBSITE MONITOR\n")
        f.write("🔄" * 10 + "\n\n")

        for status in results:
            f.write(status + "\n")

        f.write("\n" + "─" * 50 + "\n")
        f.write(f"📊 SUMMARY: {up_count}/{len(websites)} websites accessible\n")
        f.write(f"⏰ Check time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("─" * 50 + "\n")
        f.write(f"💾 Results saved to: {filename}\n")

    print(f"💾 Results saved to: {filename}")


if __name__ == "__main__":
    main()
