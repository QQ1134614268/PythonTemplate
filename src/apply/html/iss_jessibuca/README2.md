https://developer.aliyun.com/article/1209686
1. 硬解：字面上理解就是用硬件来进行解码，是使用 GPU 的专门模块来解码。
2. 软解：字面上理解就是用软件来进行解码，是使用 CPU 来运行视频编解码代码。

软解：在软解码过程中需要对大量的视频信息进行运算，所以对 CPU 性能的要求非常高，尤其是对高码率的视频来说巨大的运算量会造成转换效率低，发热量高等问题。不过软解码的过程中不需要复杂的硬件支持，兼容性高。即使是新出的视频编码格式，也可以为其编写新的解码程序；硬解：硬解码调用 GPU 的专门模块来解码，拥有独特的计算方法，解码效率高。这样不但能够减轻 CPU 的负担，还有着低功耗，发热少等特点。但是由于硬解码起步相对晚，软件和驱动对他的支持度低，基本上硬解码内置什么样的模块就解码什么样的视频，面对各色各样的视频编码样式，兼容性没那么好。

API:
    HTMLVideoElement
    Media Source Extensions (MSE)
    WebCodecs

    W3C 规范了多种 API 用于处理视频，例如 HTMLVideoElement、Media Source Extensions(以下简称 MSE)、WebCodecs 等。不同的 API 是在不同浏览器的版本下提供的支持，且对编码格式的支持度有所不同。例如 WebCodecs 编码相关的 API 对 H.265 的支持度就比解码 API 差一些。

# video 标签; 
Source标签

MSE: 用 Javascript 自己实现一个跟 source 一样效果的前端播放器了;
类似于 flv.js ，我们可以对 MP4 进行解封装和复用最后通过 Media Source Extensions 进行播放：

WebCodecs: WebCodecs API 提供了 VideoDecoder 来直接调用硬解能力。

WASM: 我们也可以基于 WebAssembly + FFmpeg 编译实现一个软解的 Decoder（姑且称为 WASMDecoder），然后与上面的 WebCodecs 的思路一样，将 VideoDecoder 替换为 WASMDecoder 即可。
    WASM 软解方案的性能瓶颈主要在解码和渲染的环节。解码算法复杂度高，因此非常占 CPU 资源；渲染需要用 WebGL shader 进行 YUV 到 RGB 的转换计算且需要把每帧图像作为纹理从 CPU 上传到 GPU，因此也较为耗时。

2k 以上的帧率不能满足线上大多数视频流畅的观看体验。解码性能优化的常见手段有：
解码:
    算法优化
    多核并行
    SIMD: 即单指令多数据并行计算
渲染:
    OffscreenCanvas :提供了在 web worker 绘制 canvas 的能力




# jessibuca
### 关于硬解码和软解码
####硬解码
useMSE和useWCS都是硬解码
useMSE 支持 H264，
useMSE jessibuca Pro 支持 H265（需要手动开启参数），
useWCS 只支持H264(浏览器不支持H265)
useMSE 支持http 和https
useWCS 只支持https
#软解码
支持 H264(低分辨率) 和 H265(低分辨率)
jessibuca Pro 支持 H264 和 H265 高分辨率高帧率解码
软解码支持http 和https
如果遇到硬解码失败的时候，会自动切换到wasm软解码


关于解码（useMSE、useWCS、wasm）优先级
#useMSE
使用的是浏览器提供的MediaSource接口，来进行解码。

硬解码
兼容性好
ios safari不支持
支持H264和H265解码
支持http和https
#useWCS
使用的是WebCodec接口，来进行解码。

硬解码
支持H264和H265解码
支持https
ios safari不支持
兼容性不如mse
#wasm(simd)
使用的是webassembly来进行解码。

软解码
兼容性好
支持H264和H265解码
支持http和https
#优先级
如果同时配置了useMSE和useWCS，则优先使用useMSE，如果useMSE不支持，则使用useWCS，如果 useWCS 不支持，则降级到wasm解码。

useMSE > useWCS > wasm

直播流播放完了，能监听到吗？
回答：不能

因为播放器也不知道流什么时候结束，播放器是被动的接受流数据的，所以播放器也不知道流什么时候结束。

解决方案：

可以通过业务层去监听流是否结束。
可以通过监听超时事件（不建议）。
#关于当前直播流正在播的时间点
目前播放器能够监听到的时间是从流里面的时间戳，stats中的ts。

这个是流里面的时间戳，可能是相对时间戳，也可能是绝对时间戳。

如果业务上面需要获取当前直播流正在播的时间点 这需求，目前只能结合业务然后结合ts作为相对时间来计算。

从服务器获取当前播放的时间点，
监听播放器的stats事件，获取到ts，缓存一个开始时间点，通过最新的ts减去开始时间点，就是当前播放的时间点。
