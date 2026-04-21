from setuptools import setup, find_packages

setup(
    name='your_package_name',
    version='0.1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'your_command=your_module:main_function',
        ],
    },
    install_requires=[
        # List your package dependencies here
    ],
)