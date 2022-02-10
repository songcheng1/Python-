# Hook步骤：

#   1.寻找hook点

#   2.编写hook逻辑

#   3.调试

old_func = func
func = function(argument){
  my task;
  return func.apply(argument)
}
#抹除hook痕迹

func.prototype... = ...

# func:要hook的函数
  
# 对象中属性的hook公式：

old_attr = obj.attr
Object.defineProperty(obj,'attr',{
  get:function(){
    debugger;
    return old_attr
  },
  set:function(val){
    return ...  
  }
})
