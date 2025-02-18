from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="geckodriver-wrapper",
    version="0.4",
    packages=find_packages(),
    include_package_data=True,
    package_data={"geckodriver_wrapper": ["geckodriver.exe"]},
    description="A packaged version of geckodriver for offline use.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zinkx/geckodriver_packaged",  # GitHub repo URL
    project_urls={
        "Documentation": "https://github.com/zinkx/geckodriver_packaged#readme",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
    ],
)