
python3爬虫编码问题 
https://blog.csdn.net/lyxuefeng/article/details/79776751

cmd运行文件,print调用cmd编码
idea运行文件,调用idea的编码,(全局编码,工程编码,文件编码)

python中 encode编码,decode解码 
在做编码转换时，通常需要以unicode作为中间编码，即先将其他编码的字符串解码（decode）成unicode，再从unicode编码（encode）成另一种编码。
str1.decode('gb2312')，表示将gb2312编码的字符串str1转换成unicode编码。
str2.encode('gb2312')，表示将unicode编码的字符串str2转换成gb2312编码。
代码中字符串的默认编码与代码文件本身的编码一致。



获取爬取目标,  豆瓣,今日头条,房产,微信公众号,知乎,美图

浏览器操作 与 虚拟浏览器 操作 driver = webdriver.PhantomJS(executable_path=r"D:\phantomjs-2.1.1\bin\phantomjs.exe", desired_capabilities=dcap)
 
 知乎登录要验证码,csdn不要
 =====================================================================
爬虫涉及的通用技术最核心的可能就是 HTTP 请求了，我们至少至少应该掌握 HTTP 的 POST 和 GET 请求方法；其次就是 HTTP 请求和返回的 Header 含义及如何使用浏览器等工具跟踪请求 Header，因为爬虫链接请求时出现问题最多的情况一般都是 Header 有问题，譬如通常至少要保证 User-Agent、Referer、Cookie 等的伪装正确性，返回 Header 里的重定向链接，Gzip 数据需要解压等；还有就是 POST 数据的 urlencode 包装发送等；所以在进行爬虫前一定要具备比较扎实的前端与后端基础知识，同时要具备比较充足的 HTTP 知识。

有了这些知识我们可能就会急于开始爬取，其实这是不对的，我们应该做的第一件事是对要爬取的站点进行分析，至于如何分析，下面给出了一些常规套路：

首先倒腾下看你要抓取的站点有没有响应式的移动页面，如果有那就保持一个原则，尽可能的抓取他们的移动页面（原因就是一般移动页面都是内容干货啊，相对 PC 页面没那么臃肿，方便分析）。

Cookie 的操蛋之处，分析时建议开启隐身模式等，不然就面对清空 Cookie 大法了，清空 Cookie 对于爬虫网站分析至关重要，一定要 get 到。

分析爬取网页是静态页面还是动态页面，以便采取不同的爬取策略，使用不同的爬取工具。

查看网页源码找出对你有价值的数据的网页排版规律，譬如特定 CSS 选择等，从而指定抓取后的数据解析规则。

清洗数据后选择如何处理抓取到的有价值数据，譬如是存储还是直接使用，是如何存储等。

 =====================================================================
 
譬如通常至少要保证 User-Agent、Referer、Cookie 等的伪装正确性，返回 Header 里的重定向链接，Gzip 数据需要解压等；还有就是 POST 数据的 urlencode 包装发送等；

反正用啥都得考虑动态js抓取，图片验证码识别等等那些反爬虫机制 服务器异常, 超时 

BeautifulSoup和Selenium爬取豆瓣Top250电影信息，两种方法从本质上都是一样的，都是通过分析网页的DOM树结构进行元素定位，再定向爬取具体的电影信息

绕过selenium检测
一切使用自动化框架的项目，或者说代码，或者说爬虫都会碰到某些网站刚刚打开页面就被判定为：非人类行为
第一张使用mitmproxy用中间人的方式截取服务器发送来的js，修改js里面函数的参值方式发送给服务器。相当于在browser和server之间做一层中介的拦截。不过此方法要对js非常熟悉的人才好实施。
第二种方法依旧通过selenium，不过是在服务器在第一次发送js并在本地验证的时候，做好‘第一次’的伪装，从而实现‘第一次登陆’有效。。方法简单，适合小白。

BeautifulSoup -- 通过请求URL,分析网页的DOM树结构进行元素定位,需要构造请求
Selenium --  使用伪浏览器,分析网页的DOM树结构进行元素定位,效率慢,但是不用考虑请求头,请求内容
scrapy  --  高级封装的爬虫框架




环境--...
内容抓取
    登录-请求头,动态爬取
    保存文档或者数据库(mysql mongodb)
    分析数据
优化
    去重,分布式
 


# 豆果爬虫架构设计
为了更好的扩展性和爬虫工作的易于监控，爬虫项目分成3个子项目，分别是url提取、内容爬取、内容更新（包括更新线上内容和定时审核）

	主要是采用 Python 编写的scrapy框架，scrapy是目前非常热门的一种爬虫框架，它把整个爬虫过程分为了多个独立的模块，并提供了多个基类可以供我们去自由扩展，让爬虫编写变得简单而有逻辑性。并且scrapy自带的多线程、异常处理、以及强大的自定义Settings也让整个数据抓取过程变得高效而稳定。
	scrapy-redis：一个三方的基于redis的分布式爬虫框架，配合scrapy使用，让爬虫具有了分布式爬取的功能。github地址： https://github.com/darkrho/scrapy-redis 
	mongodb 、mysql 或其他数据库：针对不同类型数据可以根据具体需求来选择不同的数据库存储。结构化数据可以使用mysql节省空间，非结构化、文本等数据可以采用mongodb等非关系型数据提高访问速度。具体选择可以自行百度谷歌，有很多关于sql和nosql的对比文章。

	其实对于已有的scrapy程序，对其扩展成分布式程序还是比较容易的。总的来说就是以下几步：

