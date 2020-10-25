from setuptools import setup

setup(
    name='journal',
    version='0.0',
    license='MIT',
    packages=['journal'],
    url = 'https://github.com/GillesArcas/journal',
    author = 'Gilles Arcas',
    author_email = 'gilles.arcas@gmail.com',
    entry_points = {
        'console_scripts': ['journal=journal.journal:main'],
    },
    zip_safe=False
)