import re
import itertools as IT
import time
import argparse
import sys

def arg_parse():
    parser = argparse.ArgumentParser(description='ant sequencer')
    parser.add_argument("-n", "--number", type=int, required=True, help='calculate to \'n\'th sequence' ) 
    args = parser.parse_args()
    return args

def re_sub(_s):

    # "그룹 \d와 같은것들을 찾아서, 람다함수로 리플레이스"
    # 길이가 1인 경우가 있어서 +는 사용x.
    # group() = group(0) 매치된 전체 문자열
    # match 객체의 regs 멤버는 순서대로 그룹 위치에 대한 정보를 갖고있는 튜플 리스트, 0번은 매치된 전제 문자열 인덱싱
    # sub는 재귀적으로 동작
    s = re.sub(r'(\d)(\1*)', lambda x: str(len(x.group(0)))+x.group(1), _s)
    return s


def groupby(_s):
    for key, group in IT.groupby(_s):
        s = str(len(''.join(group)))+key
    
    return s

def re_findall(_s):
    ras1 = re.compile(r'(\d)(\1*)')
    #ras2 = re.compile(r'((\d)\2*)')

    res1 = ras1.findall(_s)
    # res2 = ras2.findall(_s)

    # findall은 tuple list 반환
    s1 = "".join([str(len(i+j))+i for i, j in ras1.findall(_s) ])
    # s2 = "".join([str(len(i))+j for i, j in ras2.findall(_s) ])

    return s1


def run(_num):
    s = "1"
    start = time.time()
    for i in range(_num):
        s = re_findall(s)
    end = time.time()
    print(f'{(end-start): .2f} ms')

    s = "1"
    start = time.time()
    for i in range(_num):
        s = re_sub(s)
    end = time.time()
    print(f'{int(end-start): .2f} ms')


if __name__=="__main__":

    args = arg_parse()
    if args.number < 3:
        print("enter a value equal or grater than 3")
        sys.exit()

    run(args.number)