# 关于 Auto filler
1.使用之前老板要求绑定的google calendar进行排课的话，auto filler就能快速地获取所有的信息并且将其填入工资表。

# 关于Google calendar里排课的格式要求
1. event title要写课的名字。
2. event description里要写上学生的名字，多个学生用逗号隔开。
3. event的时间段要设置好，因为工资的计算要用到课时，这个应该很常识。

# 第一次使用
1. 双击main.exe
2. 出现user interface之后，将自己的个人信息输入到框中，输入完毕后按update user info
3. 将客服小姐姐给的《优佳教育老师工资发放表-x月.xlsx》文档放在main.exe的同一文件夹下。
4. 按下Fill Excel Sheet按钮。
5. 网页会自动弹出请求使用你的google calendar，选择你的google账号并接受即可。

# 之后的使用
1. 每次将客户小姐姐发的《优佳教育老师工资发放表-x月.xlsx》文档放在main.exe的同一文件夹下后，打开main.exe并点击
Fill Excel Sheet即可。
2. 个人的资料将会储存在user_info.json这个文件里面，请不要删除。删了的话又要再填一次了。
3. 想要更新个人的资料，只需打开main.exe，改掉对应的输入栏内的文字，再按update user info即可。


# Folder Structure
## ENV
virtual environment

## ui
Design of the panel. 
* PyQt5 designer is located at ENV/Lib/site-packages/pyqt5_tools/designer.exe
* To convert .ui file to .py file, use the following command
~~~
python -m PyQt5.uic.pyuic -x ui/main.ui -o main.py
~~~

## dist.rar
The standalone exe is in this dist.rar, just give to the user, they can use it.

## Others
* credentials.json
This is for the use of google calendar api.
* token.pickle
After accepted the use of google calendar api, a token(like a pass) will be generated.
* main.py
A user interface. Using command pycui ui/main.ui -o main.py to generate script from a ui file.
* fill_course_hours.py
All calculations and operations happen here.
* user_info.json
A file used to store the information of the user.
* main.spec
A by product when using pyinstaller. To make the program to a standalone exe, use the following command:
~~~
pyinstaller -F main.py
~~~
-F is to compress all dlls and stuff into the exe, so it's much cleaner.

