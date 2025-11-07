# KDE Activity Launcher
A lightweight Python/Qt script to launch and switch KDE Plasma Activities easily.

## About
KDE Activity Launcher is a simple tool for managing KDE Plasma Activities from the command line or via custom shortcuts. While Plasma’s native Activities feature exists, this launcher makes it easy to script or hot-key different workflows — e.g., switch to a “Work” activity, “Gaming” activity, or “Presentation” activity with one command.

## Features
- Quickly list existing activities.
- Launch programs on a specific activity by name.
- Supports tiling between different activities with [polonium](https://github.com/zeroxoneafour/polonium)
- Configure custom mappings in a `config.json` for user-friendly names.
- Minimal dependencies: mostly Python + D-Bus interaction (via pydbus).
- Shell helper script included (`set-polonium.sh`) to integrate with KWinScripts.
- Compatible with Plasma environments where Activities are enabled.

## Installation
```bash
git clone https://github.com/al1c3-dev/KDE_Activity_Launcher.git
cd KDE_Activity_Launcher

# Optional: set up Python virtual environment
python3 -m venv venv
source venv/bin/activate

# From the directory containing setup.py
python3 setup.py install
```
Directions for installing polonium can be found [here](https://github.com/zeroxoneafour/polonium)



# Documentation

## Class: KDEActivityLauncher

`KDEActivityLauncher` manages KDE Plasma activities by launching configured processes and toggling a tiling window manager when activities change.


## Methods

### `__init__(self, targets)`
Initializes the activity launcher.

- **Parameters:**
  - `targets` (`dict`): Maps activity names or UUIDs to a tuple of process lists and tiler state.  
    Example: `{ "Work": (["firefox", "code"], True) }`

- **Behavior:**
  - Connects to KDE ActivityManager via DBus.
  - Tracks current activity.
  - Sets up a listener for activity changes.

---

### `set_tiler(enabled: bool)`
Toggles the tiling window manager state using an external script.

- **Parameters:**
  - `enabled` (`bool`): `True` to enable tiler, `False` to disable.

- **Behavior:**
  - Calls `./set-polonium.sh` with `true` or `false`.

---

### `read_activities(self, targets)`
Converts activity names to UUIDs and returns a dictionary for internal use.

- **Parameters:**
  - `targets` (`dict`): Mapping of activity names to process lists and tiler state.

- **Returns:**
  - `dict`: Mapping of activity UUIDs to their respective process list and tiler state.

---

### `get_activity_id_by_name(self, target_name: str) -> str | None`
Retrieves the UUID for a KDE activity by name.

- **Parameters:**
  - `target_name` (`str`): Name of the activity.

- **Returns:**
  - `str` or `None`: UUID if found, otherwise `None`.

---

### `get_activity(self, activity_id)`
Gets the configuration for a specific activity.

- **Parameters:**
  - `activity_id` (`str`): Activity UUID.

- **Returns:**
  - Tuple `[process_list, tiler_enabled]` corresponding to that activity.

---

### `on_activity_changed(self, new_activity)`
Callback invoked when the current KDE activity changes.

- **Parameters:**
  - `new_activity` (`str`): UUID of the new activity.

- **Behavior:**
  - Updates the current activity.
  - Toggles tiler according to configuration.
  - Launches processes configured for the activity.

---

### `cleanup(self, *args)`
Terminates all running subprocesses and exits the program.

- **Parameters:**
  - `*args`: Optional signal arguments.

- **Behavior:**
  - Iterates through all subprocesses started by the launcher and terminates them gracefully.
  - Calls `sys.exit(0)`.


