usage = '''
Jets CLI.
Usage:
  app.py help
  app.py view
  app.py create <title> <note>
'''

from model import *
from docopt import docopt
from commands import *
    
args = docopt(usage)

if args['help']:
    help()

if args['view']:
    view()

if args['create']:
  title = args['<title>']
  note = args['<note>']
  create(title, note)

    