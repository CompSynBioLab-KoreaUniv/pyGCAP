from setuptools import setup, find_packages

setup(
    name='pgc-finder',
    version='0.0.4',
    description='Python package for probe-based gene cluster finding in large microbial genome database',
    author='jsrim',
    author_email='comfortindex@naver.com',
    url='https://github.com/jrim42/pgc-finder',
    install_requires=['pandas', 'matplotlib', 'requests'],
    packages=find_packages(),
    keywords=['gene', 'cluster', 'genomics', 'bioinformatics'],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'pgc-finder=pgc_finder.cli:main',
        ],
    },
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
)
