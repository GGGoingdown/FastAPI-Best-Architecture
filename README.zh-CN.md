# FastAPI 最佳架构

[![GitHub](https://img.shields.io/github/license/fastapi-practices/fastapi_best_architecture)](https://github.com/fastapi-practices/fastapi_best_architecture/blob/master/LICENSE)
[![Static Badge](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/downloads/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Pydantic v2](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/pydantic/pydantic/main/docs/badge/v2.json)](https://pydantic.dev)

> [!CAUTION]
> **2024-3-22 (公告)**
>
> 主分支已完成 app 架构重构，请格外注意 sync fork 操作，以免造成不可挽回的损失！
>
> 我们保留并锁定了原始分支（legacy-single-app-pydantic-v2），您可以在分支选择器中找到它

简体中文 | [English](./README.md)

基于 FastAPI 框架的前后端分离中后台解决方案，遵循[伪三层架构](#伪三层架构)设计， 支持 **python3.10** 及以上版本

它的目的是让你可以直接用它作为你新项目的基础架构，本仓库作为模板库公开，任何人或企业均可免费使用

**🔥持续更新维护中🔥**

## 伪三层架构

mvc 架构作为常规设计模式，在 python web 中也很常见，但是三层架构更令人着迷

在 python web 开发中，三层架构的概念并没有通用标准，所以这里我们称之为伪三层架构

但请注意，我们并没有传统的多应用程序结构（django、springBoot...），如果您不喜欢这种模式，可以使用模板对其进行随意改造！

| 工作流程 | java           | fastapi_best_architecture |
|------|----------------|---------------------------|
| 视图   | controller     | api                       |
| 数据传输 | dto            | schema                    |
| 业务逻辑 | service + impl | service                   |
| 数据访问 | dao / mapper   | crud                      |
| 模型   | model / entity | model                     |

## 在线预览

你可以在 [fastapi_best_architecture_ui](https://github.com/fastapi-practices/fastapi_best_architecture_ui) 中查看部分预览截图

幸运的是，我们现在有一个演示站点: [FBA UI](https://fba.xwboy.top/)

> 测试员：tester / 123456
>
> 管理员：admin / 123456

## 特征

- [x] 使用 FastAPI PEP 593 Annotated 参数设计
- [x] async/await + asgiref 的全局异步设计
- [x] 遵循 Restful API 规范
- [x] 全局 SQLAlchemy 2.0 语法
- [x] Pydantic v1 和 v2 (不同分支)
- [x] Casbin RBAC 访问控制模型
- [x] 角色菜单 RBAC 访问控制模型
- [x] Celery 异步任务
- [x] JWT 中间件白名单认证
- [x] 全局自定义时区时间
- [x] Docker / Docker-compose 部署
- [x] Pytest 单元测试

## 内置功能

- [x] 用户管理：系统用户角色管理，权限分配
- [x] 部门管理：配置系统组织机构（公司、部门、小组...）
- [x] 菜单管理：配置系统菜单，用户菜单，按钮权限标识
- [x] 角色管理：角色菜单权限分配，角色路由权限分配
- [x] 字典管理：维护系统内部常用固定数据或参数
- [x] 代码生成：后端代码自动生成，支持预览，写入及下载
- [x] 操作日志：系统正常和异常操作的日志记录与查询
- [x] 登录认证：图形验证码后台认证登录
- [x] 登录日志：用户正常和异常登录的日志记录与查询
- [x] 服务监控：服务器硬件设备信息与状态
- [x] 定时任务：自动化任务，异步任务，支持函数调用
- [x] 接口文档：自动生成在线交互式 API 接口文档

## 项目结构

```
├─📁 backend--------------- # 后端
│ ├─📁 alembic------------- # 数据库迁移
│ ├─📁 app----------------- # 应用
│ │ ├─📁 admin------------- # 系统后台
│ │ │ ├─📁 api------------- # 接口
│ │ │ │ └─📁 v1------------ # 接口版本
│ │ │ ├─📁 crud------------ # CRUD
│ │ │ ├─📁 model----------- # 模型
│ │ │ ├─📁 schema---------- # 数据传输
│ │ │ ├─📁 service--------- # 服务
│ │ │ └─📁 tests----------- # 测试
│ │ ├─📁 generator--------- # 代码生成应用
│ │ └─📁 task-------------- # 任务应用
│ │   └─📁 celery_task----- # 任务分层
│ ├─📁 common-------------- # 公共资源
│ │ ├─📁 exception--------- # 异常
│ │ ├─📁 response---------- # 响应
│ │ └─📁 security---------- # 安全
│ ├─📁 core---------------- # 核心配置
│ ├─📁 database------------ # 数据库连接
│ ├─📁 log----------------- # 日志存储
│ ├─📁 middleware---------- # 中间件
│ ├─📁 scripts------------- # 脚本
│ ├─📁 sql----------------- # SQL文件
│ ├─📁 static-------------- # 静态文件
│ ├─📁 templates----------- # 模版
│ │ └─📁 py---------------- # py代码生成
│ └─📁 utils--------------- # 工具包
└─📁 deploy---------------- # 部署
  └─📁 backend------------- # 后端部署
    └─📁 docker-compose---- # docker部署
```

## 本地开发

* Python 3.10+
* Mysql 8.0+
* Redis 推荐最新稳定版
* Nodejs 14.0+

### 后端

1. 进入 `backend` 目录

   ```shell
   cd backend
   ```

2. 安装依赖包

   ```shell
   pip install -r requirements.txt
   ```

3. 创建一个数据库 `fba`，选择 utf8mb4 编码
4. 安装并启动 Redis
5. 在 `backend` 目录下创建 `.env` 文件

   ```shell
   touch .env

   cp .env.example .env
   ```

6. 按需修改配置文件 `core/conf.py` 和 `.env`
7. 数据库迁移 [alembic](https://alembic.sqlalchemy.org/en/latest/tutorial.html)

   ```shell
   # 生成迁移文件
   alembic revision --autogenerate

   # 执行迁移
   alembic upgrade head
   ```

8. 启动 celery worker, beat 和 flower

   ```shell
   celery -A app.task.celery worker -l info

   # 定时任务（可选）
   celery -A app.task.celery beat -l info

   # web 监控（可选）
   celery -A app.task.celery flower --port=8555 --basic-auth=admin:123456
   ```

9. [初始化测试数据](#测试数据)（可选）
10. 启动 fastapi 服务
   ```shell
   # 帮助
   fastapi --help

   # 开发模式
   fastapi dev main.py
   ```

11. 打开浏览器访问：http://127.0.0.1:8000/api/v1/docs

### 前端

跳转 [fastapi_best_architecture_ui](https://github.com/fastapi-practices/fastapi_best_architecture_ui) 查看详情

---

### Docker 部署

> [!WARNING]
>
> 默认端口冲突：8000，3306，6379，5672
>
> 建议在部署前关闭本地服务：mysql，redis，rabbitmq...

1. 进入 `deploy/backend/docker-compose` 目录，创建环境变量文件`.env`

   ```shell
   cd deploy/backend/docker-compose

   touch .env.server ../../../backend/.env

   cp .env.server ../../../backend/.env
   ```

2. 按需修改配置文件 `backend/core/conf.py` 和 `.env`
3. 执行一键启动命令

   ```shell
   docker-compose up -d --build
   ```

4. 等待命令执行完成
5. 打开浏览器访问：http://127.0.0.1:8000/api/v1/docs

## 测试数据

使用 `backend/sql/init_test_data.sql` 文件初始化测试数据

## 开发流程

（仅供参考）

1. 定义数据库模型（model）
2. 定义数据验证模型（schema）
3. 定义视图（api）和路由（router）
4. 编写业务（service）
5. 编写数据库操作（crud）

## 测试

通过 `pytest` 执行单元测试

1. 创建测试数据库 `fba_test`，选择 utf8mb4 编码
2. 使用 `backend/sql/create_tables.sql` 文件创建数据库表
3. 使用 `backend/sql/init_pytest_data.sql` 文件初始化测试数据
4. 进入 `backend` 目录，执行测试命令

   ```shell
   cd backend/

   pytest -vs --disable-warnings
   ```

## 状态

![Alt](https://repobeats.axiom.co/api/embed/b2174ef1abbebaea309091f1c998fc97d0c1536a.svg "Repo beats analytics image")

## 贡献者

<a href="https://github.com/fastapi-practices/fastapi_best_architecture/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=fastapi-practices/fastapi_best_architecture"/>
</a>

## 特别鸣谢

- [FastAPI](https://fastapi.tiangolo.com/)
- [Pydantic](https://docs.pydantic.dev/latest/)
- [SQLAlchemy](https://docs.sqlalchemy.org/en/20/)
- [Casbin](https://casbin.org/zh/)
- [Ruff](https://beta.ruff.rs/docs/)
- ...

## 互动

[微信 / 扣扣](https://github.com/wu-clan)

## 赞助我们

如果此项目能够帮助到你，你可以赞助作者一些咖啡豆表示鼓励：[:coffee: Sponsor :coffee:](https://wu-clan.github.io/sponsor/)

## 许可证

本项目由 [MIT](https://github.com/fastapi-practices/fastapi_best_architecture/blob/master/LICENSE) 许可证的条款进行许可

[![Stargazers over time](https://starchart.cc/fastapi-practices/fastapi_best_architecture.svg?variant=adaptive)](https://starchart.cc/fastapi-practices/fastapi_best_architecture)
