from setuptools import setup, find_packages

setup(
    name='lp-palettes',
    version='0.1.0',
    author='Shaojun Xie',
    author_email='xieshaojun0526@gmail.com',
    description='A Python package for color palettes for lets-plot.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/xie186/lp-palettes',
    packages=find_packages(),
    install_requires=[
        'lets-plot',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    python_requires='>=3.7',
)
