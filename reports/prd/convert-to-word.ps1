# PowerShell Script: Markdown to Word Converter
# Converts all PRD markdown files to Word (.docx) format using Pandoc

Write-Host "🚀 Starting Markdown to Word conversion...`n" -ForegroundColor Cyan

# Configuration
$inputDir = $PSScriptRoot
$outputDir = Join-Path $inputDir "word-output"
$files = @(
    "01-executive-summary.md",
    "02-system-requirements.md",
    "03-device-specifications.md",
    "04-technical-architecture.md",
    "05-functional-requirements.md",
    "06-implementation-roadmap.md",
    "07-resource-requirements.md",
    "08-risk-assessment.md",
    "09-appendix.md",
    "SHUNCOM-RULR-PRD-Complete.md"
)

# Create output directory
if (-not (Test-Path $outputDir)) {
    New-Item -ItemType Directory -Path $outputDir | Out-Null
}

# Refresh environment variables
$env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")

# Check if Pandoc is available
try {
    $pandocVersion = & pandoc --version 2>&1 | Select-Object -First 1
    Write-Host "✅ Pandoc found: $pandocVersion`n" -ForegroundColor Green
} catch {
    Write-Host "❌ Pandoc not found in PATH`n" -ForegroundColor Red
    Write-Host "Please restart PowerShell or run:`n" -ForegroundColor Yellow
    Write-Host "    `$env:Path = [System.Environment]::GetEnvironmentVariable('Path','Machine')`n"
    exit 1
}

# Convert files
$successCount = 0
$errorCount = 0
$convertedFiles = @()

foreach ($file in $files) {
    $inputPath = Join-Path $inputDir $file
    $outputFile = $file -replace '\.md$', '.docx'
    $outputPath = Join-Path $outputDir $outputFile

    if (-not (Test-Path $inputPath)) {
        Write-Host "⚠️  Skipping $file - File not found" -ForegroundColor Yellow
        $errorCount++
        continue
    }

    $index = $files.IndexOf($file) + 1
    Write-Host "📄 Converting $index/$($files.Count): $file"

    try {
        # Convert using Pandoc
        & pandoc $inputPath -o $outputPath

        if ($LASTEXITCODE -eq 0) {
            $fileSize = [math]::Round((Get-Item $outputPath).Length / 1KB, 2)
            Write-Host "   ✅ Created: $outputFile ($fileSize KB)`n" -ForegroundColor Green
            $convertedFiles += @{Name = $outputFile; Size = $fileSize}
            $successCount++
        } else {
            Write-Host "   ❌ Failed to convert $file`n" -ForegroundColor Red
            $errorCount++
        }
    } catch {
        Write-Host "   ❌ Error: $($_.Exception.Message)`n" -ForegroundColor Red
        $errorCount++
    }
}

# Summary
Write-Host ("=" * 80) -ForegroundColor Cyan
Write-Host "📊 Conversion Summary`n" -ForegroundColor Cyan
Write-Host "   Total files: $($files.Count)"
Write-Host "   ✅ Successful: $successCount" -ForegroundColor Green
Write-Host "   ❌ Errors: $errorCount" -ForegroundColor Red
Write-Host "   📁 Output directory: $outputDir`n"

if ($convertedFiles.Count -gt 0) {
    Write-Host "📝 Converted Files:`n" -ForegroundColor Cyan
    foreach ($file in $convertedFiles) {
        Write-Host "   • $($file.Name) ($($file.Size) KB)"
    }
    $totalSize = ($convertedFiles | Measure-Object -Property Size -Sum).Sum
    Write-Host "`n   Total size: $([math]::Round($totalSize, 2)) KB"
}

Write-Host ("`n" + "=" * 80) -ForegroundColor Cyan
Write-Host "✨ Conversion completed!`n" -ForegroundColor Green

if ($errorCount -gt 0) {
    Write-Host "⚠️  Some files failed to convert. Please check the errors above.`n" -ForegroundColor Yellow
}
