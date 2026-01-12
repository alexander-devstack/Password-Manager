# MyPass – Local Password Manager (Tkinter)

MyPass is a simple local password manager built with Python and Tkinter. It generates strong random passwords, lets you associate them with a website and email/username, and saves the entries to a local `data.txt` file instead of relying on a third‑party cloud service.[file:356][file:355]

> Note: This is a learning project and is **not** intended as a production‑grade secure password manager. It demonstrates basic GUI design, password generation, file I/O, and clipboard usage in Python.

---

## Features

- Generate random passwords using letters, numbers, and symbols.
- One‑click copy of the generated password to the clipboard via `pyperclip`.
- Input fields for website, email/username, and password.
- Confirmation dialog before saving any credentials.
- Append‑only local storage in `data.txt` (one entry per line: `website | email | password`).[file:356]

---

## Files

- `main.py`  
  Core application code:
  - Imports Tkinter widgets, message boxes, `random` utilities, and `pyperclip` for clipboard support.[file:356]
  - **`generate_password()`**
    - Builds a password from random letters, numbers, and symbols.
    - Shuffles the characters, joins them into a string, inserts it into the password entry field, and copies it to the clipboard.[file:356]
  - **`save()`**
    - Reads values from the website, email, and password entry fields.
    - If website or password is empty, shows an “Oops” info box.
    - Otherwise, shows a confirmation dialog summarizing email and password.
    - On approval, appends `website | email | password` to `data.txt`, then clears the website and password inputs.[file:356]
  - **UI setup**
    - Creates the main `Tk()` window with padding.
    - Displays a lock/logo image using a `Canvas` and `PhotoImage` (`logo.png` in the same folder).
    - Adds labels and entry fields for Website, Email/Username, and Password.
    - “Generate Password” button calls `generate_password()`.
    - “Add” button calls `save()` and spans the full width under the inputs.[file:356]

- `logo.png` / `logo.jpg`  
  - Lock icon used in the canvas as the app logo.[file:355]

- `data.txt` *(created/used at runtime)*  
  - Local text file where credentials are stored, one record per line.

---

## Requirements

- Python 3.10 or higher.
- Modules:
  - `tkinter` (standard library)
  - `pyperclip` for clipboard integration

Install `pyperclip` with:

```bash
pip install pyperclip

##How to Run
1.Place these files in the same folder:
main.py
logo.png (or adjust the filename in main.py to match your logo)
data.txt (optional; will be created automatically if it does not exist)[file:356][file:355]
2.Open a terminal or command prompt in that folder.
3.Run:
python main.py
4.In the window:
Enter a website and, optionally, adjust the email/username.
Click Generate Password to create a strong password and copy it to the clipboard.
Click Add and confirm in the dialog to save the entry to data.txt.

##Security Notes
Entries are stored as plain text in data.txt, which is fine for learning but not secure for sensitive real‑world passwords.
For serious use, consider encryption, master passwords, and more robust storage (this project is meant as an educational GUI + file handling example only).




