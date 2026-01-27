#!/usr/bin/env node

/**
 * PRD Merge Script
 * Merges all PRD markdown files into a single comprehensive document
 *
 * Usage: node merge-prd.js
 */

const fs = require('fs');
const path = require('path');

// Configuration
const config = {
  inputDir: __dirname,
  outputFile: path.join(__dirname, 'SHUNCOM-RULR-PRD-Complete.md'),
  files: [
    '01-executive-summary.md',
    '02-system-requirements.md',
    '03-device-specifications.md',
    '04-technical-architecture.md',
    '05-functional-requirements.md',
    '06-implementation-roadmap.md',
    '07-resource-requirements.md',
    '08-risk-assessment.md',
    '09-appendix.md'
  ]
};

// Header for merged document
const header = `# SHUNCOM RULR IoT Platform
## Product Requirements Document (PRD)

**Version**: 1.0
**Date**: January 27, 2026
**Status**: Final - Ready for Approval
**Company**: Shanghai Shuncom AIOT Co., Ltd
**Project**: Smart Lighting & Urban Infrastructure Management Platform

---

## Table of Contents

1. [Executive Summary](#1-executive-summary)
2. [System Requirements](#2-system-requirements)
3. [Device Specifications](#3-device-specifications)
4. [Technical Architecture](#4-technical-architecture)
5. [Functional Requirements](#5-functional-requirements)
6. [Implementation Roadmap](#6-implementation-roadmap)
7. [Resource Requirements](#7-resource-requirements)
8. [Risk Assessment](#8-risk-assessment)
9. [Appendix & References](#9-appendix--references)

---

## Document Summary

**Total Budget**: $1,100,000 (Year 1)
**Timeline**: 8 months (Feb 2026 - Sep 2026)
**Team Size**: 10 core + 5 specialists
**Target Devices**: 100,000+ per deployment
**Expected ROI**: 183% by Year 3

---

`;

// Footer for merged document
const footer = `

---

## Document Information

**Generated**: ${new Date().toISOString()}
**Generator**: Automated PRD Merge Script
**Source Files**: 9 individual PRD sections
**Total Pages**: ~250 pages

**For Questions Contact**:
- **Project Manager**: [Email]
- **Technical Lead**: [Email]
- **General Inquiries**: info@rulr-aiot.com

---

**© 2026 Shanghai Shuncom AIOT Co., Ltd. All rights reserved.**

This document contains confidential and proprietary information. Unauthorized disclosure, copying, or distribution is strictly prohibited.
`;

// Main merge function
function mergePRD() {
  console.log('🚀 Starting PRD merge process...\n');

  let mergedContent = header;
  let successCount = 0;
  let errorCount = 0;

  config.files.forEach((filename, index) => {
    const filePath = path.join(config.inputDir, filename);

    try {
      console.log(`📄 Processing ${index + 1}/${config.files.length}: ${filename}`);

      if (!fs.existsSync(filePath)) {
        console.error(`   ❌ File not found: ${filename}`);
        errorCount++;
        return;
      }

      let content = fs.readFileSync(filePath, 'utf8');

      // Remove document metadata (first 10 lines)
      const lines = content.split('\n');
      content = lines.slice(10).join('\n');

      // Add section divider
      mergedContent += `\n\n${'='.repeat(80)}\n\n`;
      mergedContent += `# ${index + 1}. ${getSectionTitle(filename)}\n\n`;
      mergedContent += content;

      successCount++;
      console.log(`   ✅ Merged successfully`);

    } catch (error) {
      console.error(`   ❌ Error processing ${filename}:`, error.message);
      errorCount++;
    }
  });

  // Add footer
  mergedContent += footer;

  // Write merged file
  try {
    fs.writeFileSync(config.outputFile, mergedContent, 'utf8');
    console.log(`\n✅ Merge completed successfully!`);
    console.log(`\n📊 Summary:`);
    console.log(`   - Files processed: ${config.files.length}`);
    console.log(`   - Successful: ${successCount}`);
    console.log(`   - Errors: ${errorCount}`);
    console.log(`   - Output file: ${config.outputFile}`);
    console.log(`   - File size: ${(fs.statSync(config.outputFile).size / 1024).toFixed(2)} KB`);

    // Generate stats
    const stats = generateStats(mergedContent);
    console.log(`\n📈 Document Stats:`);
    console.log(`   - Total lines: ${stats.lines.toLocaleString()}`);
    console.log(`   - Total words: ${stats.words.toLocaleString()}`);
    console.log(`   - Total characters: ${stats.characters.toLocaleString()}`);
    console.log(`   - Estimated pages: ~${stats.pages}`);

  } catch (error) {
    console.error(`\n❌ Error writing merged file:`, error.message);
    process.exit(1);
  }
}

// Helper function to get section title from filename
function getSectionTitle(filename) {
  const titles = {
    '01-executive-summary.md': 'Executive Summary',
    '02-system-requirements.md': 'System Requirements',
    '03-device-specifications.md': 'Device Specifications & Hardware',
    '04-technical-architecture.md': 'Technical Architecture',
    '05-functional-requirements.md': 'Functional Requirements',
    '06-implementation-roadmap.md': 'Implementation Roadmap',
    '07-resource-requirements.md': 'Resource Requirements & Budget',
    '08-risk-assessment.md': 'Risk Assessment & Mitigation',
    '09-appendix.md': 'Appendix & References'
  };
  return titles[filename] || filename;
}

// Generate document statistics
function generateStats(content) {
  const lines = content.split('\n').length;
  const words = content.split(/\s+/).length;
  const characters = content.length;
  const pages = Math.ceil(lines / 50); // Estimate 50 lines per page

  return { lines, words, characters, pages };
}

// Run the merge
mergePRD();

console.log('\n✨ PRD merge process completed!\n');
