#!/usr/bin/env python3
"""
Link checker for Engineering Ascend repository
Checks all markdown files for broken internal links
"""

import os
import re
import glob
from pathlib import Path

def extract_links_from_markdown(file_path):
    """Extract all links from a markdown file"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all markdown links: [text](url)
    link_pattern = r'\[([^\]]+)\]\(([^)]+)\)'
    links = re.findall(link_pattern, content)
    
    return [(text, url, file_path) for text, url in links]

def is_internal_link(url):
    """Check if a link is internal (relative path)"""
    return not url.startswith(('http://', 'https://', 'mailto:', '#'))

def resolve_link_path(base_file, link_url):
    """Resolve the actual file path for a relative link"""
    base_dir = os.path.dirname(base_file)
    
    # Handle different link formats
    if link_url.startswith('./'):
        link_url = link_url[2:]
    elif link_url.startswith('/'):
        # Absolute path from repository root
        return os.path.join('.', link_url[1:])
    
    # Resolve relative path
    resolved_path = os.path.join(base_dir, link_url)
    
    # Check if file exists
    if os.path.exists(resolved_path):
        return resolved_path
    
    # Check with .md extension
    if not resolved_path.endswith('.md'):
        md_path = resolved_path + '.md'
        if os.path.exists(md_path):
            return md_path
    
    return resolved_path

def check_links():
    """Check all links in markdown files"""
    print("🔍 Checking all markdown links...\n")
    
    # Find all markdown files
    markdown_files = []
    for pattern in ['**/*.md', '*.md']:
        markdown_files.extend(glob.glob(pattern, recursive=True))
    
    all_links = []
    broken_links = []
    
    # Extract all links
    for file_path in markdown_files:
        if 'node_modules' in file_path or '.git' in file_path:
            continue
            
        links = extract_links_from_markdown(file_path)
        all_links.extend(links)
    
    print(f"📄 Found {len(markdown_files)} markdown files")
    print(f"🔗 Found {len(all_links)} total links\n")
    
    # Check each internal link
    for text, url, source_file in all_links:
        if is_internal_link(url):
            resolved_path = resolve_link_path(source_file, url)
            
            if not os.path.exists(resolved_path):
                broken_links.append({
                    'text': text,
                    'url': url,
                    'source': source_file,
                    'resolved': resolved_path
                })
                print(f"❌ BROKEN: [{text}]({url})")
                print(f"   Source: {source_file}")
                print(f"   Expected: {resolved_path}")
                print()
    
    # Summary
    print("=" * 50)
    print("📊 LINK CHECK SUMMARY")
    print("=" * 50)
    print(f"✅ Total links checked: {len(all_links)}")
    print(f"❌ Broken links found: {len(broken_links)}")
    
    if broken_links:
        print("\n🔧 BROKEN LINKS TO FIX:")
        for link in broken_links:
            print(f"   - {link['source']}: [{link['text']}]({link['url']})")
    else:
        print("\n🎉 All links are working correctly!")
    
    return len(broken_links) == 0

def check_specific_files():
    """Check specific important files"""
    important_files = [
        'README.md',
        'building-blocks/README.md',
        'system-design-challenges/README.md',
        'building-blocks/data-storage/README.md',
        'building-blocks/compute-processing/README.md',
        'building-blocks/messaging-streaming/README.md',
        'building-blocks/networking-communication/README.md',
        'building-blocks/caching-performance/README.md',
        'building-blocks/security-authentication/README.md',
        'building-blocks/monitoring-observability/README.md',
        'building-blocks/scalability-distribution/README.md'
    ]
    
    print("🎯 Checking important navigation files...\n")
    
    for file_path in important_files:
        if os.path.exists(file_path):
            links = extract_links_from_markdown(file_path)
            internal_links = [link for link in links if is_internal_link(link[1])]
            
            print(f"📄 {file_path}: {len(internal_links)} internal links")
            
            for text, url, _ in internal_links:
                resolved_path = resolve_link_path(file_path, url)
                status = "✅" if os.path.exists(resolved_path) else "❌"
                print(f"   {status} [{text}]({url})")
            print()
        else:
            print(f"⚠️  {file_path} not found\n")

if __name__ == "__main__":
    print("🚀 Engineering Ascend - Link Checker")
    print("=" * 40)
    
    # Check specific important files first
    check_specific_files()
    
    print("=" * 40)
    
    # Full link check
    success = check_links()
    
    if success:
        print("\n🎉 All links are working! Ready for deployment.")
    else:
        print("\n⚠️  Please fix broken links before deploying.")
    
    print(f"\n🌐 Local server running at: http://localhost:8000")
    print("   Press Ctrl+C to stop the server")
