from setuptools import setup

setup(
    name='github-events-cli',
    version='0.1',
    py_modules=['github_events'],
    install_requires=['requests'],
    entry_points={
        'console_scripts': [
            'github-events=github_events:main',
        ],
    },
)
