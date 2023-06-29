gdigrab  录屏
-s 1920x1080 录制的屏幕宽度、高度
-offset_x 100  偏移
-offset_y 200  偏移
需要注意宽度、高度分别加上偏移以后不能超出屏幕
例如 -s 1920x1080 -offset_x 100 -offset_y 200

-i desktop 录制屏幕
-thread_queue_size 此选项设置从文件或设备读取时排队数据包的最大数量。低延迟/高速率的直播流，如果不及时读取数据包可能会被丢弃；设置此值可以强制 ffmpeg 使用单独的输入线程并在数据包到达时立即读取数据包。默认情况下，ffmpeg 仅在指定了多个输入时才执行此操作。
-r 帧率
libx264 使用 libx264 编码所有视频流并复制所有音频流。
-acodec 设置音频编解码器,copy :所选流的数据包应从输入文件传送并在输出文件中混合
-f 强制输入或输出文件格式。通常会自动检测输入文件的格式，并根据输出文件的文件扩展名猜测格式，因此在大多数情况下不需要此选项。

ffmpeg -thread_queue_size 1000 -r 30 -f gdigrab -s 1820x880 -offset_x 100 -offset_y 200 -i desktop -vcodec libx264 -acodec copy -preset:v ultrafast -tune:v zerolatency -max_delay 10 -g 50 -sc_threshold 0 -f flv rtmp://xxxxxx


录制桌面，支持微软自带播放器和浏览器播放
ffmpeg -f gdigrab -i desktop  -vcodec libx264  -pix_fmt yuv420p    output.mp4

指定编码格式和像素格式

 

 指定录制时长
ffmpeg -f gdigrab -i desktop  -vcodec libx264  -pix_fmt yuv420p  -t 300  test.mp4
-t 指定录制时间长度，单位秒

指定捕获区域
（不加-offset_x 和 -offset_y就是捕获全屏）

ffmpeg -f gdigrab -i desktop -offset_x 10 -offset_y 20  -vcodec libx264  -pix_fmt yuv420p  -t 60  output.mp4

