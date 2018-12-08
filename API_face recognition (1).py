#!/usr/bin/env python
# coding: utf-8

# In[5]:


KEY = 'tbdIripRr96cUlAGKFHtFroB'  # Replace with a valid Subscription Key here.

# 沿用API的示范代码，{subscription key}用KEY代入
headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': 'tbdIripRr96cUlAGKFHtFroB'.format(subscription_key = KEY),
}
headers


# In[1]:


from aip import AipFace

""" 你的 APPID AK SK """
APP_ID = '14131125'
API_KEY = 'tbdIripRr96cUlAGKFHtFroB'
SECRET_KEY = 'Znc0y2Yh4SpMXuBL7I5AdTzuiXcWcdNh'

client = AipFace(APP_ID, API_KEY, SECRET_KEY)


# In[2]:


#from 模块名 import 函数名
from aip import AipFace


# In[5]:


#选择了URL类型，base64看不懂。暂时用一张图片链接测试（图片的base64编码指将一副图片数据编码成一串字符串，使用该字符串代替图像地址。）
image = "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1544208974338&di=2e86f9cd0e74b20e7a018d50e69d509f&imgtype=0&src=http%3A%2F%2Fs4.sinaimg.cn%2Forignal%2F492dc5e9bdaf7ac9bab73"
imageType = "URL"

#client.detect()这个函数即为面部检测函数，内部可填入三个参数，image,imageType,options。
""" 调用人脸检测 """
client.detect(image, imageType);


""" 如果有可选参数 """
options = {}
options["face_field"] = "race,age,gender"
options["max_face_num"] = 4
options["face_type"] = "LIVE"

""" 带参数调用人脸检测 """
client.detect(image, imageType, options)


# In[6]:


result = client.detect(image, imageType, options)
print(result)


# In[15]:


#然后测试base64类型的人脸检测
import base64
filePath ="biyezhao.jpg"
with open(filePath,"rb") as f:  
# b64encode是编码，这里改了一下将二进制格式转化为BASE64格式 要注意不然要报错（_io.BufferedReader object错误）的 ；还有记得把照片和py档放一起
    base64_data = base64.b64encode(f.read())
image = str(base64_data,'utf-8')


# In[17]:


#参考https://blog.csdn.net/qq_40821981/article/details/81665322
from aip import AipFace
import base64
""" 你的 APPID AK SK """
from aip import AipFace

""" 你的 APPID AK SK """
APP_ID = '14131125'
API_KEY = 'tbdIripRr96cUlAGKFHtFroB'
SECRET_KEY = 'Znc0y2Yh4SpMXuBL7I5AdTzuiXcWcdNh'

client = AipFace(APP_ID, API_KEY, SECRET_KEY)


client = AipFace(APP_ID, API_KEY, SECRET_KEY)

filePath ="biyezhao.jpg"
with open(filePath,"rb") as f:  
# b64encode是编码
    base64_data = base64.b64encode(f.read())
image = str(base64_data,'utf-8')
imageType = "BASE64"

#参数设置
options = {}
options["face_field"] = "age,beauty"
options["max_face_num"] = 4
options["face_type"] = "LIVE"

""" 调用人脸检测 """
result = client.detect(image, imageType,options);
print(result)


# In[29]:


#测试建一个人脸库 有点复杂 摸索中..
from aip import AipFace
import base64
""" 你的 APPID AK SK """
APP_ID = '14131125'
API_KEY = 'tbdIripRr96cUlAGKFHtFroB'
SECRET_KEY = 'Znc0y2Yh4SpMXuBL7I5AdTzuiXcWcdNh'

client = AipFace(APP_ID, API_KEY, SECRET_KEY)

#W文件路径记得反斜杠
filePath = r"D:\API_qimo\图像识别"

with open(filePath,"rb") as f:  
# b64encode是编码
	base64_data = base64.b64encode(f.read())
image = str(base64_data,'utf-8')
imageType = "BASE64"

groupIdList = "test"

""" 调用人脸搜索 """
a = client.search(image, imageType, groupIdList);

print(a)


# In[ ]:




