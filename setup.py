from setuptools import find_packages, setup

tests_require = [
    'pytest>=2.8.3',
    'pytest-cov>=2.2.0',
    'pytest-django>=2.9.1',
]

setup(
    name='django-healthchecks',
    version='0.7.1',
    description="Simple Django app/framework to publish health checks",
    long_description=open('README.rst', 'r').read(),
    url='https://github.com/mvantellingen/django-healthchecks',
    author="Michael van Tellingen",
    author_email="michaelvantellingen@gmail.com",
    install_requires=[
        'Django>=1.7',
        'six>=1.1',
    ],
    tests_require=tests_require,
    extras_require={'test': tests_require},
    use_scm_version=True,
    entry_points={},
    package_dir={'': 'src'},
    packages=find_packages('src'),
    include_package_data=True,
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.7',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    zip_safe=False,
)
