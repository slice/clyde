clyde
=====

clyde is a Pylint_ plugin for code that uses Discord.py_.

.. _Pylint: https://www.pylint.org
.. _Discord.py: https://discordpy.readthedocs.io/en/latest

Installation
------------

.. code:: sh

    python3 -m pip install -U git+https://github.com/slice/clyde@master#egg=clyde

Usage
-----

Add the following to your ``~/.pylintrc``::

    [MASTER]
    load-plugins=clyde

Checkers
--------

missing-cog-listener (W7001)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Warns against missing ``@Cog.listener()`` decorators in cog event listeners.

Example:

.. code:: python3

    class Sample(Cog):
        async def on_message(self, msg):
            ...

.. WARNING::
    Unfortunately, this checker only works for the built-in events dispatched by
    the library. It's up to you to put the decorator on your own events.
