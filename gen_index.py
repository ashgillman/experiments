#!/usr/bin/env python3

from pathlib import Path
from datetime import datetime

html_format = """<body>
<h1>Private Repository of Ashley Gillman</h1>
{}
<p><i>Generated {}</i></p>
</body>
""".format
site = '.'
doc_links = ['*.pdf']
link_format = '<p><a href="./{0}">{0}</a></p>'.format

hard_links = '<p><a href="/" onclick="javascript:event.target.port=8888;event.target.protocol=\'https:\'">iPython Notebook</a></p>'
subdir_links = '\n'.join(sorted([link_format(d.name)
                                 for d in Path(site).iterdir()
                                 if d.is_dir()]))
file_links = '\n'.join(sorted([link_format(f.name)
                               for pattern in doc_links
                               for f in Path(site).glob(pattern)]))

html = html_format( '\n'.join([hard_links, subdir_links, file_links]),
                   datetime.now().strftime('%d %b, %Y'))

with open(str(Path(site, 'index.html')), 'w+') as f:
    f.write(html)
