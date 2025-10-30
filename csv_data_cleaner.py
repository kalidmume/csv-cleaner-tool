
import os 
import pandas as pd 
from datetime import datetime 

def clean_data(file_path):
  """Clean data csv from messy, unwanted space """
  try:
    #get dataframe of file csv 
    df = pd.read_csv(file_path, on_bad_lines="skip", encoding="utf-8")
    before = len(df) # length file csv Before clean 
    for col in df.select_dtypes(include=['object']):
        df[col] = df[col].str.strip()
    # Remove fully empty rows
    df.replace(r'^\s*$', pd.NA, regex=True, inplace=True)  # Convert empty/whitespace strings to NA
    df.dropna(how='all', inplace=True)      
    #remove unwanted spaces 
    df.fillna('', inplace=True)
    #remove duplicates 
    df.drop_duplicates(inplace=True)
    after = len(df) # length file csv  after Cleaned
    base = os.path.splitext(os.path.basename(file_path))[0]
    date = datetime.now().strftime("%Y-%m-%d")
    count = 1
    file_output = f"{base}_Clean_{date}.csv"
    while os.path.exists(file_output):
      count += 1
      file_output = f"{base}_Clean_{date}_{count}.csv"
    df.to_csv(file_output, index=False, encoding="utf-8")
    print(f"✅ Cleaned successfully!  Rows: {before} → {after}")
    print(f"💾 Saved as {file_output}")
  except Exception as error:
    print(f"Error: {error}")

def get_file_path():
  """Function get from user file path check if correct continue else ask again"""
  while True:
    file = input("Enter file path: ").strip()
    file = os.path.abspath(file)
    
    if os.path.exists(file) and os.path.isfile(file):
      return file 
    elif os.path.isdir(file):
      print(f"📁 This is folder path: {file}")
    else:
      print("❌️ File path not found")


def main():
  print("=" * 35)
  print("=== FILE DATA CLEANER TOOLS ===".center(35))
  print("=" * 35)
  
  #Step1 get file path 
  file_path = get_file_path()
  #Step2 clean data & saved 
  clean_data(file_path)

main()

