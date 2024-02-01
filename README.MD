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

在相应类别下创建自定义命名的子目录，并在改目录下创建 part.py 文件，其中定义 part 函数（可带参数），part 函数返回相应实例即可。具体可参见已有部件的实现。

## 创建 c++ 实现的部件

### 编译系统准备

1. 已安装相应的 c++ 编译器
2. 已安装 xmake
3. 已安装 hikyuu

### 创建部件

通过 setup.py 中的 create 命令创建相应的部件，参数 -t 指明部件类别，-n 指定部件名称，如下创建一个名为 example 的指标部件：

```shell
python setup.py create -t ind -n example
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
