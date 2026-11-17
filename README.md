# IPTV 订阅镜像

本仓库只定时复制指定的 M3U 订阅文件，不同步上游仓库，也不更改频道播放地址。

来源：

- [Kimentanm/aptv](https://github.com/Kimentanm/aptv) 的 `m3u` 目录中 16 个按省份命名的移动 IPTV 列表，以及通用的 `iptv.m3u`；跳过演示、广播、视频样例和其他用途的文件
- [Elykia093/HA-CMCC-IPTV](https://github.com/Elykia093/HA-CMCC-IPTV) 的 `public/index.m3u`

GitHub Actions 每 6 小时更新一次。来源清单见 `sources.json`；如果某次抓取失败，不会把错误页面写入订阅文件，已有文件仍保留。

## 订阅地址

把下面地址里的文件名换成 `sources.json` 中任意 `file` 字段即可：

- Raw：`https://raw.githubusercontent.com/cumtwjq/iptv-subscriptions/main/m3u/aptv-hnyd.m3u`
- Pages：`https://cumtwjq.github.io/iptv-subscriptions/aptv-hnyd.m3u`
- 飞牛 NAS：`http://NAS地址:8098/aptv-hnyd.m3u`

HA-CMCC-IPTV 的文件名是 `ha-cmcc-iptv.m3u`。
APTV 通用列表的文件名是 `aptv-iptv.m3u`；其中一些线路带有 APTV 专用请求标记，其他播放器是否兼容需要实际测试。

Raw 仍使用 `raw.githubusercontent.com`。如果电视所在网络访问不了该域名，换成自己的 Raw 也不能解决；可以使用 Pages 或 NAS 地址。

## 飞牛 NAS

飞牛 NAS 上已部署 `iptv-m3u-cache` 项目，目录是 `/vol2/1000/docker/iptv-m3u-cache`，使用 `8098` 端口。项目直接运行 Python 基础镜像，不需要构建镜像。启动时从本仓库 Pages 下载服务程序，之后每 30 分钟更新订阅，并缓存到该目录的 `cache` 文件夹；订阅源暂时不可访问时保留上次可用文件。

在其他 NAS 上部署时，先拉取 `docker.1ms.run/library/python:3.13-slim` 镜像，再将 `nas/compose.yaml` 复制到项目目录，执行 `docker compose up -d`。首次启动需要能访问本仓库的 GitHub Pages。

若要从外网访问，给 NAS 配置自己的 HTTPS 域名和反向代理，将该域名的一个路径或子域名转发到此服务的 `8098` 端口。此服务只缓存 M3U 列表，不转发视频流；频道能否播放仍取决于播放设备所在网络能否访问 M3U 内的地址。
