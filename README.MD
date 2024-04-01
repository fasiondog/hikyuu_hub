Hikyuu 策略仓库

+ ind 指标部件
+ part 策略部件
  + af 资产分配策略
  + se 选股策略
  + ev 市场环境判定策略
  + cn 系统有效性策略
  + sg 信号指示器
  + pg 盈利目标策略
  + st 止损/止盈策略
  + sp 移滑价差算法
+ sys 交易系统策略
+ prtflo 资产组合策略
+ other 其他

## 创建纯 python 实现的部件

执行 setup.py 中的 create 命令，参数 -t 指明部件类别，-n 指定部件名称，如下创建一个名为 example 的指标部件：

```shell
python setup.py create -t ind -n example -cpp
```

## 创建 c++ 实现的部件

### 编译系统准备

1. 已安装相应的 c++ 编译器
2. 已安装 xmake
3. 已安装 hikyuu

### 创建部件

通过 setup.py 中的 create 命令创建相应的部件时，需要通过参数"-cpp"明确指明，如：

```shell
python setup.py create -t ind -n example -cpp
```

将在指定类别的目录下创建相应目录及相关文件。

在生成的文件中，修改 export.cpp，在其中实现自己的逻辑即可（即"my_part"的实现）。可参考 cn/ma 下的均线系统判断条件实现。另外，可在 part.py 中，修改 part() 的帮助说明。其他生成文件不要修改。

复杂实现，可以自行添加其他 c++ 源文件进行实现。

### 编译部件

使用 build 命令编译指定部件，如：

```shell
python setup.py build -t ind -n example
```

使用 buildall 命令编译所有 c++ 部件，如:

```shell
python setup.py buildall
```

清理部件

使用 clear, clearall 命令执行清理，使用方法同 build, buildall 命令

## 删除部件

直接手工删除相应目录即可

## C++ 部件注意事项

初次下载 hub 仓库时，已有的 c++ 部件不会自动编译，也无法使用。需要执行下述命令后，根据当前的系统环境更新，并执行编译后方可使用。

执行更新命令，将根据当前系统环境更新已有的所有 c++ 部件编译设置

```shell
python setup.py update
```

编译所有c++部件

```shell
python setup.py buildall
```

## 在 hikyuu.interactive 中使用 c++ 部件

在 hikyuu.interactive 中封装了 hub setup.py 中的相关命令，使用 build_hub 调用即可，如：

```python
from hikyuu.interactive import *
build_hub('default', 'update')
build_hub('default', 'buildall')
build_hub('default', 'create -t ind -n example')
```

注意：

windows系统中，由于动态库在使用时无法被替换，可能需要到 hub 仓库所在目录下执行编译

## 测试部件

每一个使用 create 命令创建的部件，都会同时创建一个 test.py，可以在其中编写相应的测试代码

使用 test 命令执行部件测试，如:

```shell
python setup.py test -t part_type -n part_name
```

使用 testall 命令执行全部部件测试，如：

```shell
python setup.py testall
```
