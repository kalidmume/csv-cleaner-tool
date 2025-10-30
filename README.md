__

** 🧹 CSV Data Cleaner Tool **

A simple, fast, and reliable Python tool to clean messy CSV files by removing empty rows, trimming spaces, removing duplicates, and filling missing values — perfect for freelancers, data analysts, and automation projects.

🌟 Overview

This tool automatically cleans and organizes your CSV files. Instead of manually fixing messy data, this script:

Strips unwanted spaces

Removes fully empty rows

Fills missing cells with empty strings

Removes duplicate rows

Saves the cleaned file safely with a timestamped name

It’s ideal for:

Freelance automation tasks

Preparing data for Excel, Google Sheets, or Pandas

Quickly fixing client CSV files

Mobile Python coding (Pydroid3 / Termux)

🚀 Features

✅ Cleans empty or whitespace-only rows ✅ Trims extra spaces from each cell ✅ Fills missing cells with empty strings for consistency ✅ Removes duplicate rows ✅ Prevents overwriting by generating unique output filenames ✅ Beginner-friendly and professional structure ✅ Works on mobile (Pydroid3 / Termux) and desktop

🛠️ How It Works

1️⃣ Checks if the input CSV file exists

2️⃣ Reads the file using Pandas

3️⃣ Strips whitespace from all string columns

4️⃣ Converts empty or whitespace-only rows to NA and removes them

5️⃣ Fills remaining missing cells with empty strings

6️⃣ Removes duplicate rows

7️⃣ Saves the cleaned CSV with a timestamped filename

8️⃣ Prints a success message showing rows before and after cleaning

📦 Example

Input File — data.csv:

Name, Age, Country Kalid, 18, Kenya Sora, , Saudi , , Mansur, 18, English

Output File — data_Clean_2025-10-30.csv:

Name,Age,Country Kalid,18,Kenya Sora,,Saudi Mansur,18,English

✅ Cleaned successfully! Rows: 4 → 3

💻 Usage

1️⃣ Run the Script

python csv_data_cleaner.py

2️⃣ Enter CSV File Path

Enter file path: data.csv

3️⃣ Output Example

✅ Cleaned successfully! Rows: 4 → 3 💾 Saved as data_Clean_2025-10-30.csv

🧩 File Structure

csv_data_cleaner/ ├── csv_data_cleaner.py ├── README.md ├── sample_input.csv ├── sample_output_cleaned.csv └── LICENSE (MIT)

🧠 Code Preview

import os import pandas as pd from datetime import datetime

def clean_data(file_path): “““Clean CSV by removing empty rows, duplicates, and trimming spaces””” try: df = pd.read_csv(file_path, on_bad_lines=“skip”, encoding=“utf-8”) before = len(df) for col in df.select_dtypes(include=[‘object’]): df[col] = df[col].str.strip() df.replace(r’^\s*$‘, pd.NA, regex=True, inplace=True) df.dropna(how=‘all’, inplace=True) df.fillna(’’, inplace=True) df.drop_duplicates(inplace=True) after = len(df) base = os.path.splitext(os.path.basename(file_path))[0] date = datetime.now().strftime(“%Y-%m-%d”) count = 1 file_output = f"{base}Clean{date}.csv" while os.path.exists(file_output): count += 1 file_output = f"{base}Clean{date}_{count}.csv" df.to_csv(file_output, index=False, encoding=“utf-8”) print(f"✅ Cleaned successfully! Rows: {before} → {after}“) print(f”💾 Saved as {file_output}“) except Exception as error: print(f"Error: {error}”)

💡 Why You Love It

Saves hours of manual data cleanup

Lightweight , simple and professional

Can clean CSVs for finance, e-commerce, analytics, or school data

Easy to integrate into bigger automation workflows

🔮 Future Improvements

Batch process multiple CSV files in a folder

Add Excel file support (.xlsx)

Generate summary reports (rows removed, duplicates found)

Add CLI arguments for automation

👨‍💻 Author

KalidCode — Freelance Python Developer & Automation Engineer 💼 Services: Data Cleaning • Automation Scripts • File Tools • Flask APIs 🌐 Portfolio: https://github.com/kalidmume

⚖️ License

This project is licensed under the MIT License — see LICENSE file for details.

---
