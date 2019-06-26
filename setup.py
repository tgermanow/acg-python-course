from setuptools import setup

setup(
    name='acg-python-course learning project',
    version='0.1',
    author='John Doe',
    author_email='john.doe@example.com',
    description='something, something, something...',
    license='GPLv3',
    packages=['shotty'],
    url='example.com/project-page',
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        shotty=shotty.shotty:cli
    ''',    
)