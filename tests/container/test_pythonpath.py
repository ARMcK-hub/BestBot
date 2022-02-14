import sys

def test_python_path():    
    paths = sys.path
    workspace = '/workspaces/bestbot'

    assert workspace in paths
