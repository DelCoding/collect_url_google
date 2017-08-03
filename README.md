# collect_url_google
在google搜索结果中提取目标URL和Title

	使用前提
		1、安装Selenium，如没有安装可使用pip install selenium进行安装。
		2、下载chromrdriver，把chromedriver下载好后，将其放在python安装文件夹目录下的Scripts目录下。
            如我本机装的是Anaconda3，那我就放在：D:\Program Files\Anaconda3\Scripts

    main.py为主要文件，运行main.py，并输入搜索关键字及你需要爬取的页数即可。

    preg.py为本地测试文件，用于提取保存在本地的html源码。