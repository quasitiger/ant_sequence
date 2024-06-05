import argparse
import sys

def arg_parse():
    parser = argparse.ArgumentParser(description='ant sequencer')
    parser.add_argument("-n", "--number", type=int, required=True, help='calculate to \'n\'th sequence' ) 
    args = parser.parse_args()
    return args


def run(_number):

    print(f'calculate to {_number}')
    # 처음 배열
    init_queue = [1,1]
    
    # 인덱스는 0부터 시작이지만, 입력값은 1부터 시작하므로 보정, 시작 배열을 1,1로 잡아서 
    for i in range(_number-2):
        
        # 새로운 수열이 생성될 배열
        new_queue = []

        # 제일 첫 값을 pop
        s1 = init_queue.pop(0)
        count = 1

        while init_queue:
            s2 = init_queue.pop(0)
            if s1 == s2:
                count+=1
                s1 = s2
            elif s1 != s2:
                new_queue.append(count)
                new_queue.append(s1)
                s1 = s2
                count=1

        
        new_queue.append(count)
        new_queue.append(s1)

        # 이전 결과가 다시 입력으로
        init_queue = new_queue.copy()
    
    # 출력
    print(f"{_number}th sequence is {new_queue}")
    median_value = int(len(new_queue)/2)-1
    print(f"and median value is { new_queue[ median_value:median_value+2]}")


if __name__ == "__main__":
    args = arg_parse()
    if args.number < 3:
        print("enter a value equal or grater than 3")
        sys.exit()
    
    run(args.number)