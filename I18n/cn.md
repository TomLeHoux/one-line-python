![One Line Python](../imgs/banner.png)

---

[<img src="../imgs/lang.gif" width=40% align="right">](./index.md)

忘记在您的代码中使用多行。将一切压缩到一行中并完成所有任务。数组是您的盟友，让您能够以单行代码执行以前需要多行完成的所有任务。

# 简介
欢迎来到 One Line Python 存储库！在这里，我们通过挑战自己在一行代码内完成任务，探索编写简洁的 Python 代码的艺术。该存储库旨在展示各种编程问题的创造性和高效解决方案，全部都压缩到一行中。

# 目录

- [简介](#简介)
- [目录](#目录)
- [规则](#规则)
- [代码概念](#代码概念)
  - [变量](#变量)
    - [使用 `list` 数据类型。](#使用-list-数据类型)
      - [修改值。](#修改值)
    - [使用 `dict` 数据类型。](#使用-dict-数据类型)
      - [修改值。](#修改值-1)
    - [修改全局变量。](#修改全局变量)
      - [修改值。](#修改值-2)
  - [条件语句](#条件语句)
    - [一系列的 if 语句](#一系列的-if-语句)
  - [函数](#函数)
  - [模块](#模块)
  - [While 循环](#while-循环)
  - [类](#类)
- [贡献](#贡献)
- [许可证](#许可证)


# 规则

1. 所有代码必须仅使用一行，包括任何导入的文件（标准和外部模块/库除外）。
2. 不要使用 `;` 作为行分隔符。
3. 不要使用 `exec()`。

下面，您将找到不同概念的一行格式。请记住，这些解决方案可能并非总是最高效或适合每种情况。它们是特定案例的解决方案。

# 代码概念

## 变量

我找到了一些定义和修改变量的解决方案：

### 使用 `list` 数据类型。

当您只需要使用一个变量时，推荐使用此方法。

**语法**
```py
[... for variable in [value]]
```

您可以尝试添加更多值，但通常不推荐这样做。

#### 修改值。

我找到的修改变量值的解决方案不寻常但有效：

**语法**
```py
[variable.replace(variable, new_value) for variable in [value]]
```

### 使用 `dict` 数据类型。

当您需要使用多个变量时，这是一个很好的选择。

**语法**
```py
[... for variables in [{'variable_A': 'value', 'variable_B': 'value', ...}]]
```

#### 修改值。

使用 `.update` 方法来更改变量的值。

**语法**
```py
[variables.update({'variable_A': 'new value'}) for variables in [{'variable_A': 'value', 'variable_B': 'value', ...}]]
```

### 修改全局变量。

与前一种方法类似，我们可以更新全局变量以添加自己的变量。此方法更有趣，因为它允许我们像传统定义的变量一样使用它。

**语法**
```py
[globals().update({'variable':'value'})]
```

#### 修改值。

由于我们不能使用 `=` 更改变量的值，因此我们可以使用修改 `dict` 变量的方法。

**语法**
```py
[globals().update({'variable':'new_value'})]
```

## 条件语句

如果您已经习惯在数组中使用 `if-else` 语句，可以跳过此主题，因为在实现上没有太大变化

。

在 `for` 语句后面可以添加一个独立的 `if` 语句，而无需 `else`：

**语法**
```py
[for variable in [value] if condition]
```

如果需要 `else` 语句，可以在 `for` 语句之前添加条件：

**语法**
```py
[... if condition else ... for variable in [value] ]
```

如果需要 `elif` 语句，可以在 `else` 部分内部添加额外的 `if` 语句：

**语法**
```py
[... if condition else (... if condition else ...)  for variable in [value] ]
```

> 括号是可选的；它们只是为了更好的可视化效果。

### 一系列的 if 语句

有各种不同目的的场景。在需要一系列返回不同值的 `if` 语句序列而又不使用 `else` 的情况下，可以将 `else` 条件表示为 `None`：

**语法**
```py
[[... if condition else None, ... if condition else None] for variable in [value] ]
```

使用此方法的问题是数组中存在 `None` 值。如果这会带来问题，您可以使用 `filter` 结合 `list` 去除这些 `None` 值：

**语法**
```py
[list(filter(lambda condition_result: condition_result != None, [... if condition else None, ... if condition else None])) for variable in [value] ]
```

**示例**

```py
[list(filter(lambda condition_result: condition_result != None, ['大于 10' if number > 10 else None, '大于 20' if number > 20 else None])) for number in [11]]
```

**等同于**
```py
number = 40
if number > 10: print('大于 10')
if number > 20: print('大于 20')
```

## 函数

一行函数的解决方案是使用 `lambda`。不需要使用 `return`。定义变量的所有方法都可以应用在这里。

**语法** *(list)*
```py
[function() for function in [lambda parameter: ...]]
```
**语法** *(dict)*
```py
[variables['function']() for variables in [{'function': lambda parameter: ...}]]
```
**语法** *(global)*
```py
[globals().update({'function': lambda parameter: ...})]
```

**示例**

```py
[[odd(number) for number in [2,11,5]] for odd in [lambda number: "偶数" if number % 2 == 0 else "奇数"]]
```

**等同于**
```py
def odd(number):
    if number % 2 == 0: return "偶数"
    return "奇数"

odd(2) # 偶数
odd(11) # 奇数
odd(5) # 奇数
```

## 模块

要导入模块，可以使用与定义和使用 `__import__` 函数相同的概念。这样，我们可以完全导入模块：

**语法**
```py
[... for module in [__import__('

module_name')]]
```

**示例**

```py
[os.listdir('./') for os in [__import__('os')]]
```

**等同于**

```py
import os
os.listdir('./')
```

## While 循环

要创建一个 `while` 循环，我们需要使用递归：

**语法**
```py
[while_loop(while_loop) for while_loop in [lambda cycle: [..., cycle(cycle) if condition else None][1]]]
```

**示例**

```py
[globals().update({'i':0}), [while_loop(while_loop) for while_loop in [lambda cycle: [[print(i), globals().update({'i':i+1})], cycle(cycle) if i <= 5 else None][1]]]]
```

**等同于**

```py
i = 0
while i <= 5:
    print(i)
    i += 1
```

这里是另一个例子：

**示例**

```py
[[while_loop(while_loop) for while_loop in [lambda cycle: [[print(odd(number)) for number in [int(input('Number: '))]], cycle(cycle)][1]]] for odd in [lambda number: "奇数" if number % 2 == 0 else "偶数"]]
```

**等同于**
```py
def odd(number):
    if number % 2 == 0: return "偶数"
    return "奇数"

while True:
    number = int(input("Number: "))
    print(odd(number))
```

## 类

我为创建一个 `class` 想到的方法是使用 `lambda` 和 `SimpleNamespace`：

**语法**
```py
[globals().update({'SimpleNamespace': __import__('types').SimpleNamespace}), globals().update({'class_name': lambda parameters: [<init code>, SimpleNamespace(**{'method': lambda parameters: ...})][1]})]
```

**示例**
```py
[globals().update({'SimpleNamespace': __import__('types').SimpleNamespace}), globals().update({'Cat': lambda name: [print(f"Your cat's name is {name}."), SimpleNamespace(**{'meow': lambda: print(f'{name}: 喵！')})][1]}), Cat('Tom').meow()]
```

**等同于**
```py
class Cat:
     def __init__(self, name) -> None:
         self.name = name
         print(f"Your cat's name is {self.name}.")
    
     def meow(self) -> None:
         print(f'{self.name}: 喵！')

Cat('Tom').meow()
```

# 贡献

非常感谢对 One Line Python 仓库的贡献！如果您有创意的一行代码解决方案或者想要改进现有的代码，请按照以下步骤操作：

1. Fork 该仓库。
2. 为您的功能或错误修复创建一个新分支。
3. 使用清晰简明的信息提交您的更改。
4. 推送您的更改到您 Fork 的仓库。
5. 提交一个详细描述您更改的拉取请求。

# 许可证
One Line Python 仓库基于 MIT 许可证。