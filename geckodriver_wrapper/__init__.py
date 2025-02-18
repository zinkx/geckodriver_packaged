import os

def get_geckodriver_path():
    """Returns the absolute path to the geckodriver binary."""
    return os.path.join(os.path.dirname(__file__), "geckodriver.exe")