# A股量化全景监控中心 - Render部署版

## 一键部署到 Render

### 方式一: Render Blueprint (推荐)

1. Fork 本项目到你的 GitHub
2. 登录 [Render Dashboard](https://dashboard.render.com)
3. 点击 **New +** → **Blueprint**
4. 选择你的仓库，Render 会自动读取 `render.yaml`
5. 点击 **Apply**，等待部署完成
6. 访问分配的域名即可

### 方式二: 手动创建 Web Service

1. 登录 [Render](https://dashboard.render.com)
2. **New +** → **Web Service**
3. 连接你的 GitHub 仓库
4. 配置:
   - **Runtime**: Docker
   - **Plan**: Free (或 Starter)
   - **Branch**: main
   - **Root Directory**: `./`
   - **Dockerfile Path**: `./Dockerfile`
5. 添加环境变量:
   - `HOST` = `0.0.0.0`
   - `PORT` = `10000`
   - `UPDATE_INTERVAL` = `300`
6. 点击 **Create Web Service**

### 方式三: 本地测试

```bash
# 1. 构建镜像
docker build -t quant-monitor .

# 2. 运行
docker run -p 10000:10000 -e PORT=10000 quant-monitor

# 3. 访问 http://localhost:10000
```

## 接入真实数据

当前使用模拟数据。接入 iFinD:

1. 修改 `backend/data_fetcher.py`:
   ```python
   fetcher = DataFetcher(use_ifind=True)
   ```

2. 在 Render Dashboard → Environment 添加:
   - `IFIND_API_KEY` = 你的密钥
   - `IFIND_API_SECRET` = 你的密钥

3. 重新部署

## 自定义标的

编辑 `backend/config.py` 中的 `STOCK_SYMBOLS`，推送后自动部署。

## 免费版限制

- 15分钟不活动后休眠（首次访问需等待唤醒）
- 每月 750 小时运行时间
- 如需 24/7 运行，升级到 Starter ($7/月)

## 技术栈

- FastAPI + WebSocket 实时推送
- Pandas/NumPy 量化计算
- 原生 JS 前端（零框架依赖）
- Docker 容器化部署
