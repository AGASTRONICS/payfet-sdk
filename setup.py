from setuptools import setup, find_packages

setup(
    name='payfet',
    version='1.0.0',
    description='Official Python SDK for interacting with the Payfet Fintech Infrastructure Platform',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Abdulsamad Opeyemi Abdulganiyu',
    author_email='agastronics@gmail.com',
    url='https://github.com/AGASTRONICS/payfet-sdk',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'requests',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires='>=3.7',
)
