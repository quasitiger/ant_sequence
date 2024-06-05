import argparse
import sys

def arg_parse():
    parser = argparse.ArgumentParser(description='ant sequencer')
    parser.add_argument("-n", "--number", type=int, required=True, help='calculate to \'n\'th sequence' ) 
    args = parser.parse_args()
    return args


def run(_number):

    print(f'calculate to {_number}')
    # 개미 수열이 저장될 문자열 변수
    init_sec = "11"
    
    # 인덱스는 0부터 시작이지만, 입력값은 1부터 시작하므로 보정, 시작 배열을 1,1로 잡아서 
    for j in range(0,_number-2):
        
        after_sec = ""
        # 첫 값을
        s1 = init_sec[0]
        count = 1

        for i in range(1,len(init_sec)):
            s2 = init_sec[i]

            if s1 == s2:
                count+=1
            elif s1 != s2:
                after_sec+=str(count)
                after_sec+=str(s1)

                s1 = s2
                count=1

        after_sec+=str(count)
        after_sec+=str(s1)

        init_sec = after_sec
                
    # 출력
    print(f"{_number}th sequence is {after_sec}")
    median_value = int(len(after_sec)/2)-1
    print(f"and median value is { after_sec[ median_value:median_value+2]}")


if __name__ == "__main__":
    args = arg_parse()
    if args.number < 3:
        print("enter a value equal or grater than 3")
        sys.exit()
    
    run(args.number)