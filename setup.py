import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

VERSION = '0.0.1'
PACKAGE_NAME = 'gpt-terminal'
AUTHOR = 'Franz Geffke'
AUTHOR_EMAIL = 'm@f-a.nz'
URL = 'https://github.com/franzos/gpt-terminal'

LICENSE = ''
DESCRIPTION = 'OpenAI GPT-based terminal assistant'
LONG_DESCRIPTION = (HERE / "README.md").read_text()
LONG_DESC_TYPE = 'text/markdown'

INSTALL_REQUIRES = [
    'openai',
]

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESC_TYPE,
    author=AUTHOR,
    license=LICENSE,
    author_email=AUTHOR_EMAIL,
    url=URL,
    install_requires=INSTALL_REQUIRES,
    entry_points = {
        'console_scripts': ['gpt-terminal=gpt_terminal.main:main'],
    },
    packages=find_packages(),
    zip_safe=False
)
