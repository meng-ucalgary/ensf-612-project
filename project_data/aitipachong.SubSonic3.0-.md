	l SubSonic 3.0简介
         SubSonic是Rob Conery用C#语言写的一个ORM开源框架，使用BSD软件授权许可（The BSD 3-Clause License）。它是一个实用的快速开发框架，通过非常简单的配置，以及附带的T4模板，就可以帮我们生成强大的数据访问层工具，让开发人员远离SQL语句的拼接，专注于业务逻辑的开发。
         SubSonic 3.0适合短、平、快的中小型项目开发，支持MsSql、MySql与SQLite三种数据库，支持Linq和支持事务。对数据库操作灵活，对生成的SQL语句会自动进行优化，虽然是ORM框架，但在性能上并没有太大的损失。它上手容易，是一个非常棒的ORM开发框架。
         3.0版本最大的缺点是框架未开发完善，对多表关联查询支持的不是很好，只支持一个多表关联条件（复杂的多表关联只能使用存储过程或SQL语句拼接方式来实现）；条件语句对In与Not In不支持（需要在数据层重新封装处理才行）；如果使用Redis缓存的话，存储数据时对subsonic3.0生成的实体有兼容问题，需要做一次转换封装后才能使用。

	l SubSonic3.0安装说明
        SubSonic3.0安装练习相关附件下载

        在MsSql中新建一个数据库SubSonicTest，并设置好登录账户与密码为SubSonicTest。
        运行下载包里的“SQL语句.txt”文件里的语句，生成数据表、记录与测试用的存储过程。
	
        


	使用Visual Studio 创建一个空白解决方案
	
	
	在解决方案中创建一个空Web应用程序项目
	
	
	将下载包里的SubSonic文件夹复制进项目文件夹中
	
	
	刷新项目就可以看到隐藏的SubSonic文件夹
	
	
	打开Web.config，添加数据库连接字符串
	
	
	将下载包里面的Dll和SubSonic.Core复制到解决方案中
	
	
	添加SubSonic3.0项目（直接使用源码项目，方便在使用时调试及修改）
	
	
	
	
	
	

	在Web工程中添加SubSonic.Core项目和Castle.Core.dll引用
	
	
	
	
	
	将SubSonic包含进项目中
	
	
	如果数据库名称、账户和密码设置同前面要求一样的话，T4模板将会直接运行生成相关实体类；如果设置不一样的，请按下面要求进行设置：
	1、打开Web项目内，SubSonic文件夹内的Settings.ttinclude配置文件，进行设置指定内容
	
	
	
	

	2、设置好后，选择全部T4模板文件（即：.tt文件），运行生成代码
	
	
	
	
	l SubSonic3.0模板介绍说明
	文本中介绍附件中的SubSonic文件夹模板（MsSql），不适用官方发布的模板
	文件名称	说明
	ActiveRecord.tt	按数据表生成对应名称的类实体（Model），以及支持lambda表达式的各种常用函数（包括：增、改、查、删、Exists等）
	Context.tt	生成常用公共模板函数：Select、Insert、Avg、Count、Max、Min、Variance、StandardDeviation、Sum、Delete、GetQuery、Update等
	EntityTable.tt	新增模板（原SubSonic3.0没有这个模板，里面的功能从Struct.tt模板中分离出来的），主要功能是可直接获取数据表名称与字段名称，减少开发中硬编码的存在。
	CreateModel.tt	新增模板（原SubSonic3.0没有这个模板），主要功能是数据表生成对应名称的类实体（Model），这是普通的实体类，不附任何多余的内容（函数），主要用于存储到Redis缓存或做C/S接口通讯时转JSON使用。非必须项。
	Settings.ttinclude	模板参数配置
	SQLServer.ttinclude	MqSql数据库读取、生成的相关配置
	StoredProcedures.tt	生成存储过程调用函数（本模板生成的函数调用存储过程非常方便，详情请关注例子）
	Structs.tt	生成表结构模板，提供给SubSonic插件使用

	l SubSonic3.0使用例子
	点击下载本文例子的解决方案源码
	












