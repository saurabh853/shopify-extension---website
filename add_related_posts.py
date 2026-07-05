import os
import glob
import re
import random

# Get all blog post paths (excluding index.html)
blog_dir = 'blog'
html_files = [f for f in glob.glob(os.path.join(blog_dir, '*.html')) if os.path.basename(f) != 'index.html']

# Parse all posts to build a dictionary of URL -> Title
posts = {}
title_pattern = re.compile(r'<h1 class="blog-post__title">(.*?)</h1>')

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    match = title_pattern.search(content)
    if match:
        filename = os.path.basename(filepath)
        url = f"/blog/{filename}"
        title = match.group(1).strip()
        posts[filepath] = {"url": url, "title": title}
    else:
        print(f"Warning: No title found in {filepath}")

# Now inject related posts into each file
all_filepaths = list(posts.keys())

for filepath in all_filepaths:
    # Pick 4 random posts that are not the current post
    available_posts = [p for p in all_filepaths if p != filepath]
    sampled_posts = random.sample(available_posts, min(4, len(available_posts)))
    
    related_html = "\n        <!-- Related Posts -->\n        <h2>Related Posts</h2>\n        <ul>\n"
    for sp in sampled_posts:
        related_html += f'          <li><a href="{posts[sp]["url"]}">{posts[sp]["title"]}</a></li>\n'
    related_html += "        </ul>\n\n"
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Find the injection point: before "        <!-- CTA Box -->"
    inject_point = "        <!-- CTA Box -->"
    if inject_point in content:
        new_content = content.replace(inject_point, related_html + inject_point)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
    else:
        print(f"Warning: CTA Box not found in {filepath}")

print(f"Successfully processed {len(all_filepaths)} blog posts.")
