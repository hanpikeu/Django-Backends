# Django-Backends
장고로 개발한 백엔드 입니다.

## pip install
mysqlclient가 Windows에서는 설치가 되지 않을 수 있습니다.
Windows에서는 이 명령어를 사용해주십시요.
```pip
pip install https://download.lfd.uci.edu/pythonlibs/s2jqpv5t/mysqlclient-1.4.6-cp37-cp37m-win32.whl
```

## How to install server

### Debian 10

#### Install Requires
```bash
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install python3-dev mariadb python-mysqldb git nginx certbot python-certbot-nginx
```

#### Clone repository
```bash
sudo git clone https://github.com/China-Gate/Django-Backends.git
cd Django-Backends
```

#### Create Virtual Environment
```bash
python3 -m pip install pip --upgrade
python3 -m pip install virtualenv
python3 -m virtualenv '.venv'
source .venv/bin/activate
python3 -m pip install -r requirements.txt
```

#### Setup NginX And Certificate

```bash
sudo certbot --nginx
```
Setup Config of Nginx 
Use server-setting/nginx.conf.template
```bash
sudo systemctl restart nginx
```


#### Setup Database
```bash
sudo mysql_secure_installation
sudo mysql
```
```mysql
CREATE DATABASE {database_name};
CREATE USER '{user_name}'@'localhost' IDENTIFIED BY '{pass_word}';
GRANT USAGE ON {database_name}.* TO '{user_name}'@'localhost';
GRANT INSERT, SELECT, UPDATE, DELETE ON {database_name}.* TO '{user_name}'@'localhost';
```

#### Setup .env
Use server-setting/.env.template

#### Setup Django-Backends
```bash
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py runserver
```
