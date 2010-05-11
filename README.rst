===================
c2c.recipe.jsconfig
===================

Requirements
------------

Requires zc.buildout.

Installation
------------

c2c.recipe.jsconfig is a `zc.buildout <http://pypi.python.org/pypi/zc.buildout>`_
recipe which generates a javascript configuration file based on key/value pairs
from the buildout configuration.

**Installing using easy_install**::

    $ easy_install c2c.recipe.jsconfig
    
**Manual installation for development**:

Download the source code as `archive <http://github.com/camptocamp/c2c.recipe.jsconfig/zipball/master>`_
or clone the GIT repository::

    git clone http://github.com/camptocamp/c2c.recipe.jsconfig.git
    
Then run the setup::

    cd c2c.recipe.jsconfig
    python setup.py develop

Usage in buildout
-----------------

Create a buildout.cfg file which contains the following::

    [buildout]
    parts = jsconfig

    [jsconfig]
    recipe = c2c.recipe.jsconfig
    output = path/to/Config.js
    namespace = App
    key1 = value1
    key2 = value2

Then launch the buildout command::

    $ buildout

And voilà!
Your path/to/Config.js javascript configuration file has been
generated successfully.

