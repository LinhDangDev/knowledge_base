import os
import re
from pathlib import Path

# Base directory
base_dir = r"D:\OneDrive - linhdangdev\Documents\Obsidian Vault\ShucomAIOT\SHUNCOM RULR Knowledge Base"

def get_relative_path(from_file, to_file):
    """Calculate relative path between two files"""
    from_path = Path(from_file).parent
    to_path = Path(to_file)
    return os.path.relpath(to_path, from_path).replace('\\', '/')

def convert_wikilink(match, current_file, all_files):
    """Convert [[wikilink]] to [markdown](path.md) link"""
    link_text = match.group(1)

    # Find the target file
    for file_path in all_files:
        file_name = Path(file_path).stem
        if file_name == link_text or file_name.replace(' ', '%20') == link_text:
            rel_path = get_relative_path(current_file, file_path)
            # URL encode spaces
            rel_path = rel_path.replace(' ', '%20')
            return f'[{link_text}]({rel_path})'

    # If not found, return original
    return match.group(0)

def remove_metadata(content):
    """Remove ugly metadata tags"""
    # Remove Tags, Created, Last Updated lines
    content = re.sub(r'\*\*Tags\*\*:.*?\n', '', content)
    content = re.sub(r'\*\*Created\*\*:.*?\n', '', content)
    content = re.sub(r'\*\*Last Updated\*\*:.*?\n', '', content)
    return content

def add_hint_to_header(content):
    """Add GitBook hint after title if metadata was removed"""
    # Check if there's a title and quotation
    pattern = r'(# .*?\n\n> .*?\n\n)'
    if re.search(pattern, content):
        # Add hint after quotation
        content = re.sub(
            pattern,
            r'\1{% hint style="info" %}\n**Platform:** SHUNCOM RULR IoT Platform v1.1 | **Last Updated:** January 2025\n{% endhint %}\n\n',
            content,
            count=1
        )
    return content

def beautify_file(file_path, all_files):
    """Beautify a single markdown file"""
    print(f"Processing: {file_path}")

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # Step 1: Convert wikilinks
    wikilink_pattern = r'\[\[([^\]]+)\]\]'
    content = re.sub(
        wikilink_pattern,
        lambda m: convert_wikilink(m, file_path, all_files),
        content
    )

    # Step 2: Remove metadata
    content = remove_metadata(content)

    # Step 3: Add hint to header
    content = add_hint_to_header(content)

    # Only write if changed
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True

    return False

def main():
    """Main beautification process"""
    # Get all markdown files
    all_files = []
    for root, dirs, files in os.walk(base_dir):
        # Skip reports directory
        if 'reports' in root:
            continue
        for file in files:
            if file.endswith('.md'):
                all_files.append(os.path.join(root, file))

    print(f"Found {len(all_files)} markdown files")

    # Process each file
    modified_count = 0
    for file_path in all_files:
        # Skip already processed System Overview
        if '01-System Overview.md' in file_path:
            print(f"Skipping (already beautified): {file_path}")
            continue

        if beautify_file(file_path, all_files):
            modified_count += 1

    print(f"\n✅ Beautification complete!")
    print(f"📊 Modified {modified_count} files out of {len(all_files)} total files")

if __name__ == "__main__":
    main()
