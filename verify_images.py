import os
import re
base = r"c:\Users\Paulinus Kingsley\OneDrive\Apps\Walk for Peace"
missing = []
for fname in os.listdir(base):
    if fname.endswith('.html'):
        path = os.path.join(base, fname)
        text = open(path, encoding='utf-8').read()
        for match in re.findall(r"['\"](images/[^'\"]+)['\"]", text):
            imgpath = os.path.join(base, match)
            if not os.path.exists(imgpath):
                missing.append((fname, match))
print('Missing references:', missing)
