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
5.git的diff命令会默认显示变动位置
上下文三行的内容

4,git的branch操作
master的操作,学习合并冲突
如果合并分支和待合并分支都有添加的操作，那么merge就会失败，就需要手动操作
新分支策略

添加的新内容
修复bug
测试stash，用于临时保存未修改内容
当在分支上做了工作，还没有提交时（可已经add)，可使用gitstash存储起来，
git stash list可查看当前存储的内容，
后续使用git stash pop恢复工作区内容，pop在恢复后会删除内容
git reflog可查看命令历史
不使用fast forward模式的好处是会保存合并的历史，参数git merge --no-ff -m "something instruction" branchname
在分支上的工作如果没有commit，就切换到其他分支，会丢失结果，也会造成异常，事实上无法切换
强制删除git branch -D branchname,比如无用的临时分支
test diff  
5,eval的作用  
eval(字符串语句)将字符串作为一个语句去执行
format这种方式语句有引号
比如
"somthing {}".format()
就需要将整个语句包装为字符串，在打印的时候也是可用作输出的格式
比如a="world"，print a的时候，显示为world，eval(a)显示的也会是无引号的方式，会去除一层引号

print eval("flag[0]"),会取出flag 0位置的值
相当于取出外围的一层引号

 
6,python -m和python直接运行
-m以模块方式运行，会把执行目录放到sys.path中，后续跟着的执行文件需要是一个模块，即需要__init__.py文件
直接运行的方式，会将脚本所在目录放入sys.path中，如果在模块2中相对路径导入模块1中的脚本，则需以-m方式运行


7,开源项目虚拟环境使用
virtualenv --no-site-packages venname 创建一个虚拟环境，不复制原来的包
指定python解释器：
virtualenv -p /usr/bin/python2.7 venname解释器的具体数值可以在~/.bashrc中找，一个是python3,7一个是python2.7
souce venname/bin/active激活虚拟环境
deactivate停止
django与mysql的数据通信
makemigrations
migrate
需要在setting下配置数据库的host，数据库名，密码等

