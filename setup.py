from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()
with open('HISTORY.rst') as f:
    history = f.read()

setup(
    name='cubiscan',
    use_scm_version=True,
    description='Library to talk to cubiscan machines',
    long_description=readme + '\n\n' + history,
    author='Camptocamp',
    author_email='info@camptocamp.com',
    url='https://github.com/camptocamp/cubiscan',
    license='LGPLv3+',
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=['future', 'unicodecsv'],
    setup_requires=[
        'setuptools_scm',
    ],
    classifiers=(
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: '
        'GNU Lesser General Public License v3 or later (LGPLv3+)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
    ),
)
