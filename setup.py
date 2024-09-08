# setup.py

from setuptools import setup, find_packages

setup(
    name="credito",  # The name of your package
    version="3.2.5",  # Initial version
    author="James-Beans",
    author_email="hello@jamesdev.xyz",
    description="A Python module to display credits on pressing CTRL + O",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/james-beans/credito",  # Optional: GitHub link
    packages=find_packages(),
    include_package_data=True,  # Include non-code files like credits.cfg
    package_data={
        # Include any files in the "data" subfolder under "credito"
        "": ["data/*.cfg"],
    },
    install_requires=[
        # List of dependencies
        "keyboard",  # Add other dependencies here if needed
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: Microsoft :: Windows",
    ],
    python_requires=">=3.12",
)
