# 中文车牌识别服务

1. 公有云API识别调用的不便：

   1. 需要配置一整套 API 验证等工作
   2. 用户需要额外花费
   3. 图片位置会涉及多一次的传输（除非图片和 API 都在某个公有云 API 账号下）

2. 本地优势：快速识别

3. 集成服务的优势：

   1. 优先使用本地识别
   2. 识别失败可以调用备用的公有云 API 进行识别（可选）

## 使用说明

启动服务：

```shell
docker run -it --rm -e CORS="true" -p 3000:3000 ooclab/ga.npr:v0.0.1
```

调用接口测试：

```shell
curl -X POST \
  http://127.0.0.1:3000/lpr \
  -H 'Content-Type: application/json' \
  -d '{
"url": "https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=2050338583,3464354364&fm=26&gp=0.jpg"
}'
```

返回示例：

```json
{
    "status": "success",
    "data": {
        "lp": "黑L53710",
        "precision": 0.9421328561646598,
        "pos": [
            356,
            20,
            566,
            78
        ]
    }
}
```

接口文档：[http://apidoc.ooclab.com/?url=http://127.0.0.1:3000](http://apidoc.ooclab.com/?url=http://127.0.0.1:3000)

## 参考

当前车牌识别功能使用 [HyperLPR](https://github.com/zeusees/HyperLPR) 。
