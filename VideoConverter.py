import ffmpy
ff = ffmpy.FFmpeg(
executable='ffmpeg-master-latest-win64-gpl/bin/ffmpeg',
inputs={'input.mp4': None},
outputs={'output.avi': None}
)
ff.run()