import time # 경과 시간과 남은 시간, 대기 등을 위한 time 모듈 import
import os   # 명령어 사용을 위한 os 모듈 import
 
def t_calc(sec):    # 핵심 연산에 필요한 t_calc 함수. 함수 호출시 날라온 값을 매개변수 sec에 값을 받음.
    s_t = time.time()   # 시간 간격 측정을 위한 시작점인 변수 s_t 선언 (start_time)
    e_t = s_t + sec # 시간 간격 측정을 위한 끝점인 변수 e_t 선언 (end_time)

    while time.time() < e_t:    # 현재 시간이 e_t의 값보다 작아질 때 까지 반복 실행
        p_t = time.time() - s_t # 경과 시간 측정 값 변수 p_t 선언 (past_time)
        r_t = e_t - time.time() # 남은 시간 계산 값 변수 r_t 선언 (remain_time)

        print(f"경과 시간: {f_t(p_t)} / 남은 시간: {f_t(r_t)}", end = "\r") # 경과 시간과 남은 시간을 보기 편하게 포맷팅하여 출력. 출력 기록이 안남고, 값 실시간 업데이트.
        time.sleep(1)   # 출력 값 확인을 위한 1초 대기
    
    print("사용시간이 종료되었습니다. 3초 뒤 프로그램이 종료됩니다.")   # 반복 실행 나오면 사용시간 종료 문구 출력
    os.system("netsh advfirewall firewall add rule name=blocked_80 dir=out action=block protocol=TCP remoteport=80")    # 80번 http 포트 차단
    os.system("netsh advfirewall firewall add rule name=blocked_443 dir=out action=block protocol=TCP remoteport=443")  # 443번 https 포트 차단
    time.sleep(3)   # 3초 뒤 프로그램 종료를 위해 3초 대기

def f_t(sec):   # 위 경과 시간, 남은 시간 포맷팅 함수. 함수 호출시 날라온 값을 매개변수 sec에 값을 받음.
     m, s = divmod(sec, 60) # sec 값을 나눠 s(초)를 m(분)으로 변환
     h, m = divmod(m, 60)   # m 값을 나눠 m(분)를 h(시간)으로 변환
     return "{:02d}:{:02d}:{:02d}".format(int(h), int(m), int(s))   # 위 변환 값을 h:m:s 형식으로 반환

def input_t_c(input_sec):   # 제한 시간 입력 값 시:분:초 형식 포맷팅 함수
    h, m, s = map(int, input_sec.split(":"))    # 입력값을 :를 기준으로 int로 쪼개 변수 h,m,s로 저장
    sec = h * 3600 + m * 60 + s # h,m,s로 나눠진 값을 초로 다 더해서 변수 sec에 저장
    t_calc(sec) # sec 값을 t_calc 함수로 보내며 호출
    
def verify_t(): # 입력 값 검증 함수.
    print("인터넷 사용시간 제어기 (windows)")   # 시작 문구 출력
    sec = input("사용 제한 시간을 입력하세요 (시:분:초): ") # 시:분:초 형식으로 시간을 입력받아 변수 sec에 저장
    if not sec: # sec에 값이 안 들어있다면,
        print("값이 잘못되었습니다. 다시 입력하세요.")  # 재입력 문구 출력
        time.sleep(1)   # 문구 확인을 위한 1초 대기
        verify_t()  # 재입력을 위한 입력 값 검증 함수 재호출 (재귀함수)
    else:   # 값이 들어 있다면,
        input_t_c(sec)  # sec 값을 input_t_c 함수를 보내며 호출

verify_t()  # 프로그램 작동을 위한 입력 값 검증 함수 호출