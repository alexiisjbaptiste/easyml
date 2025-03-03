from setuptools import setup, find_packages

setup(
    name="easyml",  # Package name (users will install with pip install easyml)
    version="0.1.0",  # Update version as needed
    description="A lightweight, one-liner ML training and deployment library",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/YOUR_GITHUB_USERNAME/easyml",  # GitHub repo
    packages=find_packages(),
    install_requires=[
        "pandas",
        "scikit-learn",
        "xgboost",
        "fastapi",
        "uvicorn",
        "joblib"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
