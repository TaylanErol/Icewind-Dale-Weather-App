import customtkinter as ctk
import tkinter as tk
import random
from PIL import Image
import tkinter.font as tkFont



# Full descriptions for weather events
weather_events = {
    1: ("Clear Skies", "2d4", [
        ("a) ", "bold"), ("[No Wind] ", "italic"), ("-50°F\n", "normal"),
        ("b) Dim Natural Light from: ", "bold"), ("½ Moon / Aurora / Twilight\n", "underline"),
        ("   i) Disadvantage on ", "normal"), ("[Sight] ", "bold"), ("Perception Checks.", "normal")
    ]),
    2: ("Light Cloud Coverage", "1d4", [
        ("a) ", "bold"), ("[Mild Wind] ", "italic"), ("-55°F\n", "normal"),
        ("b) Dim Natural Light from: ", "bold"), ("¾ Moon / Aurora / Twilight\n", "underline"),
        ("   i) Disadvantage on ", "normal"), ("[Sight] ", "bold"), ("Perception Checks.", "normal")
    ]),
    3: ("Overcast", "1d4", [
        ("a) ", "bold"), ("[Moderate Wind] ", "italic"), ("-65°F\n", "normal"),
        ("   i) Disadvantage on Ranged Attack Rolls\n", "normal"),
        ("b) No Natural Light: ", "bold"), ("[Blinded]\n", "italic"),
        ("   i) No ", "normal"), ("[Sight] ", "bold"), ("Perception Checks\n", "normal"),
        ("   ii) Disadvantage on Attack Rolls.", "normal")
    ]),
    4: ("Storm Clouds", "1d4", [
        ("a) ", "bold"), ("[Severe Wind] ", "italic"), ("-80°F\n", "normal"),
        ("   i) Disadvantage on Ranged Attack Rolls\n", "normal"),
        ("   ii) Disadvantage on ", "normal"), ("[Hearing] ", "bold"), ("Perception Checks\n", "normal"),
        ("b) No Natural Light: ", "bold"), ("[Blinded]\n", "italic"),
        ("   i) No ", "normal"), ("[Sight] ", "bold"), ("Perception Checks\n", "normal"),
        ("   ii) Disadvantage on Attack Rolls\n", "normal"),
        ("c) Extreme Cold for those without natural cold resistance:\n", "bold"),
        ("   i) 1/Hr DC 10 CON Saving Throw: ", "normal"), ("On Fail +1 Exhaustion.", "italic")
    ]),
    5: ("Light Snow Dusting", "1d4", [
        ("a) ", "bold"), ("[No Wind] ", "italic"), ("-60°F\n", "normal"),
        ("b) Dim Natural Light from: ", "bold"), ("Full Moon / Aurora / Twilight\n", "underline"),
        ("   i) Disadvantage on ", "normal"), ("[Sight] ", "bold"), ("Perception Checks.", "normal")
    ]),
    6: ("Heavy Snowfall", "1d4", [
        ("a) ", "bold"), ("[Mild Wind] ", "italic"), ("-70°F\n", "normal"),
        ("b) No Natural Light: ", "bold"), ("[Blinded]\n", "italic"),
        ("   i) No ", "normal"), ("[Sight] ", "bold"), ("Perception Checks\n", "normal"),
        ("   ii) Disadvantage on Attack Rolls\n", "normal"),
        ("c) Extreme Cold for those without cold resistance:\n", "bold"),
        ("   i) 1/Hr DC 10 CON Saving Throw: ", "normal"), ("Fail +1 Exhaustion.", "italic")
    ]),
    7: ("Blizzard", "2d4", [
        ("a) ", "bold"), ("[Moderate Wind] ", "italic"), ("-90°F\n", "normal"),
        ("   i) Disadvantage on Ranged Attack Rolls\n", "normal"),
        ("   ii) Disadvantage on ", "normal"), ("[Hearing] ", "bold"), ("Perception Checks (Hearing Range Reduced to 100ft)\n", "italic"),
        ("b) No Natural Light: ", "bold"), ("[Blinded]\n", "italic"),
        ("   i) No ", "normal"), ("[Sight] ", "bold"), ("Perception Checks\n", "normal"),
        ("   ii) Disadvantage on Attack Rolls\n", "normal"),
        ("   iii) Visibility from Unnatural Lights Reduced to 30ft.\n", "italic"),
        ("c) Extreme Cold for those without cold resistance:\n", "bold"),
        ("   i) 1/Hr DC 10 CON Saving Throw: ", "normal"), ("Fail +1 Exhaustion\n", "italic"),
        ("d) Extinguishing Winds: ", "bold"), ("Makes open flames, fog, tracks in the snow, and non-magical flying impossible.\n", "normal"),
        ("e) Veering off course - If the party travels during a blizzard:\n", "bold"),
        ("   i) Navigator must make a 1/Hr DC 15 Survival check:\n", "normal"),
        ("      ● On Fail 14-10: Party makes no progress.\n", "normal"),
        ("      ● On Fail 9 or lower: One random untied party member is lost.\n", "normal"),
        ("      ● Group DC 15 Survival Check 1/hr to find the lost member.\n", "normal"),
        ("f) On turn end: ", "bold"), ("Concentration Spells require DC 10 CON Saving Throw to maintain.", "italic")
    ]),
    8: ("White Out", "1d4", [
        ("a) ", "bold"), ("[Severe Wind] ", "italic"), ("-130°F\n", "normal"),
        ("   i) Disadvantage on Ranged Attack Rolls\n", "normal"),
        ("   ii) Disadvantage on ", "normal"), ("[Hearing] ", "bold"), ("Perception Checks (Hearing Range Reduced to 30ft)\n", "italic"),
        ("b) No Natural Light: ", "bold"), ("[Blinded]\n", "italic"),
        ("   i) No ", "normal"), ("[Sight] ", "bold"), ("Perception Checks\n", "normal"),
        ("   ii) Disadvantage on Attack Rolls\n", "normal"),
        ("   iii) Visibility from Unnatural Lights Reduced to 10ft.\n", "italic"),
        ("c) Extreme Cold:\n", "bold"),
        ("   i) With Cold Resist: 1/Hr DC 10 CON Saving Throw: ", "normal"), ("Fail +1 Exhaustion\n", "italic"),
        ("   ii) No Cold Resist: 1/Hr DC 15 CON Saving Throw: ", "normal"), ("Fail +1 Exhaustion\n", "italic"),
        ("d) Extinguishing Winds: ", "bold"), ("Makes open flames, fog, tracks in the snow, and non-magical flying impossible.\n", "normal"),
        ("e) Veering off course - If the party travels during a white out:\n", "bold"),
        ("   i) Navigator must make a 1/Hr DC 18 Survival check:\n", "normal"),
        ("      ● On Fail 17-15: Party makes no progress.\n", "normal"),
        ("      ● On Fail 14-10: One random untied party member is lost.\n", "normal"),
        ("      ● On Fail 9 or lower: One random tied party member is lost.\n", "normal"),
        ("      ● Group DC 18 Survival Check 1/hr to find the lost member.\n", "normal"),
        ("f) On turn end: ", "bold"), ("Concentration Spells require DC 10 CON Saving Throw to maintain.", "italic")
    ]),
    9: ("Extreme Fog", "1d4", [
        ("a) ", "bold"), ("[No Wind] ", "italic"), ("-55°F\n", "normal"),
        ("b) Dim Natural Light from: ", "bold"), ("Full Moon / Aurora / Twilight\n", "underline"),
        ("   i) Disadvantage on ", "normal"), ("[Sight] ", "bold"), ("Perception Checks\n", "normal"),
        ("   ii) Visibility from Unnatural Lights Reduced to 5ft.\n", "italic"),
        ("c) Veering off course - If the party travels during the extreme fog:\n", "bold"),
        ("   i) Navigator must make a 1/Hr DC 12 Survival check:\n", "normal"),
        ("      ● On Fail 11-8: Party makes no progress.\n", "normal"),
        ("      ● On Fail 7 or lower: One random untied party member is lost.\n", "normal"),
        ("      ● Group DC 12 Survival Check 1/hr to find the lost member.", "normal")
    ]),
    10: ("Lightning Storm", "2d4", [
        ("a) ", "bold"), ("[Mild Wind] ", "italic"), ("-60°F\n", "normal"),
        ("b) Dim Natural Light from: ", "bold"), ("Rapid Lightning\n", "underline"),
        ("   i) Disadvantage on ", "normal"), ("[Sight] ", "bold"), ("Perception Checks\n", "normal"),
        ("c) Frightening Lightning / Thunderous Threat:\n", "bold"),
        ("   i) 1/Hr Players caught in the open tundra must roll a d100:\n", "normal"),
        ("      ● On 001: The character must make a DC 15 DEX Saving Throw:\n", "normal"),
        ("        Fail: 8d8 lightning damage / Half on a success.\n", "italic"),
        (
        "      ● Each creature within 15ft of the striking point must also make a DC 15 DEX Saving Throw:\n", "normal"),
        ("        Fail: ½ the full damage. Save: No Damage.\n", "italic"),
        ("   ii) 1/Hr Booming Thunder has a 50% chance to cause an avalanche in the mountains.\n", "normal"),
        ("      ● Disadvantage on ", "normal"), ("[Hearing] ", "bold"), ("Perception Checks.", "normal")
    ]),
    11: ("Hail Storm", "1d4", [
        ("a) ", "bold"), ("[Severe Wind] ", "italic"), ("-80°F\n", "normal"),
        ("   i) Disadvantage on Ranged Attack Rolls\n", "normal"),
        ("   ii) Disadvantage on ", "normal"), ("[Hearing] ", "bold"), ("Perception Checks\n", "normal"),
        ("b) No Natural Light: ", "bold"), ("[Blinded]\n", "italic"),
        ("   i) No ", "normal"), ("[Sight] ", "bold"), ("Perception Checks\n", "normal"),
        ("   ii) Disadvantage on Attack Rolls\n", "normal"),
        ("c) Extreme Cold for those without cold resistance:\n", "bold"),
        ("   i) 1/Hr DC 10 CON Saving Throw: ", "normal"), ("On Fail +1 Exhaustion.\n", "italic"),
        ("d) Icey Monstrosity:\n", "bold"),
        ("   i) 1/Hr DC 10 DEX Saving Throw: ", "normal"), ("Fail 1d12 Bludgeoning or half on a success.", "italic")
    ]),
    12: ("Wind Vortex", "1d4", [
        ("a) ", "bold"), ("[Severe Wind] ", "italic"), ("-110°F\n", "normal"),
        ("   i) Disadvantage on Ranged Attack Rolls\n", "normal"),
        ("   ii) Disadvantage on ", "normal"), ("[Hearing] ", "bold"), ("Perception Checks\n", "normal"),
        ("b) Dim Natural Light from: ", "bold"), ("½ Moon / Aurora / Twilight\n", "underline"),
        ("   i) Disadvantage on ", "normal"), ("[Sight] ", "bold"), ("Perception Checks\n", "normal"),
        ("c) Extreme Cold for those with natural cold resistance:\n", "bold"),
        ("   i) With Cold Resist: 1/Hr DC 10 CON Saving Throw: ", "normal"), ("Fail +1 Exhaustion\n", "italic"),
        ("   ii) No Cold Resist: 1/Hr DC 15 CON Saving Throw: ", "normal"), ("Fail +1 Exhaustion\n", "italic"),
        ("d) Extinguishing Winds: ", "bold"),
        ("The severe wind makes open flames, fog, tracks in the snow, and non-magical flying impossible.", "normal")
    ])
}

