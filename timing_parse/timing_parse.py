#!/usr/bin/env python
"""Test ways of parsing cesm timing files from a template

Author: Ben Andre <andre@ucar.edu>

"""

from __future__ import print_function

import sys

if sys.hexversion < 0x02070000:
    print(70 * "*")
    print("ERROR: {0} requires python >= 2.7.x. ".format(sys.argv[0]))
    print("It appears that you are running python {0}".format(
        ".".join(str(x) for x in sys.version_info[0:3])))
    print(70 * "*")
    sys.exit(1)

#
# built-in modules
#
import argparse
import os
import traceback

if sys.version_info[0] == 2:
    from ConfigParser import SafeConfigParser as config_parser
else:
    from configparser import ConfigParser as config_parser

#
# installed dependencies
#
import parse

#
# other modules in this package
#


# -------------------------------------------------------------------------------
#
# User input
#
# -------------------------------------------------------------------------------
def commandline_options():
    """Process the command line arguments.

    """
    parser = argparse.ArgumentParser(
        description='FIXME: python program template.')

    parser.add_argument('--backtrace', action='store_true',
                        help='show exception backtraces as extra debugging '
                        'output')

    parser.add_argument('--debug', action='store_true',
                        help='extra debugging output')

    parser.add_argument('--config', nargs=1, required=True,
                        help='path to config file')

    parser.add_argument('--timing-file', nargs=1, required=True,
                        help='path to timing file')

    options = parser.parse_args()
    return options


def read_config_file(filename):
    """Read the configuration file and process

    """
    print("Reading configuration file : {0}".format(filename))

    cfg_file = os.path.abspath(filename)
    if not os.path.isfile(cfg_file):
        raise RuntimeError("Could not find config file: {0}".format(cfg_file))

    config = config_parser()
    config.read(cfg_file)

    return config

# -------------------------------------------------------------------------------
#
# FIXME: work functions
#
# -------------------------------------------------------------------------------
def read_file_to_buffer(filename):
    """
    """
    print("Reading to buffer: {0}".format(filename))
    with open(filename, 'r') as input_file:
        file_buffer = input_file.readlines()
    return file_buffer

# -------------------------------------------------------------------------------
#
# main
#
# -------------------------------------------------------------------------------
def main(options):
    config = read_config_file(options.config[0])
    template = read_file_to_buffer(config.get('main', 'template'))
    timing_file = read_file_to_buffer(options.timing_file[0])

    if len(template) != len(timing_file):
        raise RuntimeError('Number of lines in files differ.')
    timing_data = {}
    for template_line, data_line in zip(template, timing_file):
        result = parse.parse(template_line, data_line)
        if result:
            if len(result.named):
                timing_data.update(result.named)
    print(timing_data)
    return 0


if __name__ == "__main__":
    options = commandline_options()
    try:
        status = main(options)
        sys.exit(status)
    except Exception as error:
        print(str(error))
        if options.backtrace:
            traceback.print_exc()
        sys.exit(1)
