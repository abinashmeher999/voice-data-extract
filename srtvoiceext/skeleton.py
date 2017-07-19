#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This is a skeleton file that can serve as a starting point for a Python
console script. To run this script uncomment the following line in the
entry_points section in setup.cfg:

    console_scripts =
     srt_voice = srtvoiceext.skeleton:run

Then run `python setup.py install` which will install the command `vdataext`
inside your current environment.
Besides console scripts, the header (i.e. until _logger...) of this file can
also be used as template for Python modules.

Note: This skeleton file can be safely removed if not needed!
"""

import argparse
import sys
import logging

from srtvoiceext import __version__
from srtvoiceext import extract

__author__ = "Abinash Meher"
__copyright__ = "Abinash Meher"
__license__ = "mit"

_logger = logging.getLogger(__name__)


def parse_args(args):
    """Parse command line parameters

    Args:
      args ([str]): command line parameters as list of strings

    Returns:
      :obj:`argparse.Namespace`: command line parameters namespace
    """
    parser = argparse.ArgumentParser(
        description="Given a video file and it's subtitles it helps extract voice data from it")
    parser.add_argument(
        '--version',
        action='version',
        version='voice-data-extract {ver}'.format(ver=__version__))
    parser.add_argument(
        '-v',
        '--verbose',
        dest="loglevel",
        help="set loglevel to INFO",
        action='store_const',
        const=logging.INFO)
    parser.add_argument(
        '-vv',
        '--very-verbose',
        dest="loglevel",
        help="set loglevel to DEBUG",
        action='store_const',
        const=logging.DEBUG)
    parser.add_argument(
        '-fv',
        '--video',
        dest="video_filename",
        required=True,
        help="filename of the video"
    )
    parser.add_argument(
        '-fs',
        '--subtitles',
        dest="subtitles_filename",
        required=True,
        help="filename of the video"
    )
    parser.add_argument(
        '-o',
        "--outdir",
        dest="output_directory",
        help="the directory in which the audio clips are going to be stored (default : ./voice_clips)",
        default="voice_clips"
    )
    return parser.parse_args(args)


def setup_logging(loglevel):
    """Setup basic logging

    Args:
      loglevel (int): minimum loglevel for emitting messages
    """
    logformat = "[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
    logging.basicConfig(level=loglevel, stream=sys.stdout,
                        format=logformat, datefmt="%Y-%m-%d %H:%M:%S")


def main(args):
    """Main entry point allowing external calls

    Args:
      args ([str]): command line parameter list
    """
    args = parse_args(args)
    setup_logging(args.loglevel)
    # print("{} {} {}".format(args.video_filename, args.subtitles_filename, args.output_directory))
    extract(args.video_filename, args.subtitles_filename, args.output_directory)


def run():
    """Entry point for console_scripts
    """
    main(sys.argv[1:])


if __name__ == "__main__":
    run()
