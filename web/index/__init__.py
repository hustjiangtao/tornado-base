# -*- coding: utf-8 -*-
# -*- author: Jiangtao -*-

"""
每个独立的模块应至少包含如下项目：
.
├── __init__.py
├── handler.py  路由处理（必选）
├── model.py  模型（必选，可为空）
├── schema.sql  数据库创建文件（可选）
├── service.py  业务逻辑（可选）
├── tests.py  单元测试（可选）
└── url.py  路由视图（必选）
新模块需要将模块名以字符串形式注册至 apps 中的 installed_apps
"""
