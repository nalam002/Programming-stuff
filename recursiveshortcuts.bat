@ECHO ON

SET SrcRoot=C:\Users\teacher.DESKTOP-6R84B69\Desktop\test\new\AE-A Term Assessment (Midterm)
SET TargetRoot=C:\Users\teacher.DESKTOP-6R84B69\Desktop\test\new\AE-A Term Assessment (Midterm)_link

SETLOCAL ENABLEDELAYEDEXPANSION
FOR /R "%SrcRoot%" %%A IN ("*") DO (
  SET oDir=%%~DPA
  SET oFile=%%~A
  IF NOT EXIST "%TargetRoot%!oDir:~80!" MD "%TargetRoot%!oDir:~80!"
    IF NOT EXIST "%TargetRoot%!oFile:~80!" MKLINK "%TargetRoot%!oFile:~80!" "%%~A"
  )

PAUSE
EXIT