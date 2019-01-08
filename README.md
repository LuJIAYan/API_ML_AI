## 项目介绍
<table>
    <tr>
        <td><b>Target release</b></td>
        <td>2018/1/9</td>   
    </tr>
    <tr>
        <td><b>Epic</b></td>
        <td>“毕业通”APP</td>   
    </tr>
	<tr>
        <td><b>完成情况</b></td>
        <td><b><code>完成</code></b></td>
    </tr>
    	<tr>
        <td><b>Document Status</b></td>
        <td>4.0</td>
    </tr>  
    <tr>
        <td rowspan="1"><b>ower</b></td>
        <td><a href="https://github.com/LuJIAYan">@LuJIAYan</a></td>
    </tr>
    <tr>
        <td rowspan="1"><b>Developer</b></td>
        <td><a href="https://github.com/LuJIAYan">@LuJIAYan</a></td>
    </tr>
        <tr>
        <td rowspan="1"><b>designer</b></td>
        <td><a href="https://github.com/LuJIAYan">@LuJIAYan</a></td>
    </tr>
        <tr>
        <td rowspan="1"><b>QA</b></td>
        <td><a href="https://github.com/LuJIAYan">@LuJIAYan</a></td>
    </tr>
    
</table>

## 评分量规表位置
- [评分量表](#评分量表)


# Product Requirements  
## Introduction：
“毕业通”APP是一个提供给毕业生回忆与联系大学的毕业通讯社交APP。

## Goals：
APP两大特色：回忆与联系。<br>
###### 加强联系：
> 做一个毕业通讯社交APP，记录校园每一届毕业生的毕业照，然后利用人脸识别系统，每个人脸对应ta的个人信息（姓名，联系电话，QQ，微信，专业等），也可以方便毕业之后联系，点击头像可以发起临时会话，加强联系。

###### 社交化回忆，增加用户互动：
> 1. APP还有毕业墙页，相当于毕业生的朋友圈，又区别于微信朋友圈，该APP可以送礼，留言会浮动在页面下方，视觉效果比较不一样；<br>
> 2. 再根据点赞的数据，做数据分析和数据可视化，每周推出数据榜单，如：我的头号粉丝（点赞评论次数最多的人筛选出来）等；<br>
> 3. (远）有能力的话结合虚拟现实技术，发展VR一体机，再现大学毕业场景，让用户声临其境，与过去自己对话（类似哈利波特、头号玩家的情景），回忆过去，反思现在。<br>

# Background&strategic fit：
#### 背景
- 弱关系更有助于我们获取信息。很多人会觉得应该和同行业的人以及同等价值观的人交流，最为没有阻碍，最有效率。强关系提供了纽带，而弱关系则扮演了桥梁的角色。如果能够将强关系的信任和弱关系的新信息组合起来，我们会发现自己很多时候都变得游刃有余。
- 开放式创新组织间知识协同是组织间在知识方面的相互配合与协作，知识资源跨越组织边界的优化配置。该APP可以把不同专业的人汇聚在一起同时提供平台他们联系合作，各施所长，协同发展创新。

#### 策略：
- 运用了机器学习中视觉技术的细粒度图像识别的图像分析——图像主体检测功能，通过即对于输入的一张毕业照图片（可正常解码，且长宽比适宜），识别里面人脸，返回人脸数据id匹配人脸库对应人脸信息，输出该人的个人信息。

# Requirements：
#### 用户痛点
1. 毕业后对应不上同学名字，忘记同学姓名
2. 毕业后想找其他专业同学合作，不知道姓名及联系方式
3. 毕业后同学联系互动少


#### 需求列表

title | User story |  importance |notes |技术
--- | --- |--- |--- |---
遗忘与回忆 | 毕业多年后后看到毕业照对应不上同学的名息|importance |核心功能|百度人脸识别
加强联系合作 | 毕业后联系少互动少|general|APP的毕业墙留言、送礼、临时会话|通讯技术、直播送礼相关技术
趣味性 | 用户粘度不高|general|APP的定时推出最榜单|数据分析与利用

## Assumptions:
1.用户使用通讯录回忆册页面的时候可以佩戴相关的VR产品，让用户身临其境回忆起毕业照的场景。

## user interaction and design
* 产品功能图：
![产品功能图](images/功能结构图.jpg)

* 首页流程图:
![首页流程图](images/首页流程图.jpg)

* [Axure预览网址](https://lujiayan.github.io/API_yuanxing/)

*  原型功能界面总览图
![原型功能界面总览图](images/页面总览.png)

## 调用了face++人脸识别api
[API调用代码档]()
* 导入函数
![](images/导入函数.png)
* 建立人脸库
![](images/建立人脸库.png)
* 添加人脸
![](images/添加人脸.png)
* 人脸搜索
![](images/人脸搜索.png)
* 自定义人脸信息
![](images/自定义人脸信息.png)
* 人脸加矩形框
![](images/加矩形框.png)

## questions（可解决问题）：
1. 调用百度api、旷视api识别人脸
2. 返回人脸姓名等个人信息
3. 不公开隐私信息，有设置按钮，防止恶意骚扰

## not doing（暂时不做）：
 1. 虚拟现实情景
 2. 数据榜单
 

# 评分量表
## PRD1加值宣言
通过调用百度人脸识别API，点击APP毕业照人脸头像，返回人脸姓名等相关信息，方便毕业生查找相关同学的信息，加强沟通协作。

## PRD2核心价值
最小可行性目标是实现一张毕业照（4个同学）识别，返回同学姓名，专业等相关信息。

## PRD3核心价值与用户痛点
- 解决 “毕业后忘记同学名字”、“平时沟通互动少找人帮忙尴尬”和“找同学合作没有联系方式”等毕业社交痛点问题。

## PRD4需求列表与人工智能API加值
- 产品文档中“[需求](#Requirements)”部分有反映使用的API加值，
- 用到的的api有人脸检测、人脸识别、分类、信息匹配，

## 原型
- [产品原型展示和信息设计](https://lujiayan.github.io/API_yuanxing/)，包括交互及界面设计、信息设计、原型文档的所有内容。
- 人工智能的加值部分在原型文档 首页-毕业通讯录

## 使用水平：API之输入及输出
- [百度api调用]()
- [face++ api调用]()

##### API1.使用水平
1.  输入：点击/触摸毕业生头像
2.  输出：毕业生信息（姓名，性别，院系、班级）

#### API2.使用比较分析
对比项 | face++ | 百度API
---|---|---
成熟度 |目前只有文字自定义训练库 | 比较好，有自定义图像训练库，还有训练报告
性价比 | [有提供免费试用、WebAPI接入0.0005-0.01元/次](https://www.faceplusplus.com.cn/v2/pricing/)等 | 	[有提供免费试用、开通续费0.0007元/次](https://console.bce.baidu.com/ai/#/ai/imagerecognition/overview/index)

#### API3.使用后风险报告
* 单人特征识别中的性别识别。人脸识别仅能识别到人脸外貌更偏向女性还是男性，很难对女生男相、男生女相进行正确的判断。--已输出学生的姓名、专业为主。<br>
- 人工智能概率性：由于照片人脸的角度、光线、发型问题，识别人脸会有出错几率。face_recognition是一个基于python的开源的人脸识别库，据说识别准确率达到了99.38%
- [利用百度api物体检测平台](http://ai.baidu.com/easydl/image)尝试训练了一组图像，结果如图。建议：训练图片越多，训练精准度越高，笔者仅测试了7张照片，训练效果欠佳
- ![百度物体检测模型报告](images/训练报告.png)

#### API4.加分项
- 用到的的api有图像检测识别出人脸、自定义图像ID为姓名班级、利用百度开放平台进行自定义图像模型训练



## 清单：
* [百度api定制图像模型训练](http://ai.baidu.com/easydl/app/2/model)
* [face++调用参考](https://blog.csdn.net/qq_37588821/article/details/80633563)
* [百度api调用参考](https://blog.csdn.net/qq_40821981/article/details/81630552)
* [dlib安装](https://www.cnblogs.com/AdaminXie/p/9032224.html)
* [dlib训练连载](https://blog.csdn.net/hongbin_xu/article/details/78347484)
* dlib库、cmake库安装完成、boost库安装未成功
