# 도넛크롤러의 이전 버전입니다. 

### 몰트 위스키(mod_wsgi) 를 이용한 장고서버 셋팅 -> 가장 손쉬운 셋팅방법

```
...
0. 가상환경 생성 및 필요모듈 설치하기 
1. sudo pip install mod_wsgi-httpd 
2. sudo pip install mod_wsgi 
3. pip freeze 로 전역환경에 설치되었음을 확인하기 
4. settings.py에 INSTALLED_APPS 설정에 'mod_wsgi.server' 추가하기
5. 정적(static)파일 생성하기 
-> python manage.py collectstatic
5. manage.py 파일이 위치한 곳에서 mod_wsgi 실행하기 
-> python manage.py runmodwsgi --setup-only --user sylee --group sylee --server-root=/tmp/mod_wsgi-localhost:8000:1012
6. 아파치 실행 또는 재실행하기 
-> /tmp/mod_wsgi-localhost:8000:1012/apachectl start(restart)

* 아파치 설정파일 변경 : /tmp/mod_wsgi-localhost:8000:1012/httpd.conf
...
```

### 서버셋팅시 참고 사이트 

* https://github.com/GrahamDumpleton/mod_wsgi
* http://ggilrong.tistory.com/entry/Django-Apache-%EC%89%AC%EC%9A%B4-%EC%97%B0%EB%8F%99%EB%B0%A9%EB%B2%95-How-to-use-Django-with-Apache-and-modwsgi
* http://stackoverflow.com/questions/24760872/how-can-run-django-on-centos-using-wsgi

### 에러처리 

```
/tmp/mod_wsgi-localhost:8000:1012/error_log
crontab error 발생시 /var/spool/mail/sylee 에 로그가 찍힌다. (sylee 파일은 다른 이름으로 변경가능)
static files 깨지면 mod_wsgi 리로드 
```


### 서비스 사용법
```
* FORM 의미
....................................................................................................................................................
- 생성 : db에 존재하지 않는 연관검색어를 설정한 기간만큼 크롤링
- 조회 : 복수개의 연관검색어 크롤링 결과를 조회하여 시각적으로 디스플레이함 (검색어가 정확하지 않거나 db에 존재하지 않는 경우 없다고 알려준다.)
- csv : 크롤링 결과를 설정한 기간만큼 csv 파일로 내려받음
- 삭제 : 크롤링 결과를 설정한 기간만큼 제거함
- JSON : 크롤링 결과를 설정한 기간만큼 json 포맷으로 디스플레이함
- 업데이트 : db에 존재하는 연관검색어에서 설정한 기간만큼 추가로 크롤링 (기간을 설정하지 않고 category only, donut only 체크시 도넛이름이나 카테고리만 새로 업데이트한다.)
..................................................................................................................................................... 

* 파일형식 
.......................
인코딩 : EUC-KR
확장자 : CSV
.......................
column[0] : 카테고리 
column[1] : 도넛이름
column[2] : 연관검색어  
.......................


* 하루치 데이터 생성
...........................
시작날짜 : 데이터 얻을려는 날짜
끝날짜 : 시작날짜와 같음 
...........................


* 날짜를 입력하지 않는 경우 
...........................
시작날짜 : 디폴트 값
끝날짜 : 오늘 날짜 
...........................
```


### 몰트 위스키 서버 환경설정 
```
* timeout, process, thread, buffer size 
* multiprocess인 경우
* multiprocess가 아닌 경우
```
