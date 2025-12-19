# ADIF Tools
These tools automate common tasks for ADIF files. I initially started this toolset using Windows batch scripts since it was quick and easy.  Due to the terrible rollout of Windows 11 and Microsoft's response I've moved to Python since it's indifferent of OS. These tools are built to manipulate ADIF files where each entry is on it's own line.  If your software outputs multiline entries you'll need to flatten them all to one line per entry for these tools to work.  By design these tools don't delete files. As long as you maintain your backup of original files exported by your logging software you can always undo any errors. All of the scripts are designed to edit any .adi file in it's current directory.  You do not need to pass it any arguments so you can invoke it through the command prompt or by double clicking. My workflow is:

1. Download original ADIF from logging tool into working directory
2. Removecomments.py - a new file is created
3. Move the original file to your directory for original files
4. Power.py - new file is updated with power tag
5. Upload this new file to your logbook of choice
6. Move the new file to your directory for updated files

Once you have both files moved to their appropriate directories you can run combine.py to consolidate all QSOs into one file.  This is useful if you normally log to QRZ and decide to also log to eQSL or LOTW.  You can also use the combined file to map all your QSOs on tools like https://stephenhouser.com/qso-mapper/. It is necessary to keep the original and updated files seperate since the deduplication process compares lines.  If you run both removecomments.py and power.py on files co-mingled with your originals, you'll end up with at least one duplicate entry for every QSO.


## removecomment.py
Will remove a string of text from the comment tag and recalculate the tag checksum for all ADIF files in the current directory.  You can change the text that is removed in line 13 of the script. Prepends *cleaned* to the file name for the output file.  **Output file: cleaned_XXXXX.adi**

## power.py
Will prompt the user for a the power used to make the QSOs in the current file, then add the <tx_pwr> tag and checksum to every line before the <comment> tag. If your logger doesn't use the <comment> tag on every line, line 29 can be changed from "<comment" to "<eor>". If you used different power levels for QSOs in the ADIF file, you'll need to break out the QSO entries into seperate files by power.  This script modifies all ADIF files in the current directory. **Output file: *original_file_name*.adi**

## combine.py
Will combine all single line entry ADIF files found in the current directory, remove duplicate lines, and remove header lines.  It does sort the entries based on callsign. If your ADIF files have multiple headers from different applications, they will be removed from the output file.  If you want a header you'll need to edit it in after running the script. **Output file: combined_unique.adi**

## combine.bat
Will combine all single line entry ADIF files found in the current directory and remove duplicate lines.  It does not sort the entries. If your ADIF files have multiple headers from different applications, they will end up in the output file.  This could lead to problems when uploading to your logbook. This script was put together quick and dirty.  It's slowed down by disk writes. It's now deprecated, please use combine.py instead.  **Output file: combined.adi**
