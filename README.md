# Daily Mood Tracker & Journal
A clean and user-friendly web application built with **Flask** that allows users to log their daily mood and maintain a short journal entry. It also displays past entries to encourage reflection and mental well-being.\

## How It Works
The app presents a simple form where users can:
- Select their current mood from a dropdown
- Write a short journal entry describing their day
- View a chronological list of past entries below the form
Each journal entry is saved with a timestamp and displayed with the selected mood.

## Tech Stack
- Python 3
- Flask
- HTML, CSS (for frontend styling)
- (Optional) JSON or text files for data storage

# Repository Structure
```plaintext
daily-mood-tracker/
├── app.py                             # Main Flask application
├── templates/
│   └── index.html                     # HTML template for UI
├── static/                            # Folder for CSS or assets (if used)
├── mood_log.txt / data.json           # File used to store entries
├── Daily_Mood_Tracker_with_Journal_(using_Flask).ipynb  # Notebook version
└── README.md
```

# Try It Locally
1. Clone the Repository
```bash
git clone https://github.com/your-username/daily-mood-tracker.git
cd daily-mood-tracker
```
2. Install Requirements
```bash
pip install flask
```
3. Run the Application
```bash
python app.py
```
Visit http://127.0.0.1:5000 in your browser to use the app.

## Explore via Jupyter Notebook
If you'd like to understand the logic in a more educational format, open:

```bash
Daily_Mood_Tracker_with_Journal_(using_Flask).ipynb
```
You can run this notebook in Google Colab or your local Jupyter environment.

## Features Displayed in the UI
- Dropdown mood selection (e.g., Happy, Angry)
- Free-text journal entry
- "Save Entry" button
- Your Past Entries section showing:
  - Mood with emoji
  - Timestamp
  - Journal text in card format

## Screenshot
Below is a screenshot of the app in action:
![Screenshot 2025-07-09 101641](https://github.com/user-attachments/assets/bd9465b5-3d2e-42a1-bddf-0a70a432e83d)
