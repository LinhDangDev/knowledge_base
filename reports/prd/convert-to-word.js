#!/usr/bin/env node

/**
 * Markdown to Word Converter Script
 * Converts all PRD markdown files to Word (.docx) format using Pandoc
 *
 * Usage: node convert-to-word.js
 */

const { execSync } = require('child_process');
const fs = require('fs');
const path = require('path');

// Configuration
const config = {
  inputDir: __dirname,
  outputDir: path.join(__dirname, 'word-output'),
  pandocPath: 'C:\\Program Files\\Pandoc\\pandoc.exe', // Default Pandoc installation path
  files: [
    '01-executive-summary.md',
    '02-system-requirements.md',
    '03-device-specifications.md',
    '04-technical-architecture.md',
    '05-functional-requirements.md',
    '06-implementation-roadmap.md',
    '07-resource-requirements.md',
    '08-risk-assessment.md',
    '09-appendix.md',
    'SHUNCOM-RULR-PRD-Complete.md'
  ]
};

// Create output directory if it doesn't exist
if (!fs.existsSync(config.outputDir)) {
  fs.mkdirSync(config.outputDir, { recursive: true });
}

// Check if Pandoc is available
function checkPandoc() {
  try {
    // Try using pandoc from PATH first
    execSync('pandoc --version', { stdio: 'ignore' });
    return 'pandoc';
  } catch (error) {
    // Try using full path
    if (fs.existsSync(config.pandocPath)) {
      return `"${config.pandocPath}"`;
    }
    throw new Error('Pandoc not found. Please ensure Pandoc is installed and in PATH, or update config.pandocPath');
  }
}

// Convert markdown to Word
function convertToWord(inputFile, outputFile, pandocCmd) {
  const command = `${pandocCmd} "${inputFile}" -o "${outputFile}" --reference-doc=reference.docx || ${pandocCmd} "${inputFile}" -o "${outputFile}"`;

  try {
    execSync(command, {
      cwd: config.inputDir,
      stdio: 'inherit'
    });
    return true;
  } catch (error) {
    console.error(`   ❌ Error converting ${path.basename(inputFile)}:`, error.message);
    return false;
  }
}

// Get file size in KB
function getFileSize(filePath) {
  const stats = fs.statSync(filePath);
  return (stats.size / 1024).toFixed(2);
}

// Get title from filename
function getTitle(filename) {
  const titles = {
    '01-executive-summary.md': '01 - Executive Summary',
    '02-system-requirements.md': '02 - System Requirements',
    '03-device-specifications.md': '03 - Device Specifications',
    '04-technical-architecture.md': '04 - Technical Architecture',
    '05-functional-requirements.md': '05 - Functional Requirements',
    '06-implementation-roadmap.md': '06 - Implementation Roadmap',
    '07-resource-requirements.md': '07 - Resource Requirements',
    '08-risk-assessment.md': '08 - Risk Assessment',
    '09-appendix.md': '09 - Appendix & References',
    'SHUNCOM-RULR-PRD-Complete.md': 'SHUNCOM RULR PRD - Complete Document'
  };
  return titles[filename] || filename;
}

// Main conversion function
function main() {
  console.log('🚀 Starting Markdown to Word conversion...\n');

  // Check Pandoc availability
  let pandocCmd;
  try {
    pandocCmd = checkPandoc();
    console.log('✅ Pandoc found and ready\n');
  } catch (error) {
    console.error('❌ Error:', error.message);
    console.log('\n📝 Installation instructions:');
    console.log('   1. Close this terminal');
    console.log('   2. Open a new terminal/PowerShell as Administrator');
    console.log('   3. Run: winget install --id JohnMacFarlane.Pandoc');
    console.log('   4. Restart terminal and run this script again\n');
    process.exit(1);
  }

  let successCount = 0;
  let errorCount = 0;
  const convertedFiles = [];

  // Convert each file
  config.files.forEach((filename, index) => {
    const inputPath = path.join(config.inputDir, filename);
    const outputFilename = filename.replace('.md', '.docx');
    const outputPath = path.join(config.outputDir, outputFilename);

    // Check if input file exists
    if (!fs.existsSync(inputPath)) {
      console.log(`⚠️  Skipping ${filename} - File not found`);
      errorCount++;
      return;
    }

    console.log(`📄 Converting ${index + 1}/${config.files.length}: ${getTitle(filename)}`);

    if (convertToWord(inputPath, outputPath, pandocCmd)) {
      const fileSize = getFileSize(outputPath);
      console.log(`   ✅ Created: ${outputFilename} (${fileSize} KB)\n`);
      convertedFiles.push({
        name: outputFilename,
        size: fileSize,
        path: outputPath
      });
      successCount++;
    } else {
      errorCount++;
    }
  });

  // Summary
  console.log('\n' + '='.repeat(80));
  console.log('📊 Conversion Summary\n');
  console.log(`   Total files: ${config.files.length}`);
  console.log(`   ✅ Successful: ${successCount}`);
  console.log(`   ❌ Errors: ${errorCount}`);
  console.log(`   📁 Output directory: ${config.outputDir}\n`);

  if (convertedFiles.length > 0) {
    console.log('📝 Converted Files:\n');
    convertedFiles.forEach(file => {
      console.log(`   • ${file.name} (${file.size} KB)`);
    });

    const totalSize = convertedFiles.reduce((sum, file) => sum + parseFloat(file.size), 0);
    console.log(`\n   Total size: ${totalSize.toFixed(2)} KB`);
  }

  console.log('\n' + '='.repeat(80));
  console.log('✨ Conversion completed!\n');

  if (errorCount > 0) {
    console.log('⚠️  Some files failed to convert. Please check the errors above.\n');
  }
}

// Run the conversion
main();
