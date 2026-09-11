import os
import glob
import re

html_files = glob.glob('**/*.html', recursive=True)

for file in html_files:
    try:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if '[breadcrumb]' in content or '[arşiv' in content or '[blog' in content:
            print(file)
    except:
        pass
