import re
import os

filepath = os.path.join('collections', 'index.html')

with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()

# The pattern is:
# <h3 style="font-size: var(--font-size-md); color: var(--color-text-primary); margin-bottom: var(--space-xs);">Clothing & Apparel</h3><p style="font-size: var(--font-size-sm); color: var(--color-text-secondary); margin-bottom: var(--space-md);">Export products, variants, dimensions, and image links.</p>

def replace_desc(match):
    h3_start = match.group(1)
    niche = match.group(2)
    h3_end = match.group(3)
    p_start = match.group(4)
    desc = match.group(5)
    p_end = match.group(6)
    
    # Generate unique description
    new_desc = f"Export comprehensive {niche} catalogs, including niche-specific variants, dimensions, and high-res image galleries."
    
    return f"{h3_start}{niche}{h3_end}{p_start}{new_desc}{p_end}"

# Regex to capture the parts
# (h3 tag start)(niche text)(h3 tag end)(p tag start)(desc text)(p tag end)
pattern = re.compile(r'(<h3[^>]*>)(.*?)(</h3>\s*)(<p[^>]*>)(.*?)(</p>)')
new_html = pattern.sub(replace_desc, html)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Collections index descriptions updated.")
