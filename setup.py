try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
        'description': 'module to watch trade sites online for items with specific keywords',
        'author': 'Schmeegy, Wizard, Wonderboy',
        'URL': 'nil',
        'download_url': 'nil',
        'author_email': 'nil',
        'version': '0.1',
        'install_requires': ['nose'],
        'packages': ['beautifulsoup4','webwatcher'],
        'scripts': [],
        'name': 'WebWatcher'
        }

setup(**config)
