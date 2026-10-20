import os, glob, sys
from html.parser import HTMLParser

sys.stdout.reconfigure(encoding='utf-8')
base_dir = r'C:\Users\orkun\.gemini\antigravity\scratch\fenix-static-final'

VOID_ELEMENTS = {
    'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 
    'link', 'meta', 'param', 'source', 'track', 'wbr'
}

class TagValidator(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.errors = []
    
    def handle_starttag(self, tag, attrs):
        if tag.lower() not in VOID_ELEMENTS:
            self.stack.append((tag.lower(), self.getpos()))
    
    def handle_endtag(self, tag):
        tag = tag.lower()
        if tag in VOID_ELEMENTS:
            return
        if not self.stack:
            self.errors.append(f"Unexpected end tag </{tag}> at line {self.getpos()[0]}")
            return
        top_tag, top_pos = self.stack[-1]
        if top_tag == tag:
            self.stack.pop()
        else:
            # Check if tag is in stack
            tag_indices = [i for i, (t, _) in enumerate(self.stack) if t == tag]
            if tag_indices:
                unclosed = [t for t, _ in self.stack[tag_indices[-1]:]]
                self.errors.append(f"Mismatched end tag </{tag}> at line {self.getpos()[0]}, expected one of {unclosed}")
                self.stack = self.stack[:tag_indices[-1]]
            else:
                self.errors.append(f"Unmatched end tag </{tag}> at line {self.getpos()[0]}")

all_files = glob.glob(os.path.join(base_dir, 'pages', '*.html')) + [os.path.join(base_dir, 'index.html')]
total_errs = 0

for fpath in all_files:
    fname = os.path.relpath(fpath, base_dir)
    with open(fpath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    validator = TagValidator()
    try:
        validator.feed(html)
    except Exception as e:
        print(f"Exception parsing {fname}: {e}")
        total_errs += 1
        continue
    
    if validator.errors:
        print(f"Errors in {fname}: {len(validator.errors)}")
        for err in validator.errors[:3]:
            print(f"  {err}")
        total_errs += len(validator.errors)

if total_errs == 0:
    print(f"PERFECT: All {len(all_files)} HTML files parsed with 0 unclosed/mismatched tag errors!")
else:
    print(f"Validation completed with {total_errs} errors across files.")
