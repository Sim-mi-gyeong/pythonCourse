# DB 연결

1. 시크릿 변수 설정 - mongoDB 주소, NABER API Secret key

2. odmantic 을 사용하여 fastapi 와 연결
 - ODM(Object Document Mapper) : Object와 Document를 연결 -> DB에 직접 접근하는 것이 아닌 중개자로서 연결하는 역할
 - Python이 DB에 접근하기 편리하도록 ODM 존재

3. models 디렉토리를 사용하여 추상화

4. book 모델 개발

5. db에 insert