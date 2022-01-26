# python编码规范

## 分号

不要再行尾加分号，不要用分号将两条命令放在同一行。

## 行长度

每行不超过80个字符

以下情况除外:

- 长度导入模块语句

- 注释里的url

不要使用反斜杠连接行

Python会将 圆括号, 中括号和花括号中的行隐式的连接起来 , 你可以利用这个特点. 如果需要, 你可以在表达式外围增加一对额外的圆括号。

```Python
foo_bar(self, width, height, color='black', design=None , x='foo', emphasis=None, highlight=None)

if(width == 0 and height == 0 and color == 'red' and emphasis == 'strong'):
```

在注释中，如果必要，将长的url放在一行

```python

Yes:  # See details at
      # http://www.example.com/us/developer/documentation/api/content/v2.0/csv_file_name_extension_full_specification.html

```

```python

No:  # See details at
     # http://www.example.com/us/developer/documentation/api/content/\
     # v2.0/csv_file_name_extension_full_specification.html

```

## 括号

宁缺毋滥的使用括号

除非是用于实现行链接，否则不要在返回语句或条件语句中使用括号，不过 元组两边使用括号是可以的

```python
Yes: if foo:
         bar()
     while x:
         x = bar()
     if x and y:
         bar()
     if not x:
         bar()
     return foo
     for (x, y) in dict.items(): ...
```

```python

No:  if (x):
         bar()
     if not(x):
         bar()
     return (foo)

```
