# 💻 Laptop Cleaner Script

A simple and automated Windows cleaner script that removes temporary files to free up space and improve system performance. This script deletes files from:

- `temp` folder
- `%temp%` folder (User's temp files)
- `prefetch` folder

It runs automatically using Windows Task Scheduler.

## 📜 Features
✅ Deletes unnecessary temporary files automatically
✅ Improves system performance
✅ Runs in the background without user intervention
✅ Lightweight and fast execution

## 🚀 Installation
1. **Download the script** from this repository.
2. **Extract the script** if it’s in a compressed format.
3. **Place it in a secure location** (e.g., `C:\Scripts\laptop_cleaner.py`).

## ⚙️ Setting Up Task Scheduler (Automatic Execution)

1. Press `Win + R`, type `taskschd.msc`, and hit `Enter`.
2. Click on **Create Basic Task...**.
3. Give your task a name (e.g., `Laptop Cleaner`) and a description.
4. Click **Next** and select how often you want to run the script (`Daily`, `Weekly`, etc.).
5. Click **Next**, set the time, and then **Next** again.
6. Select **Start a Program** and click **Next**.
7. In the **Program/script** field, type `python`.
8. In the **Add arguments (optional)** field, enter the full path of the script (e.g., `C:\Scripts\laptop_cleaner.py`).
9. Click **Finish** to save the task.
10. Right-click the task in the list, choose **Properties**, and enable **Run with highest privileges**.

## 🛑 Important Notes
- The `prefetch` folder helps improve startup times, so clearing it too frequently may slow down initial boot times.
- Running the script requires administrative privileges.
- Ensure that Task Scheduler is correctly configured to prevent any execution issues.

## 📝 Contributing
Feel free to improve or suggest changes by submitting a pull request!

---

💡 **Tip:** Schedule the cleaner to run once a week to keep your laptop optimized without affecting performance!

