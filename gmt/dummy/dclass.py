"""

.. module::
   :synopsis: This is a one-liner summary of the gmt.dummy.dclass module.

"""


class DClass:
    """This is just a dummy class."""

    def __init__(self):
        """Initialise a dummy object."""
        pass

    def act(self, cmd):
        """Act with given command.

        :param cmd: command to act upon
        :type cmd: str
        :raises ValueError: if `cmd` is ``None``
        """
        if cmd is None:
            raise ValueError('There is no None act.')
        print('Acting {}'.format(cmd))
