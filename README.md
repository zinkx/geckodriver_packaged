# Geckodriver Wrapper

This package provides a wrapped version of `geckodriver.exe` for use in offline environments.

## Installation
```bash
pip install geckodriver-wrapper
```

## Usage
```python
from geckodriver_wrapper import get_geckodriver_path
from selenium import webdriver

driver = webdriver.Firefox(executable_path=get_geckodriver_path())
driver.get("https://example.com")
```

## Driver Source
Driver Release: https://github.com/mozilla/geckodriver/releases/tag/v0.35.0 geckodriver-v0.35.0-win32.zip

## Driver Licence
Driver License: https://github.com/mozilla/geckodriver?tab=MPL-2.0-1-ov-file#readme MPL-2.0 license



