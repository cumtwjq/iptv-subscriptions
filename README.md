# IPTV 订阅镜像

本仓库只定时复制指定的 M3U 订阅文件，不同步上游仓库，也不更改频道播放地址。

来源：

- [Kimentanm/aptv](https://github.com/Kimentanm/aptv) 的 `m3u` 目录中 16 个按省份命名的移动 IPTV 列表，以及通用的 `iptv.m3u`；跳过演示、广播、视频样例和其他用途的文件
- [Elykia093/HA-CMCC-IPTV](https://github.com/Elykia093/HA-CMCC-IPTV) 的 `public/index.m3u`

GitHub Actions 每 6 小时更新一次。来源清单见 `sources.json`；如果某次抓取失败，不会把错误页面写入订阅文件，已有文件仍保留。

## 订阅地址

在直播软件里选择「添加订阅」或「导入 M3U」，粘贴下表对应的完整地址。`https://iptv.wwjjqq.top/` 只是服务首页，订阅地址必须包含 `.m3u` 文件名。直接用浏览器打开订阅时会显示 M3U 文本；浏览器本身不会播放里面的频道。

| 订阅 | 外网地址 |
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

也可以使用 [GitHub Pages](https://cumtwjq.github.io/iptv-subscriptions/aptv-hnyd.m3u) 或 [GitHub Raw](https://raw.githubusercontent.com/cumtwjq/iptv-subscriptions/main/m3u/aptv-hnyd.m3u) 地址，将文件名换成表中所需的文件名即可。APTV 通用列表中的部分线路带有 APTV 专用请求标记，其他播放器是否兼容需要实际测试。

Raw 仍使用 `raw.githubusercontent.com`。如果电视所在网络访问不了该域名，可以使用上表中的外网地址或 GitHub Pages 地址。这里提供的是 M3U 列表，不转发视频流；频道能否播放仍取决于播放设备所在网络能否访问列表内的地址。
