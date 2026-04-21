from setuptools import setup, find_packages

setup(
    name='offline-ai-autopilot',
    version='0.2.0',
    packages=find_packages(),
    install_requires=[
        'typer',
        'requests',
        'click',
        'rich',
    ],
    extras_require={
        'dev': ['pytest', 'black', 'flake8'],
        'ollama': ['ollama-sdk'],
    },
    entry_points={
        'console_scripts': [
            'offline-ai-autopilot=offline_ai_autopilot.main:main',
        ],
    },
    author='Your Name',
    author_email='your.email@example.com',
    description='A package for offline AI autopilot functionality',
    url='https://github.com/greeneyedbeautty/offline-ai-autopilot',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)