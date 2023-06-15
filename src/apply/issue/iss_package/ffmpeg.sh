# ffmpeg 推流

# ffmpeg 拉流

ffmpeg -re -i /Users/binny/ffmpeg/killer.mp4 -vcodec copy -f flv rtmp://localhost:1935/live/room1
ffplay rtmp://localhost:1935/live/room1


# 语法结构: ffmpeg 输入配置 -i 输入地址 输出配置 输出地址
ffmpeg -re -i fight.mp4 -f flv rtmp://192...........
ffmpeg -list_devices true -f dshow -i dummy 寻找可用摄像头
ffplay -f dshow -i video="摄像头名称" # 此处的摄像头名称是由上条命令执行后查询得到的
ffmpeg -f dshow -i video="摄像头名称" -vcodec libx264 -preset:v ultrafast -tune:v zerolatency -f flv 推流地址
ffmpeg -f dshow -i video="摄像头名称" -framerate 25 -bufsize 1000000k -vcodec libx264 -preset:v ultrafast -tune:v zerolatency -acodec libfaac -f flv 推流地址
#-framerate 25  推流帧率
#-preset:v ultrafast -tune:v zerolatency -acodec libfaac ：最快推流配置

ffplay -i "拉流地址" -fflags nobuffer  # 拉流播放视频 nobuffer为实时播放
ffmpeg -i "拉流地址" "输出地址" # 如ffmpeg -i https://xxx out.mp4
ffplay -i "拉流地址" -vf scale=320:240 ##更改拉流视频的分辨率 以320:240分辨率为例

ffmpeg -i "输入视频" -fflags nobuffer -t 60 -ss 0 "输出地址"# 视频截取 代表截取输入视频从0秒到60秒的片段，保存到输出地址。
ffmpeg -i "视频地址" -fflags nobuffer -update 1 -y -t 200 -ss 1 -r 1 -f image2 图片输出地址 #定时截图（不断截图后更新一张图片）
#  -ss n ： n秒后开始截图
#  -r n ： 每秒截n帧
#  -t n ： 截n秒
#其他：-q:v ：图片质量 -vframes：指定抽取的帧数
ffmpeg -i fight.mp4 -r 1 -t 200 -ss 1 -f image2 out%d.jpg
ffmpeg -i test.mp4 test.gif # 格式转换
ffmpeg -i input.mp4 -an -filter:v "setpts=0.5*PTS" output.mp4 # 视频变速 视频转为两倍速：
ffmpeg -i input.mp4 -r 10 output.mp4 #改变视频帧率 通过输出配置-r设置，例如将输入视频转换为10帧率的输出视频
ffmpeg -ss 00:00:30 -t 60 -i src.mp4 -codec copy out.mp4 # 视频剪辑 例如，从第30秒开始，截一分钟：

ffmpeg -i input.mp4 -vf vflip out.mp4 # 视频旋转 上下翻转
ffmpeg -i input.mp4 -vf hflip out.mp4 # 左右翻转
ffmpeg -i input.mp4 -vf transpose=1 out.mp4 # 顺时针90°
ffmpeg -i input.mp4 -vf transpose=2 out.mp4 # 逆时针90°
ffmpeg -i input.mp4 -vf crop=1280:720:0:120 out.mp4 # 视频尺寸裁剪 crop后的参数，宽：高：起始x：起始y

# 快退 快进
# 裸的H264码流，如果实现快进快退必须基于 I 帧才能实现：在播放前对整个码流进行统计，总共有多少帧，所有的 I 帧在什么位置。在播放的时候，再根据用户快进或快退的位置判断相邻最近的 I 帧在什么位置，然后从那一个 I 帧开始解码播放。
ffmpeg -i input.mkv -filter:v "setpts=0.5*PTS" output.mkv
ffmpeg -i input.mkv -r 16 -filter:v "setpts=0.25*PTS" output.mkv
ffmpeg -i input.mkv -filter:v "setpts=2.0*PTS" output.mkv
ffmpeg -i input.mkv -filter:a "atempo=2.0" -vn output.mkv
ffmpeg -i input.mkv -filter:a "atempo=2.0,atempo=2.0" -vn output.mkv
ffmpeg -i input.mkv -filter_complex "[0:v]setpts=0.5*PTS[v];[0:a]atempo=2.0[a]" -map "[v]" -map "[a]" output.mkv


//推流桌面 - 只有桌面内容
ffmpeg -f avfoundation -pixel_format uyvy422 -i "1" -f flv rtmp://localhost:1935/live/room1

