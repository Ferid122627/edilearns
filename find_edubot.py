import re

path = 'index.html'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

lines = content.split('\n')
for i, line in enumerate(lines):
    if 'edubot' in line.lower() or 'agent hub' in line.lower():
        # print first 50 chars to avoid encoding errors
        print(f"{i+1}: {line.strip()[:50]}")
