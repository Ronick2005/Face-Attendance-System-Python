import os
path = os.path.dirname(os.path.abspath(__file__)) + '\\..\\'
os.system('pip3 install virtualenv')
os.system('python3 -m venv ' + path + 'env')
os.system(path + '.\env\Scripts\activate.bat')
os.system('python -m pip install --upgrade pip')
os.system('pip install -r requirements.txt')
os.system('python ' + path + '.\FaceAttendance(script).py')
os.system('deactivate')
os.system('rmdir /s /q ' + path + '.\env')
exit()