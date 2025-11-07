#!/bin/bash

CONF="$HOME/.config/kwinrc"
KEY="poloniumEnabled"
STATE="$1"

if [[ "$STATE" != "true" && "$STATE" != "false" ]]; then
    echo "Usage: $0 [true|false]"
    exit 1
fi

echo "Setting Polonium to $STATE..."
kwriteconfig5 --file kwinrc --group Plugins --key "$KEY" "$STATE"

# Reload KWin
qdbus org.kde.KWin /KWin reconfigure
