#  Python and Flask Bootcamp: Create Websites using Flask!

`conda create -n myenv numpy`: This command creates a virtual environment called "myenv" and installs the NumPy library, a Python library for number crunching.

`conda create --name myenv python=3.11`: This command creates a virtual environment called "myenv" and specifies that the environment uses Python version 3.11. This command not only creates a blank virtual environment, but also installs the specified version of Python.

`conda create -n myflaskenv flask`: This command creates a virtual environment called "myflaskenv" and installs the Flask library, a Python micro-framework for building web applications.

`conda create -n myenv numpy` is a conda command used to create a virtual environment called "myenv" in Anaconda and to install the NumPy library.

`conda create`: This is part of the conda command and is used to create a virtual environment.
-n myenv: This is an option that specifies the name of the virtual environment to be created as "myenv". You can change the name of "myenv" to something else if you wish.
`numpy`: This is the name of the package to be installed in the virtual environment, in this case the NumPy library, a Python library for scientific computing and mathematical operations.

To list out all the environment
`conda env list`

 


This was useful to me when I encountered a similar error in Windows:

To install the virtual environment:

pip install virtualenv
To create a virtual environment: pip install

virtualenv flask
To navigate to the script and activate virtualenv: virtualenv flask

activate
To install the flask: python -m

python -m pip install flask
Check if flask is installed: python -m pip

python -m pip list




=========·=========

users/form.py：該文件定義了使用 Flask-WTF 和 WTForms 構建的表單類，用於用戶註冊、登入和更新帳戶信息。它包含了 RegistrationForm、LoginForm 和 UpdateUserForm 這些表單類，用於定義不同的表單字段、驗證器和自定義驗證方法。

users/views.py：該文件定義了 Flask 應用中與用戶相關的路由和視圖函數。它包含了用戶註冊、登入、登出和更新帳戶信息等功能的實現。在這些視圖函數中，它引用了 form.py 中定義的表單類來處理用戶提交的表單數據。

users/picture_handler.py：該文件定義了處理用戶頭像圖片的函數。它包含了一個名為 add_profile_pic 的函數，該函數用於將上傳的用戶頭像圖片進行處理、保存並返回保存的文件名。該函數使用 Pillow 库來調整圖片的大小並保存。

