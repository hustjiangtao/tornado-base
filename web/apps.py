# -*- coding: utf-8 -*-
# -*- author: Jiangtao -*-

"""
apps 将项目下所有独立的模块注册至 installed_apps
根据 installed_apps 获取所有模块的 模型（model）和路由（url）
由 importlib 导入所有 模型（model）和路由（url）
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

installed_apps = [
    'index',
    'health',
    'auth',
    # 'cto51',
]

import importlib
# apps = (importlib.import_module(f'web.{app}') for app in installed_apps)
apps_model_modules = [importlib.import_module(f'web.{app}.model') for app in installed_apps]
app_url_modules = [importlib.import_module(f'web.{app}.url') for app in installed_apps]
# for x in app_url_modules:
#     print(x.URL_HANDLERS)
