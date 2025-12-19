rem Version 1.3
@echo on
rem Combine all ADIF files into single scratch file
type *.adi >> scratch.tmp
pause

rem Create empty file named importfile.tmp
copy nul importfile.tmp >nul
pause

rem Dedupe lines in the scratch file, into the import file.
for /f "tokens=*" %%a in (scratch.tmp) do (
  find "%%a" importfile.tmp >nul || echo %%a>>importfile.tmp
)
pause

rem Overwrite the current combined file with new deduped temp file
move /y importfile.tmp combined.adi
pause

rem Get rid of scretch file. 
del scratch.tmp
pause
