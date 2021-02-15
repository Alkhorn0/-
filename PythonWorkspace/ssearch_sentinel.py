# 선형검색 공부
# 선형 검색 알고리즘을 보초법으로 수정
from typing import Any, Sequence
import copy

def seq_search(seq: Sequence, key: Any) -> int:
    """ 시퀀스 a에서 key와 값이 같은 원소를 선형 검색(보초법)"""
    a = copy.deepcopy(seq)  # seq를 복사 
    a.append(key)

    i = 0
    while True:
        if a[i] == key:
            break      # 검색에 성공하면 while문을 종료
        i += 1
    return -1 if i == len(seq) else i       # i값이 len(seq)와 같으면 찾은것은 보초이므로 검색에 실패 -> -1 반환 / 그렇지 않으면 i 반환

if __name__ == '__main__':
    num = int(input("원소 수를 입력하세요.: "))     # num값을 입력받음
    x = [None] * num                              # 원소 수가 num인 배열을 생성

    for i in range(num):
        x[i] = int(input(f"x[{i}]: "))
    
    ky = int(input('검색할 값을 입력하세요.: '))    # 검색할 키 ky를 입력받음

    idx = seq_search(x,ky)                        # ky와 값이 같은 원소를 x에서 검색

    if idx == -1:
        print('검색값을 갖는 원소가 존재하지 않습니다.')
    else:
        print(f'검색값은 x[{idx}]에 있습니다.')