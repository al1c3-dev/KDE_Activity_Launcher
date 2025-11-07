from kdeactivitylauncher import KDEActivityLauncher
import signal
from gi.repository import GLib
import json
import os

CONFIG_FILE = "config.json"

def load_config():
    if not os.path.exists(CONFIG_FILE):
        raise FileNotFoundError(f"{CONFIG_FILE} not found.")

    with open(CONFIG_FILE, "r") as f:
        data = json.load(f)

    return data

def main():
    TARGET_ACTIVITIES = load_config()

    manager = KDEActivityLauncher(TARGET_ACTIVITIES)
    signal.signal(signal.SIGINT, manager.cleanup)
    signal.signal(signal.SIGTERM, manager.cleanup)
    loop = GLib.MainLoop()
    try:
        loop.run()
    except KeyboardInterrupt:
        manager.cleanup()


if __name__ == "__main__":
    main()
