import subprocess
import signal
import sys
import time
from pydbus import SessionBus
from gi.repository import GLib




class KDEActivityLauncher:
    def __init__(self, targets):
        self.bus = SessionBus()
        self.activity_manager = self.bus.get("org.kde.ActivityManager", "/ActivityManager/Activities")
        self.current_activity = self.activity_manager.CurrentActivity
        self.processes = {}  # activity_id:[ [subprocesses] , bool tiler state]
        self.target_activities = self.read_activities(targets)

        print(f"Manager started on activity {self.current_activity}")
        self.activity_manager.CurrentActivityChanged.connect(self.on_activity_changed)

    def set_tiler(enabled: bool):
    subprocess.run(["./set-polonium.sh", str(enabled).lower()])

    def read_activities(self,targets):
        target_activities={}
        for key, value in targets.items():
            activity_id = self.get_activity_id_by_name(key) or key
            target_activities[activity_id] = value
        return target_activities

    def get_activity_id_by_name(self,target_name: str):
        uuids = subprocess.check_output(
            ["qdbus", "org.kde.ActivityManager", "/ActivityManager/Activities", "ListActivities"]).decode().splitlines()

        for uuid in uuids:
            name = subprocess.check_output(
                ["qdbus", "org.kde.ActivityManager", "/ActivityManager/Activities","org.kde.ActivityManager.Activities.ActivityName", uuid]
            ).decode().strip()

            if name == target_name:
                return uuid

        return None

    def get_activity(self, activity_id):

        return self.target_activities.get(activity_id, ([], False))

    def on_activity_changed(self, new_activity):

        print(f"Switched activity to {new_activity}")
        self.current_activity = new_activity

        process_list, tiler_enabled = self.get_activity(new_activity)

        set_tiler(tiler_enabled)

        if not process_list:
            print("No configured processes for this activity.")
            return

        if new_activity not in self.processes:
            self.processes.setdefault(new_activity, [])

            for process in process_list:
                print(f"Starting process: {process}")
                p = subprocess.Popen(process)
                self.processes[new_activity].append(p)


    def cleanup(self, *args):
        print("Cleaning up...")
        for plist in self.processes.values():
            for p in plist:
                if p.poll() is None:
                    p.terminate()
        sys.exit(0)























