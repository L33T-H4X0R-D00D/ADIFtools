"""
Version 1
"""

import os

def combine_and_deduplicate(source_dir, output_file):
    # Use a set to store unique lines (automatically handles deduplication)
    unique_lines = set()

    # Check if directory exists
    if not os.path.exists(source_dir):
        print(f"Error: Directory '{source_dir}' not found.")
        return

    print(f"Reading files from: {source_dir}...")

    # 1. Iterate through all files in the source directory
    for filename in os.listdir(source_dir):
        if filename.endswith(".adi"):
            file_path = os.path.join(source_dir, filename)
            
            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    # Add each line to the set
                    for line in f:
                        # strip() removes leading/trailing whitespace including \n
                        # Check if line is not empty AND does not contain <eoh>. This ensures "Text" and "Text " are treated as duplicates
                        clean_line = line.strip()
                        if clean_line and "<eoh>" not in clean_line:
                            unique_lines.add(clean_line)
            except Exception as e:
                print(f"Could not read {filename}: {e}")

    # 2. Write the unique lines to the new output file
    try:
        with open(output_file, 'w', encoding='utf-8') as f_out:
            # Sorting makes the output easier to read, though not strictly required
            for line in sorted(unique_lines):
                f_out.write(line + '\n')
                
        print(f"Success! Combined {len(unique_lines)} unique lines into '{output_file}'")
        
    except Exception as e:
        print(f"Error writing to output file: {e}")

# --- Configuration ---
# Update these paths to match your actual folders
# '.' represents the current folder where the script is running
source_directory = './'  
output_filename = 'combined_unique.adi'

# Run the function
combine_and_deduplicate(source_directory, output_filename)