# Weather progression mapping
weather_progression = {
    1: [(2, 4, 2), (5, 6, 5), (7, 8, 9)],
    2: [(1, 2, 1), (3, 3, 3), (4, 4, 5)],
    3: [(1, 2, 2), (3, 3, 4), (4, 4, 11)],
    4: [(1, 2, 3), (3, 3, 6), (4, 4, 10)],
    5: [(1, 2, 2), (3, 3, 6), (4, 4, 10)],
    6: [(1, 2, 3), (3, 3, 7), (4, 4, 11)],
    7: [(2, 4, 4), (5, 6, 6), (7, 8, 8)],
    8: [(1, 2, 5), (3, 3, 6), (4, 4, 7)],
    9: [(1, 2, 1), (3, 3, 5), (4, 4, 12)],
    10: [(2, 4, 4), (5, 6, 5), (7, 8, 6)],
    11: [(1, 2, 3), (3, 3, 6), (4, 4, 7)],
    12: [(1, 4, 1)]  # Wind Vortex always improves to Clear Skies
}

current_weather = {"event": None, "duration": 0}

# Mapping of weather events to colors for the visual bar
weather_colors = {
    1: "#1E90FF",  # Clear Skies - Dodger Blue
    2: "#87CEFA",  # Light Cloud Coverage - Light Sky Blue
    3: "#B0C4DE",  # Overcast - Light Steel Blue
    4: "#708090",  # Storm Clouds - Slate Gray
    5: "#ADD8E6",  # Light Snow Dusting - Light Blue
    6: "#FFFFFF",  # Heavy Snowfall - White
    7: "#F0FFFF",  # Blizzard - Azure
    8: "#E0FFFF",  # White Out - Light Cyan
    9: "#F5F5F5",  # Extreme Fog - White Smoke
    10:"#FFA07A",  # Lightning Storm - Light Salmon
    11:"#A9A9A9",  # Hail Storm - Dark Gray
    12:"#2F4F4F",  # Wind Vortex - Dark Slate Gray
}

