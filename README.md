# practice
用于学习和复习
1.os.walk()的使用
返回三元组，
a，b,c=os.walk(target)
a表示target目录下的目录
b,表示a目录下的目录列表，不包含.与..
c表示a目录下的文件列表，相对路径，不是绝对路径
windows上的使用需要特别注意编码问题，这地方仍然有坑

pickle模块可以python方式存储结果到文件，并读取使用

topdown为true表示广度优先遍历，false表示深度优先  
2.python的多线程模块
创建方法，lock,rlock，信号量，event,local,
condition
及基本用法  
3.迭代器的基本用法
例中生成斐波那契数列数列，并可多次访问
定义__iter__与next方法，可使用列表生成式操作
为避免对象只能使用一次，在停止时重设初始变量，从而一个对象可完整遍历无数次
4,git的branch操作
学习合并冲突

