try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = [
    'description': 'My Project',
    'author': 'My Name',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'My email.',
    'version': '0.1',
    'install_require': ['nose'],
    'packages': ['ex49'],
    'scripts': [],
    'name': 'ex49'
]

setup(**config)
