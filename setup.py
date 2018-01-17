from setuptools import setup, find_packages

setup(
    name='venusianconfiguration',
    version='1.1.1.dev0',
    description='Experiment for configuring with venusian instead of *.zcml',
    long_description=(open('README.rst').read() + '\n' +
                      open('CHANGELOG.rst').read()),
    # Get more strings from
    # http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Programming Language :: Python',
    ],
    keywords='',
    author='Asko Soukka',
    author_email='asko.soukka@iki.fi',
    url='https://github.com/datakurre/venusianconfiguration/',
    license='GPL',
    packages=find_packages('src', exclude=['ez_setup']),
    package_dir={'': 'src'},
    namespace_packages=[],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'six',
        'zope.configuration',
        'venusian>=1.0a8',
    ],
    extras_require={'test': [
        'plone.testing',
    ]},
)
