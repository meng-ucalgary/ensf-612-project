`skeleton` is similar to the template part of PasteScript_ but 
without any dependencies; it is also compatible with Python 3.

Requirements
============

- Python 2.6 or 3.1

It currently only has been tested with Python 2.6 and 3.1 on Mac OSX.


Installation
============

The easiest way to get skeleton is if you have setuptools / distribute_ or pip_ installed::

	easy_install skeleton

or::

	pip install skeleton

The current development version can be found at 
http://github.com/dinoboff/skeleton/tarball/master.


Usage example
=============

Let's create a basic module template; one with a `setup.py`, a `README` and the 
module files.

First, create the skeleton script layout::

	mkmodule.py
	basic-module/README
	basic-module/setup.py_tmpl
	basic-module/{module_name}.py

`mkmodule.py`
-------------

`mkmodule.py` is the script that create new modules::


	#!/usr/bin/env python
	"""
	Basic script to create an empty python package containing one module
	"""
	from skeleton import Skeleton, Var


	class BasicModule(Skeleton):
	    """
	    Create an empty module with its etup script and a README file.
	    """
	    src = 'basic-module'
	    variables = [
	        Var('module_name'),
	        Var('author'),
	        Var('author_email'),
	        ]


	def main():
	    """Basic command line bootstrap for the BasicModule Skeleton"""
	    BasicModule.cmd()

	if __name__ == '__main__':
	    main()


The `src` attribute sets the relative path to the skeleton directory where the 
script will find the files and directories to create.

The `variables` attribute list the variables the templates will require.
The variables with a default can be left blank by the user.

`Skeleton.cmd()` is a convenient method to set an optparser and 
the logging basic config, and to apply the skeleton::


	Usage: mkmodule.py [options] dst_dir

	Options:
	  -h, --help            show this help message and exit
	  -q, --quiet           
	  -v, --verbose         
	  -d, --debug           
	  --module-name=NAME    Module Name
	  --author=AUTHOR       Author
	  --author-email=EMAIL  Author Email


If you needed to run a `Skeleton` yourself, you would use the 
constructor, the `update` or `__setitem__` methods to set the variables
(`Skeleton` is a `dict` subclass), and the `write(dst_dir)` or `run(dst_dir)`
methods to apply the skeleton. `write()` will raise a `KeyException` if a 
variable is not set; `run()` will prompt the user for the missing variables


`basic-module/README`
---------------------

`README` a is static file that will simply be copied::

	TODO: write the description of this module.
	
`basic-module/setup.py_tmpl`
----------------------------

`setup.py_tmpl` is a template (it ends with the _tmpl suffix) that will be used
to create a `setup.py` file::

	#!/usr/bin/env python

	from distutils.core import setup


	PROJECT = {module_name!r}
	VERSION = '0.1'
	AUTHOR = {author!r}
	AUTHOR_EMAIL = {author_email!r}
	DESC = "A short description..."

	setup(
	    name=PROJECT,
	    version=VERSION,
	    description=DESC,
	    long_description=open('README.rst').read(),
	    author=AUTHOR,
	    author_email=AUTHOR_EMAIL,
	    py_module=[{module_name!r},],
	)

By default, `Skeleton` uses python 2.6+ `string formatting`_.

`basic-module/{module_name}.py`
-------------------------------

`{module_name}.py` is the module file for which the name will be set dynamically
at run time.

.. NOTE::
	All file names are formatted using `Skeleton.template_formatter` method.
	Watch out for special characters (with the default formatter,
	use `{{` to render `{` and `}}` for `}` - unless you want to render
	a variable).

Extra
=====

`skeleton` includes a skeleton for a basic package layout, you can 
run it with::

	python -m skeleton.examples.basicpackage <dst_dir>

or with `virtualenvwrapper.project`. Install it::

	pip install skeleton[virtualenv-templates]

Configure virtualenvwrapper_ and virtualenwrapper.project_; then,
create a new project::

	mkproject -t package <project name>


Todo:
=====

- add more examples.


Development
===========

Report any issues and fork `squeleton` at
http://github.com/dinoboff/skeleton/ .



.. _PasteScript: http://pythonpaste.org/script/
.. _pip: http://pip.openplans.org/
.. _distribute: http://packages.python.org/distribute/
.. _string formatting: http://docs.python.org/library/functions.html#format
.. _virtualenwrapper.project: http://www.doughellmann.com/projects/virtualenvwrapper.project/
.. _virtualenvwrapper: http://www.doughellmann.com/projects/virtualenvwrapper/
