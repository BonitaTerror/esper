from setuptools import setup


readme = open('README.rst').read()

setup(name='esper',
      version='0.9.9',
      author='Benjamin Moran',
      author_email='benmoran@protonmail.com',
      description=__doc__.splitlines()[0],
      license='MIT',
      keywords='ecs,entity component system,game',
      url='https://github.com/benmoran56/esper',
      download_url='https://github.com/benmoran56/esper/releases',
      platforms='POSIX, Windows, MacOS X',
      py_modules=['esper'],
      classifiers=[
            "Development Status :: 4 - Beta",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
            "Programming Language :: Python",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.4",
            "Programming Language :: Python :: 3.5",
            "Programming Language :: Python :: 3.6",
            "Topic :: Games/Entertainment",
            "Topic :: Software Development :: Libraries :: Python Modules",
      ])
