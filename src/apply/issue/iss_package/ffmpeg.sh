# 语法结构: ffmpeg 输入配置 -i 输入地址 输出配置 输出地址

# ffmpeg 拉流
ffmpeg -i input.mp4 output.mp4
ffmpeg -i rtmp://127.0.0.1/live/123456 -c copy out.flv
# ffmpeg 推流
ffmpeg -re -i /home/input.mp4 -c copy -f flv rtmp://127.0.0.1/live/123456 # 推流到流媒体踢
ffmpeg -f gdigrab -i desktop -vcodec libx264 -pix_fmt yuv420p -t 300 -y -f flv out.mp4 # 录屏推流

#
-i:
  input.mp4 # 本地文件
  rtsp://xxx # rtsp 地址
  http://xxx # http 地址
  desktop # 桌面, 可以与
  "0"  # 推流摄像头
  "1"  # 推流麦克风
  "0:1"  # 摄像头 + 麦克风
  0:1 # 摄像头 + 麦克风
  video="摄像头名称" # 根据摄像头名称播放, 摄像头名称是查询得到的
-f: # 当输入配置 指定采集
  avfoundation
  gdigrab # 使用gdi录屏
  dshow
-f libx264 # 当为输出配置, 指定编码

-vcodec:
  copy # 与原来一样
  libx264 # h264编码
-acodec
  libfaac
  libmp3lame

-an # 去掉音频
-vn # 去掉视频

-pixel_format uyvy422 # 更改像素格式

-s 1280x800 # 分辨率 frame size
-ss 10 # 10秒后开始

-r: # 帧速率
  25 # 帧率25, FPS;
  30000/1001
-re # 与原来一样, 否则最大速度推送
-framerate 25  # 推流帧率
-preset ultrafast
-preset:v ultrafast

-ar 44100
-ac 1

-vsync 2
-vf:
  format=yuv444p,crop=426:240:507:339
  scale=320:240 # 更改拉流视频的分辨率 以320:240分辨率为例
  crop=1280:720:0:120 # 视频尺寸裁剪 crop后的参数，宽：高：起始x：起始y
  vflip # 上下翻转
  hflip # 左右翻转
-vframes 30 # 指定抽取的帧数 30帧
-capture_cursor 1
-b:v 1M
-b:a 128K
-b # 指定比特率, 默认 VBR
-vb # 视频比特率
-c:v ibvpx-vp9 #
-c:a libopus
-c copy # 复制流 ; 输出流和输入流相同的编解码器
-tune:v zerolatency


其他:
ffmpeg -i input.mp4 -r 10 output.mp4 # 输出配置 -r 改变视频帧率，例如将输入视频转换为10帧率的输出视频
ffmpeg -ss 00:00:30 -t 60 -i input.mp4 -codec copy out.mp4 # 视频剪辑 例如，从第30秒开始，截一分钟：
ffmpeg -i input.mp4 -fflags nobuffer -t 60 -ss 0 out.mp4 # 视频截取 代表截取输入视频从0秒到60秒的片段，保存到输出地址。
ffmpeg -i input.mp4 -vf vflip out.mp4 # 视频旋转 vflip: 上下翻转; hflip: 左右翻转; transpose=1 : 顺时针90°; transpose=2 : 逆时针90°;
ffmpeg -i input.mp4 -vf crop=1280:720:0:120 out.mp4 # 视频尺寸裁剪 crop后的参数，宽：高：起始x：起始y
ffmpeg -list_devices true -f dshow -i dummy 寻找可用摄像头
ffmpeg -f dshow -i video="摄像头名称" -framerate 25 -bufsize 1000000k -vcodec libx264 -preset:v ultrafast -tune:v zerolatency -acodec libfaac -f flv out.mp4
ffmpeg -i input.mp4 -ss 00:00:00 -t 10 out.mp4 # 裁剪:
ffmpeg -f concat -safe 0 -i inputs.txt -c copy out.mp4 # 合并 inputs.txt内容是 一行行的文件路径: file /home/input.mp4

# 转图片
ffmpeg -i input.mp4 test.gif # 转gif
ffmpeg -i input.mp4 -fflags nobuffer -update 1 -y -t 200 -ss 1 -r 1 -f image2 out%d.jpg # 定时截图（不断截图后更新一张图片）
ffmpeg -i input.mp4 -r 1 -t 10 -ss 0 -f image2 out%d.jpg
ffmpeg -i input.mp4 -r 1 -f image2 # 视频转图片:

# 图片转视频:
ffmpeg -i image-%3d.jpeg out.mp4


# 快退 快进 裸的H264码流，如果实现快进快退必须基于 I 帧才能实现：在播放前对整个码流进行统计，总共有多少帧，所有的 I 帧在什么位置。在播放的时候，再根据用户快进或快退的位置判断相邻最近的 I 帧在什么位置，然后从那一个 I 帧开始解码播放。
# filter map
ffmpeg -i input.mp4 -filter:v "setpts=0.5*PTS" output.mp4 # 视频变速 视频转为两倍速：
ffmpeg -i input.mp4 -r 16 -filter:v "setpts=0.25*PTS" output.mp4
ffmpeg -i input.mp4 -filter:v "setpts=2.0*PTS" output.mp4
ffmpeg -i input.mp4 -filter:a "atempo=2.0" -vn output.mp4
ffmpeg -i input.mp4 -filter:a "atempo=2.0,atempo=2.0" -vn output.mp4
ffmpeg -i input.mp4 -filter_complex "[0:v]setpts=0.5*PTS[v];[0:a]atempo=2.0[a]" -map "[v]" -map "[a]" output.mp4


# 播放
ffplay -i input.mp4
ffplay rtmp://localhost:1935/live/room1
ffplay -i input.mp4 -vf scale=320:240 # 更改拉流视频的分辨率 以320:240分辨率为例
ffplay -f dshow -i video="摄像头名称" # 此处的摄像头名称是由上条命令执行后查询得到的
ffplay -i input.mp4 -fflags nobuffer  # 拉流播放视频 nobuffer为实时播放

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