# Initialize weather schedule and current hour
weather_schedule = []
current_hour = 0

# Constants for the weather bar dimensions
BAR_WIDTH = 600  # Width of the bar in pixels
BAR_HEIGHT = 50  # Height of the bar in pixels

def roll_dice(dice_sides):
    return random.randint(1, dice_sides)

def roll_multiple_dice(dice_notation):
    count, sides = map(int, dice_notation.lower().split("d"))
    return sum(roll_dice(sides) for _ in range(count))

def apply_rich_text(widget, content):
    """Insert rich text into a Text widget based on tags."""
    widget.configure(state="normal")
    widget.delete("1.0", "end")
    for text, tag in content:
        widget.insert("end", text, tag)
    widget.configure(state="disabled")

def new_day():
    """Generate a 24-hour weather schedule based on dynamic progression."""
    global weather_schedule, current_hour
    weather_schedule = []
    current_hour = 0

    # Generate initial weather event by rolling a d12
    event_id = roll_dice(12)

    total_hours = 0

    while total_hours < 24:
        # Fetch details of the current weather event
        event, duration_notation, description = weather_events[event_id]
        duration_roll = roll_multiple_dice(duration_notation)  # Roll for event duration
        duration = duration_roll  # The duration is the total of the dice rolled

        hours_remaining = 24 - total_hours
        event_duration = min(duration, hours_remaining)  # Constrain duration to fit the day

        # Add the current weather event to the schedule
        for _ in range(event_duration):
            weather_schedule.append({
                'event_id': event_id,
                'event': event,
                'description': description
            })

        total_hours += event_duration

        if total_hours >= 24:
            break

        # Progress to the next weather event based on duration_roll
        progression = weather_progression.get(event_id, [])
        next_event_id = None

        # Determine the next weather event based on progression rules
        for start, end, next_event in progression:
            if start <= duration_roll <= end:
                next_event_id = next_event
                break

        # Default to Clear Skies if no progression found
        if next_event_id is None:
            next_event_id = 1

        # Update for the next iteration
        event_id = next_event_id

    # Update the display and bar
    draw_weather_bar()
    update_weather_display()

