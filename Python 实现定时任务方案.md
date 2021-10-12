在日常工作中，我们常常会用到需要周期性执行的任务，一种方式是采用 Linux 系统自带的 crond 结合命令行实现。另外一种方式是直接使用Python。接下来整理的是常见的Python定时任务的实现方式。

**目录**

    利用while True: + sleep()实现定时任务
  
    使用Timeloop库运行定时任务
    
    利用threading.Timer实现定时任务
   
    利用内置模块sched实现定时任务
    
    利用调度模块schedule实现定时任务
    
    利用任务框架APScheduler实现定时任务
    
        Job 作业
        
        Trigger 触发器
        
        Executor 执行器
        
        Jobstore 作业存储
        
        Event 事件
        
        调度器
        
        APScheduler中的重要概念
        
        Scheduler的工作流程
        
    使用分布式消息系统Celery实现定时任务
    
    使用数据流工具Apache Airflow实现定时任务
    
        Airflow 产生的背景
        
        Airflow 核心概念
        
        Airflow 的架构
    
**利用while True: + sleep()实现定时任务**

    位于 time 模块中的 sleep(secs) 函数，可以实现令当前执行的线程暂停 secs 秒后再继续执行。所谓暂停，即令当前线程进入阻塞状态，当达到 sleep() 函数规定的时间后，再由阻塞状态转为就绪状态，等待 CPU 调度。
    
    基于这样的特性我们可以通过while死循环+sleep()的方式实现简单的定时任务。
    
    
    ```
    import datetime
    import time
    def time_printer():
        now = datetime.datetime.now()
        ts = now.strftime('%Y-%m-%d %H:%M:%S')
        print('do func time :', ts)
    def loop_monitor():
        while True:
            time_printer()
            time.sleep(5)  # 暂停5秒
    if __name__ == "__main__":
        loop_monitor()
    ```
    
    主要缺点：
    
        只能设定间隔，不能指定具体的时间，比如每天早上8:00
        
        sleep 是一个阻塞函数，也就是说 sleep 这一段时间，程序什么也不能操作。  
  
**使用Timeloop库运行定时任务**  

    Timeloop是一个库，可用于运行多周期任务。这是一个简单的库，它使用decorator模式在线程中运行标记函数。
        
    ```
    import time
    from timeloop import Timeloop
    from datetime import timedelta
    tl = Timeloop()
    @tl.job(interval=timedelta(seconds=2))
    def sample_job_every_2s():
        print "2s job current time : {}".format(time.ctime())
    @tl.job(interval=timedelta(seconds=5))
    def sample_job_every_5s():
        print "5s job current time : {}".format(time.ctime())
    @tl.job(interval=timedelta(seconds=10))
    def sample_job_every_10s():
        print "10s job current time : {}".format(time.ctime())
    ```
**利用threading.Timer实现定时任务**

    threading 模块中的 Timer 是一个非阻塞函数，比 sleep 稍好一点，timer最基本理解就是定时器，我们可以启动多个定时任务，这些定时器任务是异步执行，所以不存在等待顺序执行问题。
    
    Timer(interval, function, args=[ ], kwargs={ })

        interval: 指定的时间 
        
        function: 要执行的方法
        
        args/kwargs: 方法的参数
    
    备注：Timer只能执行一次，这里需要循环调用，否则只能执行一次
        
    

