1、根据「时间范围」定时查询jira问题数据
    
    「今天-明天」

2、进行数据落库
  
    「通过Replace语句，数据不存在即插入，数据存在即更新」

3、从表里根据「创建日期」查询数据
     
    「根据dataSearch从数据库获取落库的bug数据」

4、触发定时任务
     
    「
      每隔1小时，执行jira问题爬取任务

      每天18：00，执行定时钉钉推送任务
     」