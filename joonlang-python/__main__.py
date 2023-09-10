import sys
from runtime import Joon

def main():
    if len(sys.argv) != 2:
        print("저는 강요 안 해요 ~ 파일 어딨습니까?")
    else:
        filename = sys.argv[1]
        if filename.endswith(".joon"):
            interpreter = Joon()
            interpreter.read_joon_file(filename)
        else:
            print("에러: 그래서 내가 쓴 글 읽었니? .joon 어디있나요?")

if __name__ == "__main__":
    main()
