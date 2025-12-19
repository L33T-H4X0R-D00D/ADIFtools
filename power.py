import os
import re

def process_adif_files():
    # 1. Prompt for power level
    pwr_input = input("Enter the power level (e.g., 5, 50, 100): ").strip()
    
    if not pwr_input.isdigit():
        print("Error: Please enter a numeric value.")
        return

    # Format the ADIF tag: <TX_PWR:length>value
    pwr_tag = f"<TX_PWR:{len(pwr_input)}>{pwr_input}"
    
    # 2. Iterate through files in the current directory
    files_found = False
    for filename in os.listdir('.'):
        if filename.lower().endswith('.adi') or filename.lower().endswith('.adif'):
            files_found = True
            print(f"Processing {filename}...")
            
            with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()

            # 3. Use regex to insert the tag before the end of the record
            # This looks for <EOR> (case insensitive) and places the tag before it.
            # If your records end differently, we target the end of the record marker.
            new_content = re.sub(
                r'(?i)(<comment)', 
                f'{pwr_tag}\\1', 
                content
            )

            # Write the changes back to the file
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(new_content)
    
    if files_found:
        print("\nSuccess! TX_PWR tags have been appended to all records.")
    else:
        print("No .adi or .adif files found in the current directory.")

if __name__ == "__main__":
    process_adif_files()