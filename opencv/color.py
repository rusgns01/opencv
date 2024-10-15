import cv2
import numpy as np

def onChange(x):
    pass

def brightnessTrackbar():
    # 이미지 로드
    img = cv2.imread('./img/kakao.jpg')

    if img is None:
        print("이미지를 불러올 수 없습니다. 경로를 확인하세요.")
        return

    # 이미지 크기 조정, INTER_LINEAR 보간법을 사용해 이미지를 부드럽게 확대
    img_resized = cv2.resize(img, (1299, 600), interpolation=cv2.INTER_LINEAR)

    # WINDOW_NORMAL 창 크기 조절, 밝기 조절 범위: -100 ~ 100
    cv2.namedWindow('bright', cv2.WINDOW_NORMAL)
    # 트랙바 이름, 트랙바 생성 창 이름, 초기, 최대, 트랙바 위치 변경 시 콜백함수
    cv2.createTrackbar('level', 'bright', 100, 200, onChange)

    while True:
        # 매 프레임마다 키 입력 확인, 키 값의 마지막 8비트만 추출
        # cv2.waitKey()는 32비트 정수로 키 값을 반환, OpenCV에서 주로 사용하는 건 마지막 8비트 부분이기 때문에
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break

        # 트랙바 값 가져오기 (기본값 100에서 -100~100으로 변환)
        bright_value = cv2.getTrackbarPos('level', 'bright') - 100

        # alpha = 1보다 크면 대비가 증가하고, 1보다 작으면 대비가 감소
        # 픽셀 값에 더해져 이미지의 밝기를 조절
        adjusted = cv2.convertScaleAbs(img_resized, alpha=1, beta=bright_value)

        # 조절된 이미지 표시
        cv2.imshow('bright', adjusted)

    # 모든 창 닫기
    cv2.destroyAllWindows()

brightnessTrackbar()
