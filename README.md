# 电视直播：Android TV 应用与 IPTV 订阅

本项目提供适用于 Android TV 电视和盒子的直播应用，以及按地区整理的 IPTV M3U 订阅地址。安装应用后，添加适合自己网络的订阅，即可查看频道列表并选择频道播放。

## 下载应用

[下载电视直播.apk](apk/电视直播.apk?raw=1)

将 APK 安装到 Android TV 电视或盒子，打开「电视直播」，再按下方步骤添加订阅。也可以把这些 M3U 地址用于其他支持 M3U 的播放器。

## 使用方法

1. 从下表选择所在地区的订阅；河南移动有两份列表可选，另有包含电影、电视剧和动漫频道的「通用」列表。
2. 在应用的订阅源设置中添加完整的 `.m3u` 地址。
3. 等待频道列表加载，然后选择频道播放。

订阅网址必须包含 `.m3u` 文件名；`https://iptv.wwjjqq.top/` 只是服务首页。浏览器打开订阅网址会显示 M3U 文本，观看节目请使用支持 M3U 的应用。

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
| 河南移动 | `https://iptv.wwjjqq.top/aptv-hnyd.m3u` |
| 湖南移动 | `https://iptv.wwjjqq.top/aptv-hunyd.m3u` |
| 江苏移动 | `https://iptv.wwjjqq.top/aptv-jsyd.m3u` |
| 江西移动 | `https://iptv.wwjjqq.top/aptv-jxyd.m3u` |
| 辽宁移动 | `https://iptv.wwjjqq.top/aptv-lnyd.m3u` |
| 山东移动 | `https://iptv.wwjjqq.top/aptv-sdyd.m3u` |
| 上海移动 | `https://iptv.wwjjqq.top/aptv-shyd.m3u` |
| 山西移动 | `https://iptv.wwjjqq.top/aptv-sxyd.m3u` |
| 浙江移动 | `https://iptv.wwjjqq.top/aptv-zjyd.m3u` |
| 通用（含电影、电视剧、动漫） | `https://iptv.wwjjqq.top/aptv-iptv.m3u` |
| 河南移动（HA-CMCC-IPTV） | `https://iptv.wwjjqq.top/ha-cmcc-iptv.m3u` |

## 来源与更新

地区订阅来自 [Kimentanm/aptv](https://github.com/Kimentanm/aptv)，河南移动的另一份订阅来自 [Elykia093/HA-CMCC-IPTV](https://github.com/Elykia093/HA-CMCC-IPTV)。通用订阅以 Kimentanm/aptv 为基础，另加入 [445569 的直播列表](https://iptv.445569.xyz/live.m3u) 和 [suxuang/myIPTV](https://github.com/suxuang/myIPTV) 中的电影、电视剧、动漫频道，包含虎牙影视和斗鱼影视；新增频道归入「电影」「电视剧」「动漫」三个分组。本项目约每 6 小时同步一次 M3U 文件；来源暂时不可用时，保留上次成功同步的版本。地区订阅的具体文件与来源见 [sources.json](sources.json)。

也可以使用 [GitHub Pages](https://cumtwjq.github.io/iptv-subscriptions/aptv-hnyd.m3u) 或 [GitHub Raw](https://raw.githubusercontent.com/cumtwjq/iptv-subscriptions/main/m3u/aptv-hnyd.m3u) 地址，将文件名换成表中所需的文件名即可。APTV 通用列表中的部分线路带有 APTV 专用请求标记，其他播放器是否兼容需要实际测试。

Raw 仍使用 `raw.githubusercontent.com`。如果电视所在网络访问不了该域名，可以使用上表中的外网地址或 GitHub Pages 地址。这里提供的是 M3U 列表，不转发视频流；频道能否播放仍取决于播放设备所在网络能否访问列表内的地址。
