from setuptools import setup, find_namespace_packages

setup(
    name='clean',
    version='1',
    description='',
    url='',
    author='',
    author_email='olgapasichnyuk@gmail.com',
    license='MIT',
    packages=find_namespace_packages(),
    entry_points={'console_scripts': ['cleanfolder: = clean_folder.clean:main', ]}
)
