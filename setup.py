from setuptools import setup, find_packages

setup(
    name="kde_activity_launcher",
    version="0.1.0",
    description="A simple Python script to manage KDE Plasma Activities",
    author="Alice Lupariello",
    packages=find_packages(),
    install_requires=[
        "pydbus>=0.6.0",
        "PyGObject>=3.40.0"
    ],
    python_requires='>=3.8',
    entry_points={
        'console_scripts': [
            'kdeactivitylauncher=kdeactivitylauncher:main',
        ],
    },
)
