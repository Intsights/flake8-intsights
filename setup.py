import setuptools


setuptools.setup(
    name='flake8-intsights',
    version='0.1.3',
    author='Gal Ben David',
    author_email='gal@intsights.com',
    url='https://github.com/Intsights/flake8-intsights',
    project_urls={
        'Source': 'https://github.com/Intsights/flake8-intsights',
    },
    license='MIT',
    description='Uncompromising and opinionated flake8 plugin which follows Intsights\' practices',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='flake8 conventions style lint linter intsights',
    python_requires='>=3.6',
    zip_safe=False,
    install_requires=[
        'astroid',
        'flake8',
        'flake8-assertive',
        'flake8-comprehensions',
    ],
    packages=[
        'flake8_intsights',
        'flake8_intsights.checkers',
    ],
    entry_points={
        'flake8.extension': [
            'I = flake8_intsights.checker:Checker',
        ],
    },
)
