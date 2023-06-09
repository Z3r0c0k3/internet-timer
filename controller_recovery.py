import os   # 명령어 사용을 위한 os 모듈 import
import time # 대기를 위한 time 모듈 import

def verify_pw():    # 암호 검증 함수
    pw = input("암호를 입력하세요: ")   # 암호를 입력받아 pw 함수에 저장.

    if pw == "test1234":    # pw의 값이 test1234가 맞다면
        print("복구가 승인되었습니다. 시스템을 복구합니다.")    # 복구 승인 문구 출력
        os.system("netsh advfirewall firewall delete rule name=blocked_80 protocol=TCP remoteport=80")  # 80번 포트 차단 해제
        os.system("netsh advfirewall firewall delete rule name=blocked_443 protocol=TCP remoteport=443")    # 443번 포트 차단 해제
        print("복구가 완료되었습니다. 프로그램이 3초 후 종료됩니다.")   # 복구 완료 문구 출력
        time.sleep(3)   # 3초 뒤 자동 종료를 위한 3초 대기
    else:   # 아니라면
        print("복구가 거부되었습니다. 암호를 재입력 해주세요.") # 복구 거부 문구 출력
        time.sleep(1)   # 문구 확인을 위한 1초 대기
        verify_pw() # 재입력을 위한 암호 검증 함수 재호출 (재귀함수)

print("인터넷 사용시간 제어기 복구 프로그램입니다. 반드시 관리자 권한으로 실행해주세요.")   # 시작 문구 출력
verify_pw() # 프로그램 작동을 위한 암호 검증 함수 실행