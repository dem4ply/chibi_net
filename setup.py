try:
    from setuptools import setup, find_packages
except:
    from distutils.core import setup, find_packages

# here = os.path.abspath( os.path.dirname( __file__ ) )
# README = open(os.path.join( here, 'README.rst' ) ).read()

setup(name='chibi_net',
      version='0.1',
      description='',
      # long_description=README,
      license='',
      author='',
      author_email='',
      packages=find_packages(),
      install_requires=[
          #'chibi_file==0.1',
      ],
      dependency_links = [
          'git+https://github.com/dem4ply/chibi_file.git@master#egg=chibi_file-0.1',
      ],
      classifiers=[
          'Environment :: Console',
          'Intended Audience :: Developers',
          'Programming Language :: Python',
      ])
