# HAL库

HAL库（Hardware Abstraction Layer Library）是STM32微控制器的硬件抽象层库，旨在为开发者提供一个简化、统一的编程接口来操作STM32微控制器的硬件。



# GPIO的8种模式

|     输出     |   输入   |
| :----------: | :------: |
|   推挽输出   | 浮空输入 |
|   开漏输出   | 上拉输入 |
| 复用推挽输出 | 下拉输入 |
| 复用开漏输出 | 模拟输入 |

![内部图像](C:\Users\12396\Documents\WeChat Files\wxid_fwk1goc10cu322\FileStorage\Temp\9255301b4620d485851b73684832f7d.png)

## 推挽输出

P-MOS和N-MOS配合工作，提供3.3V和0V。

## 开漏输出

只有N-MOS工作，可由外部提供3V或者5V（需要使用5V耐受的IO口）。

![62da1f567b8b2a9a73b0d2b25e6c1da](C:\Users\12396\Documents\WeChat Files\wxid_fwk1goc10cu322\FileStorage\Temp\62da1f567b8b2a9a73b0d2b25e6c1da.png)

![80b40c456774286415fbd5c30aa1cc8](C:\Users\12396\Documents\WeChat Files\wxid_fwk1goc10cu322\FileStorage\Temp\80b40c456774286415fbd5c30aa1cc8.png)

## 浮空输入

两个电阻都不启用

## 上拉输入

VDD上拉电阻接通

## 下拉输入

VSS上拉电阻接通



## 施密特触发器/TTL触发器

![施密特触发器](C:\Users\12396\Documents\WeChat Files\wxid_fwk1goc10cu322\FileStorage\Temp\f9ff80a59587c277612f23b88d6b182.png)



# 中断

​	指令出错，定时器结束，串口接受数据，GPIO电平发生变化等事件都可能导致**中断**

## 外部中断

由GPIO口引起

![image-20240110105149511](C:\Users\12396\AppData\Roaming\Typora\typora-user-images\image-20240110105149511.png)

![image-20240110105259867](C:\Users\12396\AppData\Roaming\Typora\typora-user-images\image-20240110105259867.png)

![image-20240111145536714](C:\Users\12396\AppData\Roaming\Typora\typora-user-images\image-20240111145536714.png)

# 串口

单片机最常见的串口是TTL串口。

发送的IO口称为TX（Transmit），接收的IO口成为RX（Receive）

![image-20240111145934583](C:\Users\12396\AppData\Roaming\Typora\typora-user-images\image-20240111145934583.png)

共地是为了保证电压的相对值。

串口通讯时需要保持相同的**比特率**。

## 轮询模式

stm32串口内部由两个寄存器：**发送数据寄存器（TDR）**和**发送位移寄存器**。

调用HAL_UART_Transmit发送数据的时候，stm32的CPU依次将数据转移至寄存器，按照设置好的比特率转换成高低电平从TX输出。TDR中的数据会在发送位移寄存器中的数据发送完成后转移到发送位移寄存器。

![image-20240111150839834](C:\Users\12396\AppData\Roaming\Typora\typora-user-images\image-20240111150839834.png)

此过程中CPU会不断查询数据是否在两个寄存器间完成转移，知道数据发送完成或者设定的时间结束。

轮询模式下的串口接收类似，CPU会不断查询RDR中是否有新的数据并转移数据。

![image-20240111151158864](C:\Users\12396\AppData\Roaming\Typora\typora-user-images\image-20240111151158864.png)

轮询模式下CPU需要不断查询，无法执行其他指令。

## 串口的中断模式

中断模式可以解决轮询模式下CPU阻塞的问题。

中断模式下的串口发送时，CPU将数据从TDR转移后就可以去执行其他任务，当发送位移寄存器数据发送后，会触发**发送数据寄存器中断**，将CPU叫回。如此反复，直至完成数据发送或者超时。

类似的，接收数据时，每当一帧数据从接受位移寄存器存入RDR时，都会触发**接收数据寄存器非空**中断，将CPU叫回。HAL库已经做好了封装，只有当接受了设定好的字节数，即接收完成时才会触发回调函数HAL_UART_RxCpltCallback()。我们可以将需要执行的代码写入这个函数中,但是并不推荐在HAL库中写入代码。因此,这个函数前有一个__weak弱定义关键字，即我们可以在其他地方重新定义这个函数，Tx也有类似的函数。在工程中，我们往往单独开一个文件写入定义。

由于不能再while循环中写入串口中断模式的接受和发送，我们可以**在回调函数的结尾再次写入接受或者发送的函**以完成循环。

中断模式使用的函数与轮询模式类似，多一个_IT。

## 回调函数（CallBack）

当有事件发生时就会调用这个函数。



一个错误案例：

```c
void HAL_UART_RxCpltCallback(UART_HandleTypeDef *huart) 
{ 
	HAL_UART_Transmit_IT(&huart1, recieveData, 2); 
	HAL_Delay(100); 
	HAL_UART_Transmit_IT(&huart1, message, strlen(message));
 }
```

串口助手最终只传回了一条信息

解决：

可能有几个原因：

1. **串口缓冲区溢出**：
   - 如果 `receiveData` 和 `message` 两条消息的发送间隔太短，第一条消息可能还没有完全发送完毕，这可能导致第二条消息的一部分或全部被丢弃。

2. **异步传输中断问题**：
   - 使用 `HAL_UART_Transmit_IT` 进行异步传输时，数据的发送是在中断服务程序中完成的。如果中断优先级设置不当，或者中断服务程序中有问题，可能导致数据没有被完全发送。

3. **延时的使用**：
   - 虽然在两次传输之间使用了 `HAL_Delay(500)` 延时，但这可能不足以保证第一次传输完成。`HAL_Delay` 只是简单地等待一段时间，而不是等待串口传输完成。

4. **串口配置或助手软件问题**：
   - 检查您的串口配置（波特率、数据位、停止位、奇偶校验等）是否与串口助手软件的配置一致。
   - 确保串口助手软件能够正确处理连续的串口数据。

**解决这些问题的一种方法是在 `HAL_UART_TxCpltCallback` 中处理第二次传输**，该回调函数会在第一次传输完成时被调用。这样可以确保第一次传输完全完成后，再开始第二次传输。同时，检查和调整串口配置和中断优先级设置，确保它们适合您的应用场景。

## DMA模式

DMA（direct memory access）模式可以进一步节省CPU，并接受不定长的数据。

我们可以创建一条DMA通道，告诉DMA需要将数据从哪里传输到哪里，DMA就会自动传输数据，在传输完成的时候触发中断。

![image-20240111163357169](C:\Users\12396\AppData\Roaming\Typora\typora-user-images\image-20240111163357169.png)

![image-20240111163414071](C:\Users\12396\AppData\Roaming\Typora\typora-user-images\image-20240111163414071.png)

DMA模式中需要设置通道，地址自增等参数，这些以后再详细说。

## 接收不定长数据

该功能依赖**串口空闲中断**实现。该中断与接受的数据长度无关，只有当RX引脚上无数据加入后触发，即空闲**（ldle）**时触发。使用函数**HAL_UARTEx_ReceiveToIdle**，同样有弱定义的回调函数，通常我们会在函数的开头确认是否是目标串口触发了回调函数，并在结尾也写上接受函数以实现循环。

# 蓝牙模块

蓝牙分为**经典蓝牙**和**低功耗蓝牙（BLE）**。蓝牙通讯分为**主机**和**从机**。

* 具体流程

  从机向外广播自己的信息

  主机扫描到子机后发起连接