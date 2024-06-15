
=======
# Front Description
Gachon university AI&amp;software department 2023 graduation project _ Bard prompt engineering
<img width="730" alt="스크린샷 2023-12-09 오전 1 43 33" src="https://github.com/baeksh0330/2023graduationProject_BardpromptEngineering/assets/94830364/e7101880-c63e-473b-940e-f0199a774185"></br>
<img width="731" alt="스크린샷 2023-12-09 오전 1 44 21" src="https://github.com/baeksh0330/2023graduationProject_BardpromptEngineering/assets/94830364/2a197b8c-94d3-4617-a6b5-ea919951aa5a"></br>
<img width="599" alt="스크린샷 2023-12-09 오전 1 44 33" src="https://github.com/baeksh0330/2023graduationProject_BardpromptEngineering/assets/94830364/1219767b-8aec-4412-b811-d7e11ff71c35"></br>
<img width="543" alt="스크린샷 2023-12-09 오전 1 44 41" src="https://github.com/baeksh0330/2023graduationProject_BardpromptEngineering/assets/94830364/759a2711-a481-4fa0-bf5d-c8b44ad65040"></br></br>



1. 맨 위의 텍스트 박스 : 원하는 질문 입력
2. 밑의 전송 버튼 : 클릭 시 내가 입력한 질문을 바드에게 질문 --> 굳이 버튼 안누르고 엔터 키 눌러도 같은 기능 실행 가능

*** 입력한 문자열이 담긴 변수 : user_input </br>
--> user_input을 query_optimizer(user_input) 함수로 보냄 --> optimize한 query 반환 (= optimized_query) </br></br>

*** optimize한 query가 담긴 변수 : optimized_query </br>
--> generate_response(optimized_query) 로 최적화한 쿼리 보냄 --> 그에 따른 bard의 답변 반환 (=response) </br></br>

*** 바드에게 답변 받은 문자열이 담긴 변수 : response </br>
--> response를 prompt_optimizer(response) 함수로 보냄 --> responxe optimize 해서 반환 (= 최종결과) </br></br>

- 각 함수에 query, prompt enginnering을 수행하는 코드를 추가하기. </br>
- 각자 본인 bard Token 이용하여 yourToken 부분 수정 필요. </br>
- 실행 후 터미널에 streamlit run app.py 입력.</br>
