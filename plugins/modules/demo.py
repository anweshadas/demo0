#!/usr/bin/python
# pylint: disable=E0401
# demo.py - A custom module plugin for Ansible.
# Author: Anwesha Das(@anweshadas)
# License: GPL-3.0-or-later
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, annotations, division, print_function


DOCUMENTATION = """
    module: demo
    author: Anwesha Das (@anweshadas)
    version_added: "0.0.1"
    short_description: A demo module plugin for Ansible following the ADT development guide.
    description:
      - This is a demo module plugin designed to return Hello message.
    options:
      name:
        description: Value specified here is appended to the Hello message.
        type: str
"""

EXAMPLES = """
# demo module example

- name: Display a hello message
  ansible.builtin.debug:
    msg: "{{ 'ansible-creator' | demo }}"
"""

RETURN = r"""
text:
  description:
  - Hello name.
  returned: on success
  sample: Hello, Ansible
  type: str
"""

__metaclass__ = type  # pylint: disable=C0103

from typing import TYPE_CHECKING

from ansible.module_utils.basic import AnsibleModule  # type: ignore


if TYPE_CHECKING:
    from typing import Callable


def _sample_module(name: str) -> str:
    """Returns Hello message.

    Args:
        name: The name to greet.

    Returns:
        str: The greeting message.
    """
    return "Hello, " + name


def main() -> None:
    """entry point for module execution"""
    argument_spec = dict(
        name=dict(type="str"),
    )
    module = AnsibleModule(
        argument_spec=argument_spec,
    )

    res = _sample_module(module.params["name"])

    result = {"changed": False, "text": res}
    module.exit_json(**result)


if __name__ == "__main__":
    main()
