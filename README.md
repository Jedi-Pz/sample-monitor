# sample monitor

## 介绍
PC和移动设备投屏软件


## 安装教程
### 环境

1. OS:win11
2. IDE:VS2022，工作负荷勾选C++桌面开发，单个组件勾选最新V143带spectra的生成工具
3. SDK:10.0.22621
4. WDK:10.0.22621.382

## 使用说明
### IddSampleDriver 使用说明
> 在安装好上述环境后进行如下操作可以生成驱动和安装挂载程序
1. 使用VS2017以上的VS打开./server/IndirectDisplay/IddSampleDriver.sln
2. 对于项目IddSampleDriver，项目属性->C/C++->运行库=多线程
3. 对于项目IddSampleApp,项目属性->C/C++->运行库=多线程调试
4. 两个项目的SDK都应设置为10.22621（如果有未知变量的报错，大概率是这个问题）项目属性->常规->SDK=10.22621或者10.0（最新安装的版本）
5. 重新生成解决方案，在./x64/debug下以管理员身份运行IddSampleApp.exe，可以挂载、卸载驱动以及录制10秒的测试视频

