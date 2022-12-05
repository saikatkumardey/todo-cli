from setuptools import setup

setup(
    name="todo",
    version="1.0.0",
    author="Your Name",
    author_email="deysaikatkumar@gmail.com",
    description="A simple todo app",
    packages=["todo"],
    install_requires=[],
    entry_points={"console_scripts": ["todo=todo.__main__:main"]},
)
