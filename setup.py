from setuptools import setup

setup(
    name = "uk",
    version = "0.1.0",
    description = "Prints UK flag",
    author = "AitzazImtiaz",
    url = "https://github.com/AitzazImtiaz/uk",
    packages = ["uk"],
    entry_points = {
        'console_scripts': [
            'uk = uk.__main__:main'
        ]
    },
)