ffmpeg -f avfoundation -i "1" -vcodec libx264 -preset ultrafast -acodec libfaac -f flv rtmp://localhost:1935/live/room1
//推流摄像头
ffmpeg -f avfoundation -framerate 30 -video_size 1280x720 -i  "0"  -vcodec libx264 -acodec libfaac -f flv rtmp://localhost:1935/live/room1
//只推流麦克风
ffmpeg -f avfoundation -i ":0" -vcodec libx264 -preset ultrafast -acodec libmp3lame -ar 44100 -ac 1 -f flv rtmp://localhost:1935/live/room1
//摄像头+麦克分
ffmpeg -f avfoundation -framerate 30 -video_size 1280x720 -i "0:0" -vcodec libx264 -preset ultrafast -acodec libmp3lame -ar 44100 -ac 1 -f flv rtmp://localhost:1935/live/room1

ffmpeg -f avfoundation -framerate 30 -video_size 1280x720 -i "0:0" -vsync 2 -vcodec libx264 -preset ultrafast -acodec libmp3lame -ar 44100 -ac 1 -b:v 1M -b:a 128K -f flv rtmp://localhost:1935/live/room1

ffmpeg -f avfoundation -framerate 30 -video_size 640x480 -i  "0" -vcodec libx264 -preset ultrafast -acodec libfaac -f flv rtmp://localhost:1935/live/room1

ffmpeg -f avfoundation -framerate 30 -video_size 640x480 -i  "0" -vcodec libx264 -acodec libfaac -f flv  rtmp://localhost:1935/live/room1

ffmpeg -f avfoundation -framerate 30 -video_size 640x480 -i  "0"  \-c:v libx264 -preset ultrafast -acodec libfaac -f flv  rtmp://localhost:1935/live/room1

ffmpeg -f avfoundation -framerate 30 -video_size 640x480 -i  "0"  -vcodec libx264 -preset ultrafast -acodec libfaac -f flv  rtmp://localhost:1935/live/room1

ffmpeg -f avfoundation -framerate 30 -video_size 640x480 -i  "0"  -pixel_format nv12 -preset ultrafast -acodec libfaac -f flv rtmp://localhost:1935/live/room1

ffmpeg -f avfoundation -framerate 30 -video_size 1280x720 -i  "0"  -vf format=yuv444p,crop=426:240:507:339 -preset ultrafast -acodec libfaac -f flv  rtmp://localhost:1935/live/room1

ffmpeg -f avfoundation -capture_cursor 1 -i 1:0 -r 30000/1001 -s 1280x800 -vsync 2 -c:v libvpx-vp9 -c:a libopus -b:v 1M -b:a 128K capture.webm -f flv rtmp://localhost:1935/live/room1

ffmpeg -f avfoundation -pixel_format uyvy422 -i "1" -f flv rtmp://localhost:1935/live/room1


####

ffmpeg version N-104402-g2aa343bb6f-20211021 Copyright (c) 2000-2021 the FFmpeg developers
  built with gcc 10-win32 (GCC) 20210408
  configuration: --prefix=/ffbuild/prefix --pkg-config-flags=--static --pkg-config=pkg-config --cross-prefix=x86_64-w64-mingw32- --arch=x86_64 --target-os=mingw32 --enable-gpl --enable-version3 --disable-debug --disable-w32threads --enable-pthreads --enable-iconv --enable-libxml2 --enable-zlib --enable-libfreetype --enable-libfribidi --enable-gmp --enable-lzma --enable-fontconfig --enable-libvorbis --enable-opencl --enable-libvmaf --enable-vulkan --disable-libxcb --disable-xlib --enable-amf --enable-libaom --enable-avisynth --enable-libdav1d --enable-libdavs2 --disable-libfdk-aac --enable-ffnvcodec --enable-cuda-llvm --enable-frei0r --enable-libglslang --enable-libgme --enable-libass --enable-libbluray --enable-libmp3lame --enable-libopus --enable-libtheora --enable-libvpx --enable-libwebp --enable-lv2 --enable-libmfx --enable-libopencore-amrnb --enable-libopencore-amrwb --enable-libopenjpeg --enable-librav1e --enable-librubberband --enable-schannel --enable-sdl2 --enable-libsoxr --enable-libsrt --enable-libsvtav1 --enable-libtwolame --enable-libuavs3d --disable-libdrm --disable-vaapi --enable-libvidstab --enable-libx264 --enable-libx265 --enable-libxavs2 --enable-libxvid --enable-libzimg --enable-libzvbi --extra-cflags=-DLIBTWOLAME_STATIC --extra-cxxflags= --extra-ldflags=-pthread --extra-ldexeflags= --extra-libs=-lgomp --extra-version=20211021
  libavutil      57.  7.100 / 57.  7.100
  libavcodec     59. 12.100 / 59. 12.100
  libavformat    59.  6.100 / 59.  6.100
  libavdevice    59.  0.101 / 59.  0.101
  libavfilter     8. 15.100 /  8. 15.100
  libswscale      6.  1.100 /  6.  1.100
  libswresample   4.  0.100 /  4.  0.100
  libpostproc    56.  0.100 / 56.  0.100
