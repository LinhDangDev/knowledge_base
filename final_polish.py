import os
import re
from pathlib import Path

base_dir = r"D:\OneDrive - linhdangdev\Documents\Obsidian Vault\ShucomAIOT\SHUNCOM RULR Knowledge Base"

def enhance_mermaid_diagram(content):
    """Add colors to mermaid diagrams"""

    # Enhance graph diagrams
    def add_graph_colors(match):
        diagram = match.group(0)

        # Skip if already has classDef
        if 'classDef' in diagram:
            return diagram

        # Add classDef at the end before ```
        colors = """
    classDef default fill:#4A90E2,stroke:#2E5C8A,stroke-width:2px,color:#fff
    classDef primary fill:#7B68EE,stroke:#5A4FC4,stroke-width:2px,color:#fff
    classDef success fill:#50C878,stroke:#3A9B5C,stroke-width:2px,color:#fff
    classDef warning fill:#FFA500,stroke:#CC8400,stroke-width:2px,color:#fff
    classDef danger fill:#FF6B6B,stroke:#CC5555,stroke-width:2px,color:#fff"""

        diagram = diagram.replace('```', colors + '\n```')
        return diagram

    # Find and enhance graph diagrams
    content = re.sub(
        r'```mermaid\s*\ngraph\s+[A-Z]+.*?```',
        add_graph_colors,
        content,
        flags=re.DOTALL
    )

    return content

def remove_duplicate_hints(content):
    """Remove duplicate GitBook hints"""
    lines = content.split('\n')
    seen_hints = set()
    new_lines = []
    skip_next = 0

    for i, line in enumerate(lines):
        if skip_next > 0:
            skip_next -= 1
            continue

        if line.strip().startswith('{% hint'):
            # Get the hint block (3 lines usually)
            hint_block = '\n'.join(lines[i:i+3])
            if hint_block in seen_hints:
                skip_next = 2  # Skip next 2 lines (content + endhint)
                continue
            seen_hints.add(hint_block)

        new_lines.append(line)

    return '\n'.join(new_lines)

def fix_remaining_wikilinks(content):
    """Fix any remaining wikilinks that were missed"""
    # Common patterns for files that exist
    replacements = {
        '[[Integration Patterns]]': '[Integration Guide](02-System-Architecture/Integration%20Guide.md)',
        '[[Scalability Planning]]': '[Performance Benchmarks](08-Development-Guide/Performance%20Benchmarks.md)',
        '[[Gateway Configuration Guide]]': '[Protocol Guides](03-Device-Management/Protocol%20Guides.md)',
        '[[Light Controller Setup]]': '[Device Types Reference](Device%20Types%20Reference.md)',
        '[[Batch Operations Manual]]': '[Device Management Hub](03-Device-Management/03-Device%20Management%20Hub.md)',
        '[[Alarm Management Guide]]': '[Rule Engine System](04-Rule-Management/04-Rule%20Engine%20System.md)',
        '[[Platform Rules Examples]]': '[Rule Configuration Patterns](04-Rule-Management/Rule%20Configuration%20Patterns.md)',
        '[[Alarm Configuration Examples]]': '[Rule Configuration Patterns](04-Rule-Management/Rule%20Configuration%20Patterns.md)',
        '[[Rule Testing Procedures]]': '[Testing Scenarios](08-Development-Guide/Testing%20Scenarios.md)',
        '[[Rule Performance Optimization]]': '[Performance Benchmarks](08-Development-Guide/Performance%20Benchmarks.md)',
    }

    for wikilink, markdown_link in replacements.items():
        content = content.replace(wikilink, markdown_link)

    return content

def final_polish(file_path):
    """Final polish for each file"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # Fix remaining wikilinks
    content = fix_remaining_wikilinks(content)

    # Remove duplicate hints
    content = remove_duplicate_hints(content)

    # Enhance mermaid diagrams
    content = enhance_mermaid_diagram(content)

    if content != original:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True

    return False

def main():
    print("Final polish - Enhancing mermaid diagrams and fixing remaining issues...\n")

    modified = 0
    for root, dirs, files in os.walk(base_dir):
        if 'reports' in root:
            continue
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                if final_polish(file_path):
                    print(f"[OK] Polished: {file}")
                    modified += 1

    print(f"\n[SUCCESS] Final polish complete!")
    print(f"[STATS] Polished {modified} files")

if __name__ == "__main__":
    main()
