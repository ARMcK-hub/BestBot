import sys

def test_python_path():    
    paths = sys.path
    workspace = '/workspaces/BestBot'

    assert workspace in paths
