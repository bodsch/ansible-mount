# python 3 headers, required if submitting to Ansible

from __future__ import (absolute_import, print_function)
__metaclass__ = type

from ansible.utils.display import Display

display = Display()


class FilterModule(object):
    """
        Ansible file jinja2 tests
    """

    def filters(self):
        return {
            'type': self.var_type,
            'fstypes': self.fstypes
        }

    def var_type(self, var):
        '''
          Get the type of a variable
        '''
        return type(var).__name__

    def fstypes(self, data):
        """

        """
        result = []

        display.v("- data {} {}".format(data, type(data)))

        result = [ d['fstype'] for d in data ]

        display.v("result {} {}".format(result, type(result)))

        return result
