# Government Shutdown Board

A **Government Shutdown Board** for the [NHL LED Scoreboard](https://github.com/falkyre/nhl-led-scoreboard) that displays elapsed time since the government shutdown started on October 1, 2025 at 12:01 AM.

The board shows days, hours, minutes, and seconds that have elapsed since the shutdown began, updating every second.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Configuration](#configuration)
- [How It Works](#how-it-works)

---

## Features

- Real-time countdown showing elapsed time since October 1, 2025 at 12:01 AM
- Displays days, hours, minutes, and seconds
- Updates every second for accurate time tracking
- Customizable colors for text and title
- Configurable display duration
- Supports both 64x32 and 128x64 LED matrix sizes

---

## Installation

1. Use the NHL Led Scoreboard's plugin manager python script to install:

   ```bash
   python plugins.py add https://github.com/kas21/nls-plugin-government-shutdown-board.git
   ```

2. Add `government_shutdown_board` to your NHL-LED-Scoreboard's main configuration:

   ```bash
   nano config/config.json
   ```

   For example, to add it to the off day rotation:

   ```json
   "states": {
       "off_day": [
           "season_countdown",
           "government_shutdown_board",
           "team_summary",
           "scoreticker",
           "clock"
       ]
   }
   ```

   **Note:** You must restart the scoreboard for changes to take effect.

---

## Configuration

To customize the `government_shutdown_board` configuration, copy the sample config to config.json and edit it.

```bash
cp config.sample.json config.json
nano config.json
```

**Note:** You must restart the scoreboard for changes to take effect.

### Config Fields

- `display_seconds` → Number of seconds to display the board before cycling (default: 10)
- `fg_color` → Foreground color for elapsed time numbers in hex format (default: `"#FF0000"` - red)
- `title_color` → Color for title and labels in hex format (default: `"#FFFFFF"` - white)
- `enabled` → Enable or disable the board (default: true)

### Example Configuration

```json
{
    "display_seconds": 10,
    "fg_color": "#FF0000",
    "title_color": "#FFFFFF",
    "enabled": true
}
```

---

## How It Works

1. The board calculates elapsed time from October 1, 2025 at 12:01 AM to the current time
2. Time is broken down into days, hours, minutes, and seconds
3. The display shows:
   - "SHUTDOWN" title at the top
   - Four columns displaying: DAYS, HRS, MIN, SEC
   - Each column shows the numeric value with its label
4. The board updates every second to keep the seconds counter accurate
5. Display loops continuously while in the active state

### Example Display

```
      SHUTDOWN
  35  12  45  23
 DAYS HRS MIN SEC
```

Where:
- 35 days have elapsed
- Plus 12 hours
- Plus 45 minutes
- Plus 23 seconds

---

## License

This plugin follows the same license as the NHL LED Scoreboard project.
