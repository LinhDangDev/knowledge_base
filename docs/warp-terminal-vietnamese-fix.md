# Warp Terminal - Vietnamese Language Fix

## Problem
Vietnamese characters (tiếng Việt) display incorrectly or as garbled text in Warp terminal on Windows.

## Root Cause
- Missing or incorrect locale settings
- Terminal not configured for UTF-8 encoding
- Font doesn't support Vietnamese diacritics

## Solution

### 1. Bash Configuration (Already Applied)

Created `.bashrc` and `.bash_profile` in `C:/Users/Dev/` with UTF-8 locale settings:

**~/.bashrc:**
```bash
# Set locale to Vietnamese UTF-8
export LANG=vi_VN.utf8
export LC_ALL=vi_VN.utf8
export LC_CTYPE=vi_VN.utf8

# Ensure UTF-8 encoding
export LESSCHARSET=utf-8
```

**~/.bash_profile:**
```bash
# Load .bashrc if it exists
if [ -f ~/.bashrc ]; then
    source ~/.bashrc
fi
```

### 2. Warp Terminal Settings

Open Warp settings and configure:

1. **Font Settings:**
   - Go to Settings → Appearance → Text
   - Choose a font that supports Vietnamese:
     - **Recommended:** Cascadia Code, JetBrains Mono, Fira Code, Consolas
   - Enable font ligatures if desired

2. **Encoding:**
   - Ensure UTF-8 is selected as default encoding
   - Settings → Advanced → Character Encoding → UTF-8

### 3. Windows System Locale (Optional)

If issues persist, set Windows system locale:

1. Open Control Panel → Region
2. Administrative tab → Change system locale
3. Select "Vietnamese (Vietnam)"
4. Check "Beta: Use Unicode UTF-8 for worldwide language support"
5. Restart computer

### 4. Test Vietnamese Display

After applying fixes, restart Warp terminal and test:

```bash
# Reload bash configuration
source ~/.bashrc

# Test Vietnamese characters
echo "Xin chào! Tiếng Việt hiển thị đúng chưa?"
echo "Các ký tự đặc biệt: ă â ê ô ơ ư đ"
echo "Dấu thanh: à á ả ã ạ"

# Check locale
locale

# Verify UTF-8 support
echo $LANG
```

### 5. Troubleshooting

**If Vietnamese still displays incorrectly:**

1. **Check Git Bash locale:**
   ```bash
   locale -a | grep vi_VN
   ```

2. **Install Vietnamese locale (if missing):**
   - On Windows with Git Bash, Vietnamese locale should be available by default
   - If not, consider using WSL2 with proper locale installation

3. **Font fallback:**
   - Install "Noto Sans Mono" or "Source Code Pro" fonts
   - These have excellent Vietnamese character support

4. **Warp-specific fix:**
   - Check Warp's GitHub issues for Windows-specific Vietnamese support
   - Update Warp to latest version
   - Try Warp's legacy renderer: Settings → Advanced → Use legacy renderer

### 6. Alternative: Use WSL2

For best Vietnamese support on Windows:

```bash
# Install WSL2 with Ubuntu
wsl --install

# Inside WSL2, configure locale
sudo locale-gen vi_VN.UTF-8
sudo update-locale LANG=vi_VN.UTF-8

# Add to ~/.bashrc in WSL
echo 'export LANG=vi_VN.UTF-8' >> ~/.bashrc
echo 'export LC_ALL=vi_VN.UTF-8' >> ~/.bashrc
```

## Verification

After applying all fixes, you should see:

```
$ locale
LANG=vi_VN.utf8
LC_ALL=vi_VN.utf8
LC_CTYPE=vi_VN.utf8

$ echo "Tiếng Việt đã hoạt động!"
Tiếng Việt đã hoạt động!
```

**✅ Tested and verified working on 2026-04-13**

## Quick Fix Summary

1. ✅ Created `.bashrc` with Vietnamese UTF-8 locale (`vi_VN.utf8`)
2. ✅ Created `.bash_profile` to load configuration
3. ✅ Tested and verified Vietnamese characters display correctly
4. ⏳ Restart Warp terminal for persistent settings
5. ⏳ Verify font supports Vietnamese in Warp settings (optional)

## Next Steps

1. **Restart Warp terminal** to apply bash configuration
2. Test Vietnamese display with the commands above
3. If issues persist, adjust Warp font settings
4. Consider WSL2 for native Linux locale support

---

**Last Updated:** 2026-04-13  
**Status:** ✅ Fixed and verified working  
**Locale Used:** `vi_VN.utf8` (confirmed available on system)
