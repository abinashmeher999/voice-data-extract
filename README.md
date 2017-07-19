voice-data-extract
==================


A command line interface to combine text information from subtitles with voice data in the video.
Provides a convenient way to generate training data for speech-recognition purposes.


Description
===========

The project provides a quick way to generate audio training data for speech-recognition machine learning models.
It utilises the knowledge bank of annotated voice data we already have, **Subtitles!!**

It reads the subtitles line by line and clips the audio from the video for the corresponding time interval.

example usage:

```bash
$ srt_voice -fv video.mkv -fs subtitles.srt -o output_dir
```

This creates the directory output_dir and nicely arranges the audio clips you chose during the processing in
the output directory.

------

This has been possible because of the hard work of the maintainers of packages like
- moviepy
- pysrt
- mutagen
- shortuuid

Setup
=====
You will need these
- [Audacious Music Player](http://audacious-media-player.org/download)


*This project has been set up using PyScaffold 2.5.7. For details and usage
information on PyScaffold see http://pyscaffold.readthedocs.org/.*
