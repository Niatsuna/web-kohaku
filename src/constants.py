from os import walk
from os.path import basename, dirname, join
import importlib.util

GAMES = []
for dirpath, dirnames, filenames in walk(join(dirname(__file__), 'games')):
    for filename in [f for f in filenames if f == 'main.py']:
        path = join(dirpath, filename)
        game = basename(dirpath)
        spec = importlib.util.spec_from_file_location(game, path)
        foo = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(foo)
        GAMES.append((game, foo))