from setuptools import setup, find_packages

setup(
    name="geckodriver-wrapper",
    version="0.2",
    packages=find_packages(),  # Ensures Python finds the package
    include_package_data=True,  # Includes non-Python files like .exe
    package_data={"geckodriver_wrapper": ["geckodriver.exe"]},  # Explicitly include binary
    description="A packaged version of geckodriver for offline use.",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
    ],
)