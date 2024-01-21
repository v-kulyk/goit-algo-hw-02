from collections import deque

def is_palindrome(s):
    slower = s.lower().replace(' ', '') 
    dq = deque(slower)

    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    return True


if __name__ == '__main__':
    try:
        while True:
            s = input("введіть рядок: ")
            if is_palindrome(s):
                print("рядок паліндром")
            else:
                print("рядок не паліндром")
    except KeyboardInterrupt:
        pass