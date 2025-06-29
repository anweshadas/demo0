#!/usr/bin/python
# pylint: disable=E0401
# add.py - A custom module plugin for Ansible.
# Author: Anwesha Das(@anweshadas)
# License: GPL-3.0-or-later
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, annotations, division, print_function


DOCUMENTATION = """
    module: add
    author: Anwesha Das(@anweshadas)
    version_added: "0.0.1"
    short_description: A simple module plugin for Ansible to learn.
    description:
      - This is a demo module plugin designed to return result of addition of numbers.
    options:
      number1:
        description: number1
        required: True
        type: int
      number2:
        description: number2
        required: True
        type: int
"""

EXAMPLES = """
# add module example

- name: Add to numbers
  register: result
  anweshadas.demo0.add:
    number1: 3
    number2: 3

- name: Print the result
  ansible.builtin.debug:
    msg: "{{ result.answer }}"
"""

RETURN = """
answer:
  description:
  - The result of addtion.
  returned: on success
  sample: 6
  type: int
"""


__metaclass__ = type  # pylint: disable=C0103

from typing import TYPE_CHECKING

from ansible.module_utils.basic import AnsibleModule  # type: ignore


if TYPE_CHECKING:
    from typing import Callable


def main() -> None:
    """entry point for module execution"""
    argument_spec = {}
    argument_spec.update(
        number1=dict(type='int', required=True),
        number2=dict(type='int', required=True),
    )

    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
    )

    number1 = module.params["number1"]
    number2 = module.params["number2"]
    answer = number1 + number2
    module.exit_json(changed=False, answer=answer)


if __name__ == "__main__":
    main()
