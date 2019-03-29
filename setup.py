from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pedestrian_detection_ssdlite',
    version='0.0.1',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    ],
    url='https://github.com/cftang0827/pedestrian_detection_ssdlite',
    author='cftang0827',
    author_email='cftang0827@gmail.com',
    license='MIT',
    packages=['pedestrian_detection_ssdlite'],
    package_dir={
        "pedestrian_detection_ssdlite": "pedestrian_detection_ssdlite"
    },
    package_data={'pedestrian_detection_ssdlite': ['*.pb']},
    install_requires=[
        'tensorflow',
        'numpy',
    ],
    include_package_data=True,
    zip_safe=False)
