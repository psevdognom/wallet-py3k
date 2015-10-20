from distutils.core import setup

version = __import__('wallet').__version__
install_requires = open('requirements.txt').readlines(),

setup(
    name='wallet-py3k',
    version=version,
    author='Fernando Aramendi',
    author_email='fernando@devartis.com',
    packages=['wallet', 'wallet.test'],
    url='http://github.com/devartis/passbook/',
    license=open('LICENSE.txt').read(),
    description='Passbook file generator',
    long_description=open('README.md').read(),

    install_requires=install_requires,

    classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.5 :: Only',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
