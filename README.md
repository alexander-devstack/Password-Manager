# MyPass – Local Password Manager (Tkinter)

MyPass is a simple local password manager built with Python and Tkinter. It generates strong random passwords, lets you associate them with a website and email/username, and saves everything to a local `data.json` file instead of relying on a third‑party cloud service.[file:372][file:370][file:371]

> Note: This is a learning project and is **not** intended as a production‑grade secure password manager. It demonstrates GUI design, password generation, JSON file handling, error handling, and clipboard usage in Python.[file:372]

---

## Features

- Generate random passwords using letters, numbers, and symbols with one click.[file:372]  
- Automatically copy generated passwords to the clipboard using `pyperclip`.[file:372]  
- Input fields for website, email/username, and password.  
- Confirmation dialog before saving credentials.  
- Store credentials in a structured JSON file (`data.json`), one website per key.  
- **Search** button to look up and display saved email/password for a website.  
- Error handling for missing data file and for websites that have not been saved.[file:372][file:370]

---

## Files

### `main.py`

Core application code:

- Imports:
  - Tkinter widgets and `messagebox`.
  - `choice`, `randint`, `shuffle` from `random` for password generation.
  - `pyperclip` for clipboard support.
  - `json` for reading/writing the credentials file.[file:372]

#### Password generation

- `generate_password()`  
  - Builds a password from random letters, numbers, and symbols using list comprehensions and `shuffle()`.  
  - Joins characters into a single string, inserts it into the password entry, and copies it to the clipboard.[file:372]

#### Saving credentials

- `save()`  
  - Reads `website`, `email`, and `password` from the entry fields.  
  - Creates a `new_data` dictionary:
    ```python
    new_data = {
        website: {
            "email": email,
            "password": passwo
        }
    }
    ```  
  - If website or password is empty, shows an “Oops…” info box and does not save.[file:372]  
  - Otherwise:
    - Tries to open `data.json` and load existing data with `json.load()`.  
    - If the file is missing or invalid (`FileNotFoundError` or `JSONDecodeError`), starts from an empty dict.  
    - Updates the old data with `new_data`.  
    - Writes the merged dict back to `data.json` with `json.dump(..., indent=4)`.  
  - Clears the website and password entries in a `finally` block so they reset whether saving succeeded or not.[file:372]

#### Finding a password

- `find_password()`  
  - Reads the website name from the website entry.  
  - Tries to open `data.json` and load data.
    - If the file does not exist, shows “No Data File Found.”  
  - If data loads, checks whether the website key exists:
    - If yes, retrieves the stored email and password and shows them in a message box.  
    - If not, shows a message that no details exist for that website.[file:372][file:370]

#### UI setup

- Creates the main `Tk()` window titled **"Password Manager"**, with padding.  
- `Canvas`:
  - Loads `logo.png` via `PhotoImage` and displays it as a lock icon in the centre.[file:372][file:371]
- Labels:
  - “Website:”
  - “Email/Username:”
  - “Password:”
- Entry fields:
  - Website entry (`width=41`) focused by default.
  - Email entry (`width=60`) pre‑filled with a default address.
  - Password entry (`width=41`).[file:372]
- Buttons:
  - **Generate Password** → calls `generate_password()`.
  - **Add** → calls `save()` to persist credentials.
  - **Search** → calls `find_password()` to look up saved details for the current website.[file:372]
- Starts the Tkinter event loop with `window.mainloop()`.

### `data.json`

- JSON file storing credentials in this structure:
  {
    "Amazon": {
      "email": "example@example.com",
      "password": "R(EK&Ld8hL3#aq"
    }
  }
  
Created/updated automatically by the app when you add entries.[file:370]
logo.png / logo.jpg
Lock icon used in the canvas as the app logo.[file:371]

## Requirements
1.Python 3.10 or higher.
2.Modules:
-tkinter (standard library)
-pyperclip
-json (standard library)[file:372]
Install pyperclip with:
bash
pip install pyperclip

## How to Run
1.Place these files in the same folder:
-main.py
-logo.png (or rename your logo file to match the filename used in main.py)
-data.json (optional; will be created automatically if missing).[file:372][file:370]
2.Open a terminal or command prompt in that folder.
3.Run:
bash
python main.py

## Usage:
1.Type a website and email/username.
2.Click Generate Password to create a strong password and copy it to the clipboard.
3.Click Add to save the entry to data.json.
4.To look up an existing entry, type the website and click Search; the stored email and   password will be shown if found.[file:372][file:370]

## Security Notes
Credentials are stored in plain JSON on disk; this is fine for learning but not secure for real‑world sensitive passwords.

A production‑grade manager would add encryption, a master password, and more robust protection. This project focuses on demonstrating Tkinter, json, file I/O, and basic error handling.[file:372]