def progress_hour():
    """Advance the current hour by 1 and update display."""
    global current_hour
    if not weather_schedule:
        return  # Do nothing if schedule is empty
    current_hour = (current_hour + 1) % 24
    update_pointer()
    update_weather_display()

def update_weather_display():
    """Update the weather information display."""
    if not weather_schedule:
        return
    weather_event = weather_schedule[current_hour]
    event = weather_event['event']
    description = weather_event['description']

    weather_text.configure(state="normal")
    weather_text.delete("1.0", "end")
    apply_rich_text(weather_text, [
        (f"Hour {current_hour}: Weather Event: {event}\n\n", "title"),
    ] + description)
    weather_text.configure(state="disabled")

    # Adjust window size based on text content
    app.after(100, adjust_window_size)

def adjust_window_size():
    """Adjust the window size based on the content of the weather_text widget."""
    # Get the number of lines in the text widget
    num_lines = int(float(weather_text.index('end-1c').split('.')[0]))

    # Get the font size using tkinter.font
    font = tkFont.Font(font=weather_text['font'])
    line_height = font.metrics('linespace')  # Use the actual line height
    required_text_height = num_lines * line_height

    # Calculate the total required height of the window
    # Add heights of other widgets and padding
    total_required_height = (
        weather_label.winfo_reqheight() +
        weather_canvas.winfo_reqheight() +
        required_text_height +
        button_frame.winfo_reqheight() +
        150  # Additional padding and margins
    )

    # Get the current window width
    window_width = app.winfo_width()

    # Set minimum and maximum window height
    min_height = 500
    max_height = 1000

    # Adjust total height within bounds
    total_required_height = max(min_height, min(int(total_required_height), max_height))

    # Resize the window
    app.geometry(f"{window_width}x{total_required_height}")

