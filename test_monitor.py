import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from advanced_monitor import MoroccoWebsiteMonitor


def test_websites_list_not_empty():
    monitor = MoroccoWebsiteMonitor()
    assert len(monitor.websites) > 0


def test_websites_count():
    monitor = MoroccoWebsiteMonitor()
    assert len(monitor.websites) == 6


def test_websites_have_valid_urls():
    monitor = MoroccoWebsiteMonitor()
    for name, url in monitor.websites.items():
        assert url.startswith("https://"), f"{name} URL does not start with https://"


def test_classify_status_up():
    monitor = MoroccoWebsiteMonitor()
    assert monitor.classify_status(200) == "UP"
    assert monitor.classify_status(301) == "UP"
    assert monitor.classify_status(302) == "UP"


def test_classify_status_blocked():
    monitor = MoroccoWebsiteMonitor()
    assert monitor.classify_status(403) == "BLOCKED"
    assert monitor.classify_status(404) == "BLOCKED"
    assert monitor.classify_status(500) == "BLOCKED"
    assert monitor.classify_status(503) == "BLOCKED"


def test_classify_status_down():
    monitor = MoroccoWebsiteMonitor()
    assert monitor.classify_status(0) == "DOWN"
