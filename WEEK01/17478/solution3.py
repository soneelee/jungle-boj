def chatbot(n, cnt):
    if cnt == 0: 
        print("____"*(n) + "\"재귀함수가 뭔가요?\"")
        print("____"*(n) + "\"재귀함수는 자기 자신을 호출하는 함수라네\"")
        print("____"*(n) + "라고 답변하였지.")
        return 

# 반복되는 부분
    print("____"*(n - cnt) + "\"재귀함수가 뭔가요?\"")
    print("____"*(n - cnt) + "\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.")
    print("____"*(n - cnt) + "마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.")
    print("____"*(n - cnt) + "그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\"")

    # 구조 안에 구조
    chatbot(n, cnt-1)

     # 종료 이후 실행
    print("____"*(n - cnt) + "라고 답변하였지.") 

    # 종료 지점
    
    

n = cnt = int(input())
chatbot(n,cnt)

# n : 반복 횟수