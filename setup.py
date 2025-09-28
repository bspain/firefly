"""
Setup script for Firefly Financial Planning Application
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="firefly",
    version="1.0.0",
    author="Firefly Development Team",
    author_email="dev@firefly.example.com",
    description="Financial Independence and Retirement Planning Application",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bspain/firefly",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Office/Business :: Financial",
        "Topic :: Office/Business :: Financial :: Investment",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "firefly=main:cli",
        ],
    },
    keywords="finance, retirement, planning, investment, FIRE",
    project_urls={
        "Bug Reports": "https://github.com/bspain/firefly/issues",
        "Source": "https://github.com/bspain/firefly",
    },
)