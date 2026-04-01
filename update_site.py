import os
import glob
import re

html_files = glob.glob('*.html')

old_footer_lines = [
    '                <div>',
    '                    <h4>Contact</h4>',
    '                    <ul>',
    '                        <li><a href="contact.html">Partner With Us</a></li>',
    '                        <li><a href="mailto:hello@strateze.com">hello@strateze.com</a></li>',
    '                        <li><a href="#">Twitter/X</a></li>',
    '                        <li><a href="#">LinkedIn</a></li>',
    '                    </ul>',
    '                </div>'
]
old_footer = '\n'.join(old_footer_lines)

new_footer_lines = [
    '                <div>',
    '                    <h4>Contact</h4>',
    '                    <ul style="margin-bottom: 24px;">',
    '                        <li><a href="contact.html">Partner With Us</a></li>',
    '                        <li><a href="mailto:contact@strateze.co">contact@strateze.co</a></li>',
    '                    </ul>',
    '                    <p style="font-size: 0.9rem; color: rgba(255,255,255,0.6); line-height: 1.5; margin-bottom: 12px;">Building a community of 40,000+ young people across digital platforms.</p>',
    '                    <ul style="display: flex; gap: 16px; flex-direction: row;">',
    '                        <li><a href="https://www.tiktok.com/@strateze" target="_blank" style="padding: 0;">TikTok</a></li>',
    '                        <li><a href="https://www.instagram.com/strateze" target="_blank" style="padding: 0;">Instagram</a></li>',
    '                    </ul>',
    '                </div>'
]
new_footer = '\n'.join(new_footer_lines)

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Replace Footer globally
    # We do a loose replacement because indentation might differ if slightly off
    # Alternative: simple replace
    if old_footer in content:
        content = content.replace(old_footer, new_footer)
    
    # 2. Replace any isolated emails
    content = content.replace("hello@strateze.com", "contact@strateze.co")
    content = content.replace("hello@strateze.co", "contact@strateze.co") # fallback
    
    # 3. Case Studies file specific
    if file == 'case-studies.html':
        content = re.sub(r'[ \t]*<a href="contact\.html" class="btn btn-outline">Enquire about this .*?</a>\n', '', content)
    
    # 4. Programs file specific
    if file == 'programs.html':
        # Find every card's closing P and div, and inject the button between them
        content = re.sub(
            r'</p>\n([ \t]*)</div>', 
            r'</p>\n\1    <a href="mailto:contact@strateze.co" class="btn btn-outline" style="margin-top: 32px; align-self: flex-start;">Enquire about this programme</a>\n\1</div>', 
            content
        )

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Update completed.")
