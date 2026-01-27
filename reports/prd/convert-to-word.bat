@echo off
chcp 65001 > nul
echo ========================================
echo Markdown to Word Converter
echo ========================================
echo.

REM Refresh environment variables
call RefreshEnv.cmd 2>nul

REM Create output directory
if not exist "word-output" mkdir "word-output"

echo Converting files...
echo.

REM Convert each file
pandoc "01-executive-summary.md" -o "word-output/01-executive-summary.docx"
if %ERRORLEVEL% EQU 0 (echo [OK] 01-executive-summary.docx) else (echo [FAIL] 01-executive-summary.md)

pandoc "02-system-requirements.md" -o "word-output/02-system-requirements.docx"
if %ERRORLEVEL% EQU 0 (echo [OK] 02-system-requirements.docx) else (echo [FAIL] 02-system-requirements.md)

pandoc "03-device-specifications.md" -o "word-output/03-device-specifications.docx"
if %ERRORLEVEL% EQU 0 (echo [OK] 03-device-specifications.docx) else (echo [FAIL] 03-device-specifications.md)

pandoc "04-technical-architecture.md" -o "word-output/04-technical-architecture.docx"
if %ERRORLEVEL% EQU 0 (echo [OK] 04-technical-architecture.docx) else (echo [FAIL] 04-technical-architecture.md)

pandoc "05-functional-requirements.md" -o "word-output/05-functional-requirements.docx"
if %ERRORLEVEL% EQU 0 (echo [OK] 05-functional-requirements.docx) else (echo [FAIL] 05-functional-requirements.md)

pandoc "06-implementation-roadmap.md" -o "word-output/06-implementation-roadmap.docx"
if %ERRORLEVEL% EQU 0 (echo [OK] 06-implementation-roadmap.docx) else (echo [FAIL] 06-implementation-roadmap.md)

pandoc "07-resource-requirements.md" -o "word-output/07-resource-requirements.docx"
if %ERRORLEVEL% EQU 0 (echo [OK] 07-resource-requirements.docx) else (echo [FAIL] 07-resource-requirements.md)

pandoc "08-risk-assessment.md" -o "word-output/08-risk-assessment.docx"
if %ERRORLEVEL% EQU 0 (echo [OK] 08-risk-assessment.docx) else (echo [FAIL] 08-risk-assessment.md)

pandoc "09-appendix.md" -o "word-output/09-appendix.docx"
if %ERRORLEVEL% EQU 0 (echo [OK] 09-appendix.docx) else (echo [FAIL] 09-appendix.md)

pandoc "SHUNCOM-RULR-PRD-Complete.md" -o "word-output/SHUNCOM-RULR-PRD-Complete.docx"
if %ERRORLEVEL% EQU 0 (echo [OK] SHUNCOM-RULR-PRD-Complete.docx) else (echo [FAIL] SHUNCOM-RULR-PRD-Complete.md)

echo.
echo ========================================
echo Conversion completed!
echo Output folder: word-output\
echo ========================================
echo.
pause
