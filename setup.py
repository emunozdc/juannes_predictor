from setuptools import setupsetup(      name='CavPred',      version='1.0.0',      description='This package predicts the possible binding sites of a pdb protein using a geometrical approach.',      author='Anna Basquet, Juana Munoz, Ester Munoz',      author_email='anna.basquet01@estudiant.upf.edu, juanacamila.munoz01@estudiant.upf.edu, ester.munoz01@estudiant.upf.edu',      url='https://github.com/emunozdc/juannes-predictor',      packages=['cavpred', 'cavpred.preprocess', 'cavpred.grid', 'cavpred.voronoi'],      install_requires=['numpy', 'pyKVFinder', 'Bio', 'MDAnalysis', 'scipy', 'matplotlib'],      classifiers=['Programming Language :: Python :: 3.10']      )