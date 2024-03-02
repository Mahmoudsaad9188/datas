from setuptools import setup, find_packages

setup(
    name='datas',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA example python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/<username>/<datas>',
    author='<mahmoud saad>',
    author_email='<mahmoudsaad191988@gmail.com>'
)