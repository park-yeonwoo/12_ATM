
#잔액 초기화
balance = 1000

#사용자 입력값
while True: #조건이 true이면 무한 작동함
    num =input('사용하실 기능을 선택해주세요.(1.입금, 2.출금, 3.영수증보기, 4.종료): ')
#4를 입력하면 종료라는 출력메세지 print()를 보여주는 코드를 작성해주세요
#개발할 때는 최소한의 자원만 쓸 수 있도록 고려를 해보는 게 좋음

    #2번 출금 기능 코드
    if num == '2':
        withdraw_amount = int(input('출금할 금액을 입력해주세요 : '))
        """
        if balance >= withdraw_amount 
            print(f'출금할 금액은 {withdraw_amount}이며, 잔액은 {balance} 입니다.')
        else: balance -= withdraw_amount
            print("잔액이 부족합니다. 잔액을 확인 후 시도해주시기 바랍니다."
    
        """
        withdraw_amount = min(balance, withdraw_amount) #min을 이용해 잔액보다 작을 시 출금이 안 되게 할 수 있음
        balance -= withdraw_amount
        print(f"출금하신 금액은 {withdraw_amount}이고, 현재 잔액은 {balance}원 입니다.")

    #1번 입금 기능 코드
    if num == '1':
        #얼마 입금할래?
        deposit_amount = int(input('입금할 금액을 입금해주세요 : '))
        #balance 
        #balance = balance += deposit_amount #결과를 보여달라고 하는 명령어가 없어 날아감
        balance += deposit_amount
    print(f"입금하신 금액은 {deposit_amount}'원이고, 현재 잔액은 {balance}원 입니다.") 



    #4번 종료 기능 코드
    if num == '4':
        print('이용해 주셔서 감사합니다.')
        break

