# IPTV M3U 订阅

这里提供按地区整理的移动 IPTV 订阅和通用订阅。复制下方对应的 `.m3u` 地址，添加到支持 M3U 的电视直播应用或播放器即可。

## 使用方法

1. 从下表选择所在地区的订阅；也可以尝试「APTV 通用」或「HA-CMCC-IPTV」。
2. 在直播应用中找到「添加订阅」「导入 M3U」等入口，粘贴完整地址。
3. 等待应用加载频道列表。若频道无法播放，请检查所用网络是否能访问该频道的播放地址；不同地区、运营商的线路可能有访问限制。

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
| APTV 通用 | `https://iptv.wwjjqq.top/aptv-iptv.m3u` |
| HA-CMCC-IPTV | `https://iptv.wwjjqq.top/ha-cmcc-iptv.m3u` |

## 来源与更新

订阅列表来自 [Kimentanm/aptv](https://github.com/Kimentanm/aptv) 和 [Elykia093/HA-CMCC-IPTV](https://github.com/Elykia093/HA-CMCC-IPTV)。本项目约每 6 小时同步一次 M3U 文件；来源暂时不可用时，保留上次成功同步的版本。具体文件与来源见 [sources.json](sources.json)。

也可以使用 [GitHub Pages](https://cumtwjq.github.io/iptv-subscriptions/aptv-hnyd.m3u) 或 [GitHub Raw](https://raw.githubusercontent.com/cumtwjq/iptv-subscriptions/main/m3u/aptv-hnyd.m3u) 地址，将文件名换成表中所需的文件名即可。APTV 通用列表中的部分线路带有 APTV 专用请求标记，其他播放器是否兼容需要实际测试。

Raw 仍使用 `raw.githubusercontent.com`。如果电视所在网络访问不了该域名，可以使用上表中的外网地址或 GitHub Pages 地址。这里提供的是 M3U 列表，不转发视频流；频道能否播放仍取决于播放设备所在网络能否访问列表内的地址。
