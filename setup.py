from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="launchpad_rgb",
    version="1.0.0",
    description="Easily make MIDI messages that take advantage of the 24 bit RGB LEDs on a Novation Launchpad MK2",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/HitmanBobina47/launchpad_rgb",
    author="HitmanBobina47",
    author_email="hitmanbobina47@gmail.com",
    project_urls={
        'Bug Reports': 'https://github.com/HitmanBobina47/launchpad_rgb/issues',
        'Funding': 'https://paypal.me/HitmanBobina47',
        'Source': 'https://github.com/HitmanBobina47/launchpad_rgb'
    }
)