def draw_weather_bar():
    """Draw the 24-hour weather bar with different colors."""
    weather_canvas.delete("all")

    hour_width = BAR_WIDTH / 24

    for hour in range(24):
        x0 = hour * hour_width
        y0 = 0
        x1 = x0 + hour_width
        y1 = BAR_HEIGHT

        event_id = weather_schedule[hour]['event_id']
        color = weather_colors.get(event_id, "#000000")  # Default to black

        weather_canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline="")

    # Draw the initial pointer
    update_pointer()

def update_pointer():
    """Update the pointer to indicate the current hour."""
    weather_canvas.delete("pointer")
    hour_width = BAR_WIDTH / 24

    x0 = current_hour * hour_width
    x1 = x0 + hour_width
    y0 = 0
    y1 = BAR_HEIGHT

    # Draw a red outline rectangle to indicate current hour
    weather_canvas.create_rectangle(
        x0, y0, x1, y1, outline="red", width=3, tags="pointer"
    )

def on_canvas_click(event):
    """Handle click events on the weather bar to update the current hour."""
    global current_hour
    x = event.x
    # Calculate which hour was clicked
    hour_width = BAR_WIDTH / 24
    clicked_hour = int(x // hour_width)
    # Ensure the hour is within 0-23
    clicked_hour = max(0, min(clicked_hour, 23))
    current_hour = clicked_hour
    update_pointer()
    update_weather_display()

# Initialize CustomTkinter with custom colors
ctk.set_appearance_mode("Dark")  # Can be "Dark" or "Light"

# Define custom colors for the theme
BACKGROUND_COLOR = "#1E1E2F"  # Dark Slate Blue
PRIMARY_COLOR = "#4B9CD3"     # Icy Blue
SECONDARY_COLOR = "#A9A9B0"   # Light Gray
TEXT_COLOR = "#FFFFFF"        # White
ACCENT_COLOR = "#1B3B6F"      # Deep Blue

# Main Application
app = ctk.CTk()
app.title("Icewind Dale Weather Helper")
app.geometry("700x700")  # Initial size
app.minsize(700, 500)    # Set minimum size

# Set window background color
app.configure(fg_color=BACKGROUND_COLOR)

# Set window icon using .ico file
app.iconbitmap("auril.ico")  # Ensure you have auril.ico in the same directory

# Configure the grid
app.grid_rowconfigure(0, weight=0)  # Spacer
app.grid_rowconfigure(1, weight=0)  # Weather Label
app.grid_rowconfigure(2, weight=0)  # Weather Bar Canvas
app.grid_rowconfigure(3, weight=1)  # Weather Text
app.grid_rowconfigure(4, weight=0)  # Buttons
app.grid_columnconfigure(0, weight=1)

# Weather Display Label
weather_label = ctk.CTkLabel(
    app,
    text="Weather Information",
    font=("Trebuchet MS", 18, "bold"),
    text_color=TEXT_COLOR
)
weather_label.grid(row=1, column=0, pady=10, sticky="n")

# Weather Bar Canvas
weather_canvas = tk.Canvas(
    app, width=BAR_WIDTH, height=BAR_HEIGHT, bg=BACKGROUND_COLOR, highlightthickness=0
)
weather_canvas.grid(row=2, column=0, pady=5, sticky="n")

# Bind click event to the canvas
weather_canvas.bind("<Button-1>", on_canvas_click)

# Use a standard tk.Text widget for rich text capabilities
weather_text = tk.Text(
    app,
    wrap="word",
    font=("Trebuchet MS", 12),
    bg=BACKGROUND_COLOR,     # Set background to match window background
    fg=TEXT_COLOR,
    insertbackground=TEXT_COLOR,
    highlightthickness=0,
    bd=0
)
weather_text.grid(row=3, column=0, pady=5, sticky="nsew")
weather_text.configure(state="disabled")



# Define rich text tags
weather_text.tag_configure("title", font=("Trebuchet MS", 14, "bold"), foreground=PRIMARY_COLOR)
weather_text.tag_configure("subtitle", font=("Trebuchet MS", 12, "italic"), foreground=SECONDARY_COLOR)
weather_text.tag_configure("bold", font=("Trebuchet MS", 12, "bold"), foreground=TEXT_COLOR)
weather_text.tag_configure("italic", font=("Trebuchet MS", 12, "italic"), foreground=TEXT_COLOR)
weather_text.tag_configure("underline", font=("Trebuchet MS", 12, "underline"), foreground=TEXT_COLOR)
weather_text.tag_configure("normal", font=("Trebuchet MS", 12), foreground=TEXT_COLOR)

# Buttons
button_frame = ctk.CTkFrame(app, fg_color=BACKGROUND_COLOR)
button_frame.grid(row=4, column=0, pady=10)

button_style = {
    "font": ("Trebuchet MS", 12, "bold"),
    "text_color": TEXT_COLOR,
    "fg_color": ACCENT_COLOR,      # Use ACCENT_COLOR for buttons
    "hover_color": PRIMARY_COLOR,  # Hover color to PRIMARY_COLOR
    "corner_radius": 8,            # Add rounded corners
    "border_width": 0              # Remove border for cleaner look
}

new_day_button = ctk.CTkButton(
    button_frame,
    text="New Day",
    command=new_day,
    **button_style
)
new_day_button.pack(side="left", padx=10)

#
# progress_hour_button = ctk.CTkButton(
#     button_frame,
#     text="Progress Hour",
#     command=progress_hour,
#     **button_style
# )
#progress_hour_button.pack(side="left", padx=10)

# Run Application
app.mainloop()