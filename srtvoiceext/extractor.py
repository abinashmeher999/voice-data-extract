import os
import errno
import string

import itertools

import imageio
import moviepy.editor as mp
import pysrt
import shortuuid as suuid
from mutagen.easyid3 import EasyID3
import subprocess
from .utils import getch


def playsound(audio_filepath):
    subprocess.call(["audacious", "-3", "-H", "-q", audio_filepath])


# By github.com/seanh formatFilename.py
# https://gist.github.com/seanh/93666
def format_filename(s):
    """Take a string and return a valid filename constructed from the string.
    Uses a whitelist approach: any characters not present in valid_chars are
    removed. Also spaces are replaced with underscores.

    Note: this method may produce invalid filenames such as ``, `.` or `..`
    When I use this method I prepend a date string like '2009_01_15_19_46_32_'
    and append a file extension like '.txt', so I avoid the potential of using
    an invalid filename.

    """
    valid_chars = "-_() %s%s" % (string.ascii_letters, string.digits)
    filename = ''.join(c for c in s if c in valid_chars)
    filename = filename.replace(' ', '_')  # I don't like spaces in filenames.
    return filename


def mkdir_p(path):
    """
    Creates the directory structure if not already present
    :param path: The path to the directory, which you want to check for existence
        and create if necessary
    """
    try:
        os.makedirs(path)
    except OSError as exc:  # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise


class Extractor(object):
    def __init__(self, video_name=None, subtitle_name=None, relative_outdir='voice_data'):
        if video_name is None:
            raise ValueError('video file not specified')
        if subtitle_name is None:
            raise ValueError('subtitle file is not specified')

        imageio.plugins.ffmpeg.download()

        video_path = os.path.join(os.getcwd(), video_name)
        subtitle_path = os.path.join(os.getcwd(), subtitle_name)
        output_path = os.path.join(os.getcwd(), relative_outdir)
        mkdir_p(output_path)

        subs = pysrt.open(subtitle_path, encoding='utf-8')

        clip = mp.VideoFileClip(video_path)
        for line, num in zip(subs, itertools.count()):
            if '\n' in line.text:
                continue

            time_convert = lambda t: (t.hours, t.minutes, t.seconds + t.milliseconds / 1000)
            start = time_convert(line.start)
            end = time_convert(line.end)
            subclip = clip.subclip(t_start=start, t_end=end)

            audio_filename = "{}-{}-{}.mp3".format(num, format_filename(line.text[:100]),
                                                   suuid.ShortUUID().random(length=6))
            audio_filepath = os.path.join(output_path, audio_filename)
            subclip.audio.write_audiofile(audio_filepath, verbose=False)

            audio = EasyID3(audio_filepath)
            audio['title'] = line.text
            audio.save()

            while True:
                print(line.text, end='')
                playsound(audio_filepath)
                print("{}\t{}\t{}\t{}".format("y: Keep", "n: Delete", "r: Repeat", "q: Quit"))
                cmd = getch()
                if cmd in "yY":
                    break
                elif cmd in "nN":
                    os.remove(audio_filepath)
                    break
                elif cmd in "rR":
                    continue
                elif cmd in "qQ":
                    os.remove(audio_filepath)
                    return
                else:
                    print("Invalid input received please try again.")
