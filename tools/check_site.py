"""Static checks for this buildless site. Run: python tools/check_site.py"""
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]

class Page(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.ids, self.links, self.images, self.tags = [], [], [], []
        self.current = 0
        self.feed(path.read_text(encoding='utf-8-sig'))

    def handle_starttag(self, tag, attributes):
        a = dict(attributes)
        self.tags.append(tag)
        if 'id' in a:
            self.ids.append(a['id'])
        if a.get('aria-current') == 'page':
            self.current += 1
        if tag == 'img':
            self.images.append(a)
        for key in ('href', 'src'):
            if key in a:
                self.links.append(a[key])

pages = {p: Page(p) for p in ROOT.rglob('*.html')}
errors = []
checked = 0
for path, page in pages.items():
    name = path.relative_to(ROOT).as_posix()
    if page.tags.count('main') != 1 or page.tags.count('h1') != 1:
        errors.append(f'{name}: expected one main and h1')
    if page.current != 1:
        errors.append(f'{name}: expected one current navigation item')
    if any(n > 1 for n in Counter(page.ids).values()):
        errors.append(f'{name}: duplicate IDs')
    if len(page.images) != (1 if name == 'index.html' else 0):
        errors.append(f'{name}: portrait must occur only on root index.html')
    for image in page.images:
        if not image.get('alt') or not image.get('width') or not image.get('height'):
            errors.append(f'{name}: image missing alt or dimensions')
    for link in page.links:
        u = urlsplit(link)
        if u.scheme or u.netloc:
            continue
        target = (path.parent / unquote(u.path)).resolve() if u.path else path
        if target.is_dir():
            target /= 'index.html'
        checked += 1
        if not target.exists():
            errors.append(f'{name}: missing {link}')
        elif u.fragment and target in pages and unquote(u.fragment) not in pages[target].ids:
            errors.append(f'{name}: missing anchor {link}')
print(f'{len(pages)} pages; {checked} local links/assets/anchors checked.')
if errors:
    raise SystemExit('\n'.join(errors))
print('PASS: landmarks, navigation, unique IDs, image policy and local links.')
