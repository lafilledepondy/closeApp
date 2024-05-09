# Countdown and Close Telegram Script

This Python script displays a countdown window using Tkinter before terminating the Telegram process.

## Requirements
* Python: Ensure you have Python 3.x installed on your system.

* Tkinter Library: The script utilizes Tkinter for creating the countdown window.Or else run this command in a terminal: 

    `pip install tk`

* pgrep Utility: This script uses the pgrep utility, typically available on Unix-like systems, to find the process ID (PID) of the Telegram application.

## Usage
1. Modify Process Name: Open the script and modify the process_name variable in the main function to match the name of the process you want to terminate (e.g., "telegram").

2. Run the Script: 
    
    `./run.sh`

3. Countdown Window:
    * A Tkinter window titled "Tata" will appear with a countdown displayed in a large font.
    
    * The countdown starts from 3 and decrements by 1 every second.

4. Process Termination:
After the countdown finishes, the script will attempt to terminate the specified process (e.g., "telegram") using its process ID (PID).

## Notes:
* Ensure the specified process name matches the actual process name of the application you want to terminate.

* The script uses system commands (pgrep and kill) and is designed for Unix-like systems. Adjustments may be needed for other operating systems.

* Adjust the w and h variables to customize the size of the countdown window (w = width, h = height).

* You can uncomment and modify the 
    
        time.sleep(3)
        subprocess.Popen([f"{process_name}"])
    lines to add further actions after process termination.
