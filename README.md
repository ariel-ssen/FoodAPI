# 실행 
## Mac환경 
1. Brew 설치
   - homebrew site 내에서 복사.
3. Pyenv 설치
   - brew install pyev
4. python 설치
   - pyev install 3.12.1
5. 해당 디렉토리 접근
   - cd ****
6. 가상환경 접근
   - source myenv/bin/activate
7. 환경설정
   - pip3 install django
   - pip3 install djangorestframework
   - pip3 install drf_yasg
8. 실행
   - python3 manage.py rumserver
9. api 접근
   - http://127.0.0.1:8000/api/products/

![Uploading 스크린샷 2024-01-23 오후 3.08.54.png…]()



# API 만들기 
#### select 조회 기능만 사용

### 1. xlsx파일 -> csv파일 변경 
    why?
    csv는 단순 텍스트 형식으로 저장되기에 모든 서식은 제거되고 그값만 문서에 저장되서 필요로 하는 데이터만 사용하려고 의도
    
### 2. csv 필요한 정보만 가공 
    Columns?
    "id, food_cd, group_name, food_name,research_year, maker_name, ref_name,serving_size, calorie, carbohydrate,
    protein, province, sugars, salt, cholesterol,saturated_fatty_acids, trans_fat"
    필요한 정보만 가지고 진행

### 3. columns 순서에 맞추어 DB에 삽입
    Field?
    CharFidld 사용은 이름, 제목, 설명, 제품 코드 등 짧은 길이의 텍스트 데이터를 저장하는데 사용하기 적합하다고 생각되어 진행

### 4. RESTful API 디자인 

1. URL 구조 설계, 시리얼라이저 사용, 뷰셋과 라우터 활용
    - 계층적 구조를 사용하여 자원을 그룹화하고 관련성을 유지
    - 데이터 직렬화
    - 일관성 있고 간단한 코드를 유지

2. 버전 정보 전달 
    - v1

3. api 문서화 , filter 기능 추가 
    - drf_yasg 라이브러리 사용 
    - pip install django-filter -> SearchFilter의 search_fields
        -  텍스트 기반의 검색어를 처리. 부분 일치나 정확한 일치 검색에 유용하기에 사용.

4. Pagination 적용
    - 1page = 10 list 

#### urls explanation
- admin/ : 관리자 page
- api/products/ : db에 저장된 정보를 조회할수 있으며 검색 가능
- v1 : version 확인 
- swagger : api 문서 

#### file explanation
- tocsv.py : csv파일을 db에 저장
- Food_clean.csv : 필요한 컬럼만 가공한 파일 , 즉각 활용
- djangoProject : main -> product : serve
###### 웹개발에서 RESTAPI는 클라이언트(front)와 서버(Back)의 통신을 원활하게 하는 역할을 합니다. 
###### 개선사항 :  인증과 권한관리 , 예외처리와 오류 핸들링 , 단위 테스트와 통합테스트, 캐싱 , 백그라운드작업, 보안, 성능 최적화
