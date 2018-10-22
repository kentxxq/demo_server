# demo_server

20181016
---
在app的`__init__.py`中其实可以把`jsonrpc=JSONRPC()`放到api里的`__init__.py`。看过源码，是直接挂在到了`/api`上的。这样可以省略一部分代码
```python
from app.api import api as api_blueprint
app.register_blueprint(api_blueprint, url_prefix='/api')
```
但是大家都是放在app内，可能是为了更加清晰的项目结构。同时也可以更方便的控制挂载节点吧！

20181017
---
把`vue-element-admin`整合进来。
1. 打包出来的`index.html`放入templates文件夹,同时修改它的favicon为`/static/favicon.ico`
2. `static`文件夹覆盖掉
3. 把`favicon.ico`放入`static`中

20181022
---
试试从gitlab推送到github  


