# IPTV 订阅镜像

本仓库只定时复制指定的 M3U 订阅文件，不同步上游仓库，也不更改频道播放地址。

来源：

- [Kimentanm/aptv](https://github.com/Kimentanm/aptv) 的 `m3u` 目录中 16 个按省份命名的移动 IPTV 列表；跳过演示、广播、视频样例和其他用途的文件
- [Elykia093/HA-CMCC-IPTV](https://github.com/Elykia093/HA-CMCC-IPTV) 的 `public/index.m3u`

GitHub Actions 每 6 小时更新一次。来源清单见 `sources.json`；如果某次抓取失败，不会把错误页面写入订阅文件，已有文件仍保留。

## 订阅地址

把下面地址里的文件名换成 `sources.json` 中任意 `file` 字段即可：

- Raw：`https://raw.githubusercontent.com/cumtwjq/iptv-subscriptions/main/m3u/aptv-hnyd.m3u`
- Pages：`https://cumtwjq.github.io/iptv-subscriptions/aptv-hnyd.m3u`
- 飞牛 NAS：`http://NAS地址:8098/aptv-hnyd.m3u`

HA-CMCC-IPTV 的文件名是 `ha-cmcc-iptv.m3u`。

Raw 仍使用 `raw.githubusercontent.com`。如果电视所在网络访问不了该域名，换成自己的 Raw 也不能解决；可以使用 Pages 或 NAS 地址。

## 飞牛 NAS

`nas` 文件夹中提供 Docker Compose 服务。复制到 NAS 后执行 `docker compose up -d --build`。它每 30 分钟从本仓库 Pages 地址更新订阅，并缓存到 `nas/cache`；网络暂时断开时保留上次可用文件。`8098` 是示例端口，可以在 `nas/compose.yaml` 调整。

若要从外网访问，给 NAS 配置自己的 HTTPS 域名和反向代理，将该域名的一个路径或子域名转发到此服务的 `8098` 端口。此服务只缓存 M3U 列表，不转发视频流；频道能否播放仍取决于播放设备所在网络能否访问 M3U 内的地址。
