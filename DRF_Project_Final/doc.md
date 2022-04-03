# DB 연결

1. 시크릿 변수 설정 - mongoDB 주소, NABER API Secret key

2. odmantic 을 사용하여 fastapi 와 연결
 - ODM(Object Document Mapper) : Object와 Document를 연결 -> DB에 직접 접근하는 것이 아닌 중개자로서 연결하는 역할
 - Python이 DB에 접근하기 편리하도록 ODM 존재

3. models 디렉토리를 사용하여 추상화

4. book 모델 개발

5. db에 insert


## github 에 코드 올리기
- 토큰 발급
- 토큰 복사 : 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

## VPS : 가상 사설 서버 구축

- AWS Lightsail 사용
- 인스턴스 생성
- ssh 를 사용하여 연결 (브라우저에서 접속)
- sudo apt-get update
- sudo apt-get -y upgrade
- sudo apt-get install build-essential
- sudo apt-get install curl git vim python python3-pip
- touch .gitconfig
- git config --global user.name Sim-mi-gyeong
- git config --global user.email smegyeong@gmail.com
- git config --global --list
- git clone <프로젝트>
- cd <프로젝트>
- vi secrets.json
- sudo pip install -r requirements.txt
- sudo python3 server.py
- ip 접속
- 배포 성공!!