#!/usr/bin/env python3
"""
Fix links in building block README files
Changes .md links to .html links for GitHub Pages compatibility
"""

import os
import re
import glob

def fix_links_in_file(file_path):
    """Fix .md links to .html links in a file"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace .md links with .html links
    # Pattern: [text](./filename.md) -> [text](./filename.html)
    pattern = r'(\[([^\]]+)\]\(([^)]+)\.md\))'
    
    def replace_link(match):
        full_match = match.group(1)
        text = match.group(2)
        url = match.group(3)
        return f'[{text}]({url}.html)'
    
    new_content = re.sub(pattern, replace_link, content)
    
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"✅ Fixed links in {file_path}")
        return True
    else:
        print(f"ℹ️  No changes needed in {file_path}")
        return False

def main():
    """Fix links in all building block README files"""
    print("🔧 Fixing .md links to .html links for GitHub Pages...\n")
    
    # Find all building block README files
    building_blocks = [
        'building-blocks/data-storage/README.md',
        'building-blocks/compute-processing/README.md',
        'building-blocks/messaging-streaming/README.md',
        'building-blocks/networking-communication/README.md',
        'building-blocks/caching-performance/README.md',
        'building-blocks/security-authentication/README.md',
        'building-blocks/monitoring-observability/README.md',
        'building-blocks/scalability-distribution/README.md'
    ]
    
    fixed_count = 0
    
    for file_path in building_blocks:
        if os.path.exists(file_path):
            if fix_links_in_file(file_path):
                fixed_count += 1
        else:
            print(f"⚠️  {file_path} not found")
    
    print(f"\n📊 Summary: Fixed links in {fixed_count} files")
    print("🎉 All building block links should now work with GitHub Pages!")

if __name__ == "__main__":
    main()
