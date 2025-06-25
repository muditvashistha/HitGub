# HitGub
HitGub is a lightweight, beginner-friendly version control system built with Python and Tkinter. It lets you create **code checkpoints**, **track changes**, and **revert to previous versions** — all without needing Git.

> 🚀 Perfect for learning version control basics or tracking changes.

---

## 📸 Features

- ✅ Create a checkpoint of your current code anytime
- 🔍 View plain-English diffs between your latest checkpoint and your current code
- ⏪ Revert to your most recent checkpoint with one click
- 🗒️ Access checkpoint logs to review what changed and when
- 🖼️ Minimal but attractive GUI made with Tkinter

---

## 🛠️ Technologies Used

- Python 3.x
- Tkinter (for UI)
- `difflib` (to generate human-readable diffs)
- `os`, `datetime`, `shutil` (for file and time handling)

---

## 🧩 Folder Structure

├── core_functions.py  # Handles creating checkpoints, logs, diffs
├── user_interface.py  # Beautiful Tkinter UI
├── working.py  # Example working file (user writes code here)
├── .checkpoints/  # Stores all checkpoint versions and diff logs
