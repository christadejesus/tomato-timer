# Tomato Timer

[Features](#features) | [Screenshots](#screenshots) | [Usage](#how-to-use) | [Customization](#for-developers-or-customization) | [Attributions](#attributions) | [Contact](#contact)

Tomato Timer is a user-friendly and enhanced version of a time-management tool inspired by the Pomodoro Technique. Originally a course project from the [100 Days of Code: The Complete Python Pro Bootcamp](https://www.udemy.com/course/100-days-of-code/) by Dr. Angela Yu, this version includes several custom changes and additional features for a more engaging experience.

Built with Python and Tkinter, Tomato Timer is packaged using ```PyInstaller```, allowing it to run conveniently as a standalone program on your desktop.

## Features

- **Work and Break Cycles:** Tomato Timer follows the basic structure of the Pomodoro technique with 25-minute work sessions, 5-minute short breaks, and a 20-minute long break after every 4 work sessions.

- **Visual Timer:** A dynamic display shows the time remaining during work or break sessions with large, clear numbers for easy tracking.

- **Session Count:** After each completed work session, a ✔ mark is added to track your progress.

### Enhanced Features

- **Audio Alerts:** Notification sounds play at the start of each work or break session (requires ```Pygame``` for sound functionality).
- **Enhanced Button Control:** The 'Start' button is disabled once clicked, preventing multiple clicks and ensuring the timer runs smoothly.
- **Styled Buttons:** Added support for ```ttk``` to introduce visually appealing, styled buttons with hover effects.
- **Custom Styling:** The user interface has been visually enhanced with unique fonts and vibrant colors to create a user-friendly experience.
- **Custom Graphics:** Designed a custom tomato graphic and icon to replace the default image, making the display more playful and engaging.
- **Convenient Packaging:** Packaged the program using ```PyInstaller``` to make it easy to launch directly from a desktop shortcut, without needing to manually run the Python script.

## Screenshots
|                |                     |
| -------------- | ------------------- |
| **At start:** | ![Tomato Timer Start Screenshot](/demo_images/tomato_timer_start_700.png) | 
| **Work session:** | ![Tomato Timer Work Screenshot](/demo_images/tomato_timer_work_700.png) |
| **Break session:** | ![Tomato Timer Break Screenshot](/demo_images/tomato_timer_break_700.png) |
| **At End:** | ![Tomato Timer End Screenshot](/demo_images/tomato_timer_end_700.png) |

## How to Use
### Running the Program
**1. Download the Executable:**

- Simply download the ```tomato_timer.exe``` file from the [Releases](https://github.com/christadejesus/tomato-timer/releases) section of the repository.

**2. Running the Timer:**

- Double-click the ```tomato_timer.exe``` file to launch the program from your desktop or file manager.

- The timer interface will open, and you can start using it immediately.

**3. Session Control:**

- Press the 'Start' button to begin your first work session.
- The timer will automatically switch between work and break sessions with sound notifications to keep you on track.

**4. Finishing a Set:**

- Following your final 20 minute break, the timer will stop. 
- Press the 'Reset' button to immediately begin a new set of sessions.

**5. Exiting the Program:**

- Close the window at any time to stop the timer and exit the program. 

## For Developers or Customization:

**1. Clone the Repository:**

- If you'd like to modify the code or customize the timer, clone the repository from GitHub:

```bash
git clone https://github.com/christadejesus/tomato-timer.git
```
**2. Install Dependencies:**

- Create and activate a virtual environment, then install the necessary dependencies:

```bash
pip install -r requirements.txt
```
**3. Run the Program:**

- You can run the program by executing the ```tomato_timer.py``` file in your terminal:

```bash
python tomato_timer.py
```
**4. Modifications:**

Feel free to modify the Python code, images, or sounds. Once you've made changes, you can repackage the program using ```PyInstaller``` (see the [Attributions](#attributions) section).


## Attributions

- **Sound Effects**: [floraphonic](https://pixabay.com/users/floraphonic-38928062) from [Pixabay](https://pixabay.com/sound-effects)
- **Project Inspiration**: [100 Days of Code: The Complete Python Pro Bootcamp](https://www.udemy.com/course/100-days-of-code/), Dr. Angela Yu
- **Pygame** 
  - [GitHub repo](https://github.com/pygame/pygame)
  -  License: [GNU LGPL version 2.1](https://www.gnu.org/licenses/lgpl-3.0.html)
- **PyInstaller**
  - [GitHub repo](https://github.com/pyinstaller/pyinstaller)
  - License: [GNU GPL](https://gnu.org/licenses/gpl-2.0.html)
- **Google Fonts**
  - [Pacifico](https://fonts.google.com/specimen/Pacifico)
  - [Poppins](https://fonts.google.com/Poppins)
  
## Contact

If you have any questions, suggestions, or want to contribute to this project, feel free to reach out:

Email: christa.tech@outlook.com

LinkedIn: [@christatech](https://www.linkedin.com/in/christatech)

GitHub: [github.com/christadejesus](https://github.com/christadejesus)