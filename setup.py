from setuptools import setup, find_packages

setup(
    name="easyml",
    version="0.1.0",
    description="A one-liner ML training and deployment library",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/YOUR_GITHUB_USERNAME/easyml",
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
    python_requires='>=3.7',
)
