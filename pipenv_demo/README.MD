# Python虚拟环境

## pipenv = pip + virtual-env

### 安装

> pip3 install pipenv  

### 创建虚拟环境

准备项目的虚拟环境目录：

> mkdir pipenv_demo  
> cd pipenv_demo  
> pipenv install  

然后，安装项目依赖的库：

> pipenv install requests  

项目目录下，会产生两个文件：Pipfile和Pipfile.lock  
将项目从开发环境复制到生产环境，只需要执行pipenv install就可以了，无需再次安装项目所有依赖的包  
> pipenv install  

### 其他命令

进入虚拟环境：
> pipenv shell  

退出虚拟环境：
> exit  

安装库：
> pipenv install requests  

删除库：
> pipenv uninstall requests # 删除指定库  
> pipenv uninstall --all # 删除所有库  

升级库：
> pipenv update  

查看库的信息：
> pipenv open requests  

获取本地工程路径：
> pipenv --where  

获取虚拟环境路径：
> pipenv --venv  

检查库的依赖关系：
> pipenv graph  

检查库的安全性：
> pipenv check  

删除虚拟环境：
> pipenv --rm  
