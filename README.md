# 电视直播：Android TV 应用与 IPTV 订阅

本项目提供适用于 Android TV 电视和盒子的直播应用，以及按地区整理的 IPTV M3U 订阅地址。安装应用后，添加适合自己网络的订阅，即可查看频道列表并选择频道播放。

## 下载应用

[下载电视直播.apk](apk/电视直播.apk?raw=1)

将 APK 安装到 Android TV 电视或盒子，打开「电视直播」，再按下方步骤添加订阅。也可以把这些 M3U 地址用于其他支持 M3U 的播放器。

## 使用方法

1. 从下表选择所在地区的订阅；河南移动有两份列表可选，另有包含电影、电视剧和动漫频道的「通用」列表。
2. 在应用的订阅源设置中添加完整的 `.m3u` 地址。
3. 等待频道列表加载，然后选择频道播放。

订阅首页：[https://iptv.wwjjqq.top/](https://iptv.wwjjqq.top/)。打开首页后可按地区选择订阅、点击地址直接打开，或使用旁边的复制按钮复制完整链接，再粘贴到播放器的订阅设置中。每个订阅地址都以 `.m3u` 文件名结尾；浏览器打开后可能显示文本或播放列表，这是浏览器的处理方式，不影响播放器添加订阅。

所有订阅都在文件开头提供两份节目单：[节目单一](https://epg.zsdc.eu.org/t.xml) 和 [节目单二](http://epg.51zmt.top:8000/e.xml.gz)。支持多个节目单的播放器可以同时使用；部分播放器只读取第一个地址，遇到节目缺失时可在播放器的节目单设置中单独添加第二个地址。

## 订阅地址

| 订阅 | 地址 |
| --- | --- |
| 安徽移动 | `https://iptv.wwjjqq.top/aptv-ahyd.m3u` |
| 北京移动 | `https://iptv.wwjjqq.top/aptv-bjyd.m3u` |
| 福建移动 | `https://iptv.wwjjqq.top/aptv-fjyd.m3u` |
| 广西移动 | `https://iptv.wwjjqq.top/aptv-gxyd.m3u` |
| 贵州移动 | `https://iptv.wwjjqq.top/aptv-gzyd.m3u` |
| 河北移动 | `https://iptv.wwjjqq.top/aptv-hbyd.m3u` |
| 黑龙江移动 | `https://iptv.wwjjqq.top/aptv-hljyd.m3u` |
| 河南移动（备用） | `https://iptv.wwjjqq.top/aptv-hnyd.m3u` |
| 湖南移动（含电影、电视剧、动漫） | `https://iptv.wwjjqq.top/aptv-hunyd.m3u` |
| 江苏移动 | `https://iptv.wwjjqq.top/aptv-jsyd.m3u` |
| 江西移动 | `https://iptv.wwjjqq.top/aptv-jxyd.m3u` |
| 辽宁移动 | `https://iptv.wwjjqq.top/aptv-lnyd.m3u` |
| 山东移动 | `https://iptv.wwjjqq.top/aptv-sdyd.m3u` |
| 上海移动 | `https://iptv.wwjjqq.top/aptv-shyd.m3u` |
| 山西移动 | `https://iptv.wwjjqq.top/aptv-sxyd.m3u` |
| 浙江移动 | `https://iptv.wwjjqq.top/aptv-zjyd.m3u` |
| 通用（含电影、电视剧、动漫） | `https://iptv.wwjjqq.top/aptv-iptv.m3u` |
| 河南移动（主，含电影、电视剧、动漫） | `https://iptv.wwjjqq.top/ha-cmcc-iptv.m3u` |

## 来源与更新

本项目整理并提供 Android TV 可用的 M3U 直播订阅，方便在电视、电视盒子及兼容播放器中按地区选择频道。河南用户可优先使用「河南移动（主）」；另有 Kimentanm/aptv 的河南移动列表作为备用。河南主列表、湖南移动列表和通用列表都包含「电影」「电视剧」「动漫」分组，通用列表另收录虎牙影视和斗鱼影视。地区频道主要来自 [Kimentanm/aptv](https://github.com/Kimentanm/aptv)，河南主列表来自 [Elykia093/HA-CMCC-IPTV](https://github.com/Elykia093/HA-CMCC-IPTV)；影视内容补充自 [445569 的直播列表](https://iptv.445569.xyz/live.m3u) 和 [suxuang/myIPTV](https://github.com/suxuang/myIPTV)。订阅源定期检查；只有源文件内容有变化时才更新列表和网站。部分频道能否播放取决于来源线路及设备所在网络。

也可以打开 [GitHub Pages 订阅首页](https://cumtwjq.github.io/iptv-subscriptions/)，从表格中选择需要的订阅地址。APTV 通用列表中的部分线路带有 APTV 专用请求标记，其他播放器是否兼容需要实际测试。

Raw 仍使用 `raw.githubusercontent.com`。如果电视所在网络访问不了该域名，可以使用上表中的外网地址或 GitHub Pages 地址。这里提供的是 M3U 列表，不转发视频流；频道能否播放仍取决于播放设备所在网络能否访问列表内的地址。
