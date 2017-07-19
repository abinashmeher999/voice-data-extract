#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Setup file for srtvoiceext.

    This file was generated with PyScaffold 2.5.7, a tool that easily
    puts up a scaffold for your new Python project. Learn more under:
    http://pyscaffold.readthedocs.org/
"""

import sys
from setuptools import setup


def setup_package():
    # needs_sphinx = {'build_sphinx', 'upload_docs'}.intersection(sys.argv)
    # sphinx = ['sphinx'] if needs_sphinx else []
    setup(
        name='srtvoiceext',
        packages=['srtvoiceext'],
        version='0.1.2',
        description='A command line interface to combine text information from subtitles with voice data in the video.',
        author='Abinash Meher',
        author_email='abinashdakshana999+pypi@gmail.com',
        url='http://github.com/abinashmeher999/voice-data-extract',
        keywords=['training-data', 'speech-recognition', 'speech-to-text'],
        install_requires=['moviepy==0.2.3.2',
                          'pysrt>=1.1.1,<2',
                          'eyeD3-pip>=0.6.19,<1',
                          'imageio==2.1.2',
                          'mutagen==1.38',
                          'shortuuid>=0.5.0,<1',
                          'six>=1.10.0,<2'],
        entry_points={
            'console_scripts': ['srt_voice=srtvoiceext.skeleton:run']
        }
        # setup_requires=['six', 'pyscaffold>=2.5a0,<2.6a0'] + sphinx,
        # use_pyscaffold=True
    )


if __name__ == "__main__":
    setup_package()
