# 8-bits-CPU

PC MC and bus

![image-20230829223915458](README.assets/image-20230829223915458.png)

微程序控制器与微命令编程

![image-20230831122415911](README.assets/image-20230831122415911.png)

![image-20230831122257095](README.assets/image-20230831122257095.png)

> 记一个踩过的坑：
>
> POW打开时，有可能会立即带来上升沿，而部分总线上的数据还未准备好造成莫名其妙的错误
>
> 因此需要增加一个nop来解决此问题
