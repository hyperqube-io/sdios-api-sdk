from setuptools import find_packages, setup

setup(
    name='sdios',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'colorama>=0.3.9',
        'requests>=2.18.4',
        'semantic-version>=2.6.0',
        'typing>=3.6.2',
    ],
    license='MIT License',
    description='SDI OS API SDK',
    url='https://github.com/hyperqube-io/sdios-api-sdk',
    author='Hyperqube Technologies, Inc.',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
