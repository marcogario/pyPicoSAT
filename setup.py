from setuptools import setup
from distutils.extension import Extension
from datetime import datetime

PICOSAT_VERSION='960'
PICOSAT_DIR='picosat-%s' % PICOSAT_VERSION

PYPICOSAT_MINOR_VERSION='.%s' % datetime.utcnow().strftime("%y%m%d")
PYPICOSAT_VERSION='%s%s' % (PICOSAT_VERSION, PYPICOSAT_MINOR_VERSION)

picosat_ext = Extension('_picosat', ['picosat_python_wrap.c'],
                        include_dirs=[PICOSAT_DIR],
                        library_dirs=[PICOSAT_DIR],
                        libraries=['picosat'],
                        language='c',
                    )

short_description="Picosat SAT-Solver Wrapper"
long_description=\
"""
==========================
Picosat SAT-Solver Wrapper
==========================

pyPicosat provides a basic wrapping around the efficient Picosat SAT-Solver.


Picosat is developed by Armin Biere, for more information: http://fmv.jku.at/picosat/
"""


setup(name='pyPicosat',
      version=PYPICOSAT_VERSION,
      author='PySMT Team',
      author_email='info@pysmt.org',
      url='https://github.com/pysmt/pyPicoSAT/',
      license='BSD',
      description=short_description,
      long_description=long_description,
      ext_modules=[picosat_ext],
      py_modules=['picosat'],
      classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
      ],
  )
