# Python blog using self-made framework

## Local setup (Windows)
1. Install virtualenv
```
pip install virtualenv
```
2. Navigate to project root
3. Create virtualenv
```
virtualenv env
```
4. Activate virtualenv and install dependencies
```
env\Scripts\activate.bat
pip install -r requirements.txt
```
5. Run app
```
python app.py
```
6. Visit http://127.0.0.1:8081 in browser

## Version log
##### 0.0.1
Simplest 'Hello world'.
No dependencies, no auto-reload (re-run app manually to see changes).

##### 0.0.2
++ Parse GET params

##### 0.0.3
++ use werkzeug dev server