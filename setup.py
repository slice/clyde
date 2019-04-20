import setuptools

setuptools.setup(
    name='clyde',
    version='0.0.0',
    author='slice',
    description='A Pylint plugin for Discord.py',
    install_requires=[
        'pylint',
        'astroid'
    ],
    packages=setuptools.find_packages()
)
