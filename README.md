# Icewind Dale Weather Helper

The **Icewind Dale Weather Helper** is a GUI-based tool designed to manage and track weather events in the Icewind Dale setting for tabletop RPG campaigns. It generates dynamic weather schedules, displays detailed descriptions of weather events, and provides an interactive weather bar for tracking the current hour.

---

## Features

- **Dynamic Weather Progression**:
  - Automatically generates a 24-hour weather schedule based on dice rolls.
  - Implements logical progression between weather events.

- **Interactive Weather Bar**:
  - Visual representation of weather for the entire day.
  - Clickable bar allows quick navigation to specific hours.

- **Detailed Weather Descriptions**:
  - Displays weather effects, penalties, and flavor text for each event.

- **Rich Text Support**:
  - Styled descriptions with bold, italic, and underlined text.

- **Customizable UI**:
  - Modern aesthetics using `CustomTkinter`.
  - Dark mode support with icy blue accents.

---

## Installation

### Prerequisites
- Python 3.8+
- The following Python libraries must be installed:
  - `customtkinter`
  - `tkinter` (included with Python)
  - `Pillow`

Install the required libraries with:
```bash
pip install customtkinter Pillow
```

### Running the Application
1. Clone or download the repository.
2. Ensure the `auril.ico` file is in the `Images` directory.
3. Run the `main.py` script:
   ```bash
   python main.py
   ```

### Packaging the Application
To create a standalone executable:
1. Install `PyInstaller`:
   ```bash
   pip install pyinstaller
   ```
2. Build the executable:
   ```bash
   pyinstaller --onefile --noconsole --icon=Images/auril.ico --add-data "Images/auril.ico;Images" main.py
   ```
3. The executable will be located in the `dist` folder.

---

## Usage

1. Launch the application.
2. Click **New Day** to generate a new weather schedule.
3. Use the **interactive weather bar** to view weather details for specific hours.
4. The application automatically adjusts the UI size for readability.

---

## Known Issues
Window Resizing Bug:
When the system screen scaling (DPI settings) is set to anything other than 100%, the window size gradually grows each time it is re-rendered (e.g., when changing the displayed weather).
Workaround: Set screen scaling to 100% in your display settings to avoid this issue.

---

## Attribution

The core logic for the weather progression system was inspired by a post on Reddit:
- [DMAcademy - Weather Events and Effects Tracker](https://www.reddit.com/r/DMAcademy/comments/j1148q/i_created_a_weather_events_and_effects_tracker/) by **Jee_Day_Eye**. Special thanks to them for their brilliant idea!

---

## Folder Structure
```
IcewindDaleWeatherHelper/
│
├── main.py               # Main script
├── Images/
│   └── auril.ico         # Icon file
└── README.md             # Project documentation
```

---

## License

This project is free to use and modify. Credit to **Jee_Day_Eye** for the original weather tracking logic.

---

## Notes

- Ensure the `auril.ico` file is in the correct location to avoid errors during runtime.
- For issues with the `.ico` file in standalone executables, ensure it is included using the `--add-data` flag with `PyInstaller`.

Happy adventuring in the frozen lands of Icewind Dale!


This `README.md` covers all essential details, including features, installation, usage, and attribution. Let me know if you'd like any changes!
