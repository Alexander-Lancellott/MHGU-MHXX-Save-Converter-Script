from setuptools import setup, find_packages

setup(
    name='MHXX-MHGU-Save-Converter-Script',
    author='Alexander-Lancellott',
    author_email='alejandrov.lancellotti@gmail.com',
    version='1.0.0',
    packages=find_packages(),
    install_requires=['readchar', 'pyinstaller', 'art==6.1'],
    python_requires='>=3.12',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'build = modules.build:main',
        ],
    },
)
