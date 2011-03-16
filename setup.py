from setuptools import setup, find_packages


setup(
    name='django-beanstalkd',
    version='0.2',
    description='A convenience wrapper for beanstalkd clients and workers '
                'in Django using the beanstalkc library for Python',
    long_description=open('README.md').read(),
    author='Jonas VP',
    author_email='jvp@jonasundderwolf.de',
    url='http://github.com/jonasvp/django-beanstalkd',
    license='MPL',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=['pyyaml', 'beanstalkc'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
