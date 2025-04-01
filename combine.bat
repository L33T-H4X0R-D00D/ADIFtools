@echo off
rem combine all ADIF files into single text file
type *.adi >> new.txt

rem dedupe lines within the txt file
copy nul importfile.tmp >nul

for /f "tokens=*" %%a in (new.txt) do (
  find "%%a" importfile.tmp >nul || echo %%a>>importfile.tmp
)

move /y importfile.tmp new.txt


rem rename the txt file to adi
ren new.txt combined.adi

