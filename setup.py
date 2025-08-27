from setuptools import setup

setup(
    name='github-events',
    version='0.1',
    py_modules=['app'],
    install_requires=['requests'],
    entry_points={
        'console_scripts': [
            'github-events=app:main',
        ],
    },
)
