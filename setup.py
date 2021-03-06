from setuptools import setup

setup(
    zip_safe=False,
    version=open('VERSION').read().strip(),
    entry_points={
        'console_scripts': [
            'spellchecker = mlmorph_spellchecker.__main__:main'
        ],
    },
    test_suite = 'tests'
)