Hyper fast Audio and Video encoder
usage: ffmpeg [options] [[infile options] -i infile]... {[outfile options] outfile}...

Getting help:
    -h      -- print basic options
    -h long -- print more options
    -h full -- print all options (including all format and codec specific options, very long)
    -h type=name -- print all options for the named decoder/encoder/demuxer/muxer/filter/bsf/protocol
    See man ffmpeg for detailed description of the options.

Print help / information / capabilities:
-L                  show license
-h topic            show help
-? topic            show help
-help topic         show help
--help topic        show help
-version            show version
-buildconf          show build configuration
-formats            show available formats
-muxers             show available muxers
-demuxers           show available demuxers
-devices            show available devices
-codecs             show available codecs
-decoders           show available decoders
-encoders           show available encoders
-bsfs               show available bit stream filters
-protocols          show available protocols
-filters            show available filters
-pix_fmts           show available pixel formats
-layouts            show standard channel layouts
-sample_fmts        show available audio sample formats
-colors             show available color names
-sources device     list sources of the input device
-sinks device       list sinks of the output device
-hwaccels           show available HW acceleration methods

Global options (affect whole program instead of just one file):
-loglevel loglevel  set logging level
-v loglevel         set logging level
-report             generate a report
-max_alloc bytes    set maximum size of a single allocated block
-y                  overwrite output files
-n                  never overwrite output files
-ignore_unknown     Ignore unknown stream types
-filter_threads     number of non-complex filter threads
-filter_complex_threads  number of threads for -filter_complex
-stats              print progress report during encoding
-max_error_rate maximum error rate  ratio of decoding errors (0.0: no errors, 1.0: 100% errors) above which ffmpeg returns an error instead of success.
-bits_per_raw_sample number  set the number of bits per raw sample
-vol volume         change audio volume (256=normal)

Per-file main options:
-f fmt              force format
-c codec            codec name
-codec codec        codec name
-pre preset         preset name
-map_metadata outfile[,metadata]:infile[,metadata]  set metadata information of outfile from infile
-t duration         record or transcode "duration" seconds of audio/video
-to time_stop       record or transcode stop time
-fs limit_size      set the limit file size in bytes
-ss time_off        set the start time offset
-sseof time_off     set the start time offset relative to EOF
-seek_timestamp     enable/disable seeking by timestamp with -ss
-timestamp time     set the recording timestamp ('now' to set the current time)
-metadata string=string  add metadata
-program title=string:st=number...  add program with specified streams
-target type        specify target file type ("vcd", "svcd", "dvd", "dv" or "dv50" with optional prefixes "pal-", "ntsc-" or "film-")
-apad               audio pad
-frames number      set the number of frames to output
-filter filter_graph  set stream filtergraph
-filter_script filename  read stream filtergraph description from a file
-reinit_filter      reinit filtergraph on input parameter changes
-discard            discard
-disposition        disposition

Video options:
-vframes number     set the number of video frames to output
-r rate             set frame rate (Hz value, fraction or abbreviation)
-fpsmax rate        set max frame rate (Hz value, fraction or abbreviation)
-s size             set frame size (WxH or abbreviation)
-aspect aspect      set aspect ratio (4:3, 16:9 or 1.3333, 1.7777)
-bits_per_raw_sample number  set the number of bits per raw sample
-vn                 disable video
-vcodec codec       force video codec ('copy' to copy stream)
-timecode hh:mm:ss[:;.]ff  set initial TimeCode value.
-pass n             select the pass number (1 to 3)
-vf filter_graph    set video filters
-ab bitrate         audio bitrate (please use -b:a)
-b bitrate          video bitrate (please use -b:v)
-dn                 disable data

Audio options:
-aframes number     set the number of audio frames to output
-aq quality         set audio quality (codec-specific)
-ar rate            set audio sampling rate (in Hz)
-ac channels        set number of audio channels
-an                 disable audio
-acodec codec       force audio codec ('copy' to copy stream)
-vol volume         change audio volume (256=normal)
-af filter_graph    set audio filters

Subtitle options:
-s size             set frame size (WxH or abbreviation)
-sn                 disable subtitle
-scodec codec       force subtitle codec ('copy' to copy stream)
-stag fourcc/tag    force subtitle tag/fourcc
-fix_sub_duration   fix subtitles duration
-canvas_size size   set canvas size (WxH or abbreviation)
-spre preset        set the subtitle options to the indicated preset