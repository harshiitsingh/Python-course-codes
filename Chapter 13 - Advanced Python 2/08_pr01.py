'''
virtualenv env1
virtualenv env2
.\env1\Scripts\activate.ps1   # if want something new kill the old terminal and open new
pip install pandas flask numpy matplotlib   # packages dependencies also come with installation
pip freeze
pip freeze > .\requirements.txt
deactivate

.\env2\Scripts\activate.ps1
pip install -r .\requirements.txt
deactivate
'''