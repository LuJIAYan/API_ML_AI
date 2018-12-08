#  毕业通讯社交APP产品PRD

### 1.产品需求（Product Requirements）：
Target release | 2018年12月3日
---|---
owner | Sophialuu
designer | Sophialuu
Document Status|2.0
Developer| Sophialuu
QA| Sophialuu

### 2.目标（Goals）：

总目标：做一个毕业通讯社交APP，记录校园每一届毕业生的毕业照，然后利用人脸识别系统，每个人脸对应他的个人信息（姓名，联系电话，QQ，微信，专业等），也可以方便毕业之后联系。
 

### 3.背景和策略（Background&strategic fit）：
- 应用背景
1. 人脸自动识别系统作为一种重要的个人身份鉴别方法，最早用于罪犯照片管理和刑侦破案，现在这种技术在安全系统和商贸系统中都有很多的应用。
2. 静态人脸识别是在特定的区域或者范围之内，进行识别，也就是说识别对角度、距离、位置的要求会比较高。静态人脸识别的特点就在于用户容量小，比较适合一些小型公司的考勤之类的使用。
3.https://blog.csdn.net/qq_40821981/article/details/84670058 百度API人脸库应用
4. https://blog.csdn.net/weixin_41803874/article/details/81201393  百度AI人脸检测实现性别、人种肤色、年龄检测python
5. https://ai.baidu.com/docs#/Face-Detect-V3/top 人脸检测与属性分析

-  需求 
1. 灵感来源于小时候填的同学回忆录，但是纸质的可能只会不 会经常打开，APP可以随时打开。
2.  建立并维系强大的社交网，在毕业后有需要还能联系。人们常说大学就是社会的缩影，这个APP可以方便日后有需要的话，可以利用大学的人力资源。
3. 结合虚拟现实技术，可以回忆大学的生活，看到从前的自己。

- 策略：
利用静态人脸识别技术，制作一款毕业通讯社交APP，促进毕业生联系与大学生活。

### 4.需求（Requirements）：

title | User story |importance |notes |
--- |--- |--- |--- |
痛点1 | 毕业多年后后看到毕业照对应不上同学的名字|   importance |APP的总目标。APP可以点击毕业照头像对应上同学信息|
痛点2 | 填写纸质通讯录容易丢，不能实时更新信息|  general |APP可以随时随地打开查看。个人信息页面可以编辑信息，实时更新个人信息|
痛点3 | 毕业后有需要找老师、同学帮忙不知道找谁| general |APP可以加强联系，有记录信息数据的分析收集是个大工程|
痛点4 | 毕业后联系少| general |APP可以加强互动，毕业墙留言、送礼社交性加强，可是功能实现需要强大的技术支持|
痛点5 | APP没人支持，毕业生缺乏可靠招聘信息|general|  与可靠的招聘网站/企业合作，拉赞助|

### 5.假设（Assumptions）:
1.用户使用通讯录回忆册页面的时候可以佩戴相关的VR产品，让用户身临其境回忆起毕业照的场景。

### 6.用户交互和设计（user interaction and design）

Axure预览网址/图片
 https://lujiayan.github.io/API_yuanxing/
- 平静技术互动原则
1.  输入：点击/触摸毕业生头像
2.  输出：毕业生信息（姓名，性别，院系、班级）、VR模拟毕业照现场。

(images/首页流程图 .jpg)
1. 产品功能图：
(images/产品路线图.jpg)

2. 业务流程图：
(images/产品路线图.jpg)


3.. API调用代码档
 https://github.com/LuJIAYan/API_ML_AI/blob/master/API_face%20recognition%20(1).ipynb
 
### 7.问题（questions）：

 1. 角度、光线、发型、脸型相似等干扰分类。
 2. API的调用
 3. 最小目标，实现毕业照人脸识别信息
 4. 人脸识别+VR环境部署？

### 8.不能做（not doing）：

 1. 有些人不想公开自己的毕业照
 2. 有些人不想公开隐私信息
 3. 担心聊天恶意骚扰，因此有临时会话框，可以不用加微信也能聊天。
 4. 单人特征识别中的性别识别。人脸识别仅能识别到人脸外貌更偏向女性还是男性，很难对女生男相、男生女相进行正确的判断。--不检测男女










