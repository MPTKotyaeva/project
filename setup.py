from setuptools import setup, find_packages

setup(
    name="brain-games",
    version="1.0.0",
    description="A collection of simple math games",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'brain-games=scripts.brain_games:main',
            'brain-calc=scripts.brain_calc:main',
            'brain-gcd=scripts.brain_gcd:main',
        ],
    },
)
