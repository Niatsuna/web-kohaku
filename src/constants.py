from os import environ, walk
from os.path import basename, dirname, join
import importlib.util
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

DB_USER = environ.get('KOHAKU_DB_USER')
DB_PASSWORD = environ.get('KOHAKU_DB_PASSWORD')
DB_URL = environ.get('KOHAKU_DB_URL')

GAMES = []
for dirpath, dirnames, filenames in walk(join(dirname(__file__), 'games')):
    for filename in [f for f in filenames if f == 'main.py']:
        path = join(dirpath, filename)
        game = basename(dirpath)
        spec = importlib.util.spec_from_file_location(game, path)
        foo = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(foo)
        GAMES.append((game, foo))