* 找一台高性能服务器，用于redis队列的维护以及数据的存储。
* 扩展scrapy程序，让其通过服务器的redis来获取start_urls，并改写pipeline里数据	存储部分，把存储地址改为服务器地址。
* 在服务器上写一些生成url的脚本，并定期执行。

# 1 url提取
## 1.1 分布式抓取的原理
	采用scrapy-redis实现分布式，其实从原理上来说很简单，这里为描述方便，我们把自己的核心服务器称为master，而把用于跑爬虫程序的机器称为slave。

	我们知道，采用scrapy框架抓取网页，我们需要首先给定它一些start_urls，爬虫首先访问start_urls里面的url，再根据我们的具体逻辑，对里面的元素、或者是其他的二级、三级页面进行抓取。而要实现分布式，我们只需要在这个starts_urls里面做文章就行了。

	我们在master上搭建一个redis数据库（注意这个数据库只用作url的存储，不关心爬取的具体数据，不要和后面的mongodb或者mysql混淆），并对每一个需要爬取的网站类型，都开辟一个单独的列表字段。通过设置slave上scrapy-redis获取url的地址为master地址。这样的结果就是，尽管有多个slave，然而大家获取url的地方只有一个，那就是服务器master上的redis数据库。

	并且，由于scrapy-redis自身的队列机制，slave获取的链接不会相互冲突。这样各个slave在完成抓取任务之后，再把获取的结果汇总到服务器上（这时的数据存储不再在是redis，而是mongodb或者 mysql等存放具体内容的数据库了）

	这种方法的还有好处就是程序移植性强，只要处理好路径问题，把slave上的程序移植到另一台机器上运行，基本上就是复制粘贴的事情。
	
## 1.2 url的提取
	首先明确一点，url是在master而不是slave上生成的。
	
	对于每一个门类的urls（每一个门类对应redis下的一个字段，表示一个url的列表），我们可以单独写一个生成url的脚本。这个脚本要做的事很简单，就是按照我们需要的格式，构造除url并添加到redis里面。

	对于slave，我们知道，scrapy可以通过Settings来让爬取结束之后不自动关闭，而是不断的去询问队列里有没有新的url，如果有新的url，那么继续获取url并进行爬取。利用这一特性，我们就可以采用控制url的生成的方法，来控制slave爬虫程序的爬取。
	
## 1.3 url的处理
	1、判断URL指向网站的域名，如果指向外部网站，直接丢弃
	2、URL去重，然后URL地址存入redis和数据库；

# 2 内容爬取
## 2.1 定时爬取
	有了上面的介绍，定时抓取的实现就变得简单了，我们只需要定时的去执行url生成的脚本即可。这里推荐linux下的crontab指令，能够非常方便的制定定时任务，具体的介绍大家可以自行查看文档。

## 2.2 
# 3 内容更新
## 3.1 表设计
    帖子爬取表：
    id          :自增主键
    md5_url     :md5加密URL
    url         :爬取目标URL
    title       :爬取文章标题
    content     :爬取文章内容（已处理）
    user_id     :随机发帖的用户ID
    spider_name :爬虫名
    site        :爬取域名
    gid         :灌入帖子的ID
    module      :
    status      :状态 （1：已爬取；0：未爬取）
    use_time    :爬取时间
    create_time :创建时间
    CREATE TABLE `NewTable` (
        `id`  bigint(20) NOT NULL AUTO_INCREMENT ,
        `md5_url`  varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL ,
        `url`  varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL ,
        `title`  varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL ,
        `content`  mediumtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL ,
        `user_id`  varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL ,
        `spider_name`  varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL ,
        `site`  varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL ,
        `gid`  varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL ,
        `module`  varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL ,
        `status`  tinyint(4) NOT NULL DEFAULT 0 ,
        `use_time`  datetime NOT NULL ,
        `create_time`  datetime NOT NULL ,
    PRIMARY KEY (`id`)
    )
    ENGINE=InnoDB
    DEFAULT CHARACTER SET=utf8 COLLATE=utf8_general_ci
    AUTO_INCREMENT=4120
    ROW_FORMAT=COMPACT;



# 4 系统优化
## 4.1 防抓取方法
* 设置download_delay，这个方法基本上属于万能的，理论上只要你的delay足够长，网站服务器都没办法判断你是正常浏览还是爬虫。但它带来的副作用也是显然的：大量降低爬取效率。因此这个我们可能需要进行多次测试来得到一个合适的值。有时候download_delay可以设为一个范围随机值。
* 随机生成User-agent：更改User-agent能够防止一些403或者400的错误，基本上属于每个爬虫都会写的。这里我们可以重写scrapy 里的middleware，让程序每次请求都随机获取一个User-agent，增大隐蔽性。具体实现可以参考 http://www.sharejs.com/codes/python/8310
* 设置代理IP池：网上有很多免费或收费的代理池，可以借由他们作为中介来爬。一个问题是速度不能保证，第二个问题是，这些代理很多可能本来就没办法用。因此如果要用这个方法，比较靠谱的做法是先用程序筛选一些好用的代理，再在这些代理里面去随机、或者顺序访问。
* 设置好header里面的domian和host，有些网站，比如雪球网会根据这两项来判断请求来源，因此也是要注意的地方。

## 4.2 程序化管理、web管理
上述方法虽然能够实现一套完整的流程，但在具体操作过程中还是比较麻烦，可能的话还可以架构web服务器，通过web端来实现url的添加、爬虫状态的监控等，能够减轻非常大的工作量。这些内容如果要展开实在太多，这里就只提一下。

 

