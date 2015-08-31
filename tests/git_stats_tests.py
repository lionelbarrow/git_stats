from nose.tools import *

from git_stats.grapher import Grapher
from git_stats.cache import Cache

def test_basic():
    history = Cache("~/bt/authy").fetch_history()
    Grapher(history).files_over_time()

