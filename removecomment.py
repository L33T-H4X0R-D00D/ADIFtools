"""
Version 1
"""

import re
import os

def process_all_files():
    # Regex to find: <comment:LENGTH>TEXT<
    comment_pattern = re.compile(r'<comment:(\d+)>(.*?)<', re.IGNORECASE)
    
    # Strings to remove
    targets_to_remove = ["QSO by FT8TW_UAT", "QSO by FT8CN"]
    
    # Create an output directory so we don't overwrite original files
    output_dir = "./"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Get all files in current directory
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    
    processed_count = 0

    for filename in files:
        # Only process .txt or .adi files (adjust extensions if needed)
        if filename.lower().endswith(('.adi')):
            print(f"Processing: {filename}...")
            
            output_path = os.path.join(output_dir, f"cleaned_{filename}")
            
            try:
                with open(filename, 'r', encoding='utf-8', errors='ignore') as f_in, \
                     open(output_path, 'w', encoding='utf-8') as f_out:
                    
                    for line in f_in:
                        match = comment_pattern.search(line)
                        if match:
                            new_comment = match.group(2)
                            
                            for target in targets_to_remove:
                                new_comment = new_comment.replace(f", {target}", "")
                                new_comment = new_comment.replace(target, "")
                            
                            new_comment = new_comment.strip()
                            new_length = len(new_comment)
                            
                            # Replace the tag with the corrected length
                            new_tag_and_text = f"<comment:{new_length}>{new_comment}<"
                            line = line.replace(match.group(0), new_tag_and_text)
                        
                        f_out.write(line)
                
                processed_count += 1
                
            except Exception as e:
                print(f"Error processing {filename}: {e}")

    print(f"\nFinished! {processed_count} files processed.")
    print(f"You can find your cleaned files in the '{output_dir}' folder.")

if __name__ == "__main__":
    process_all_files()