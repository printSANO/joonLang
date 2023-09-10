import sys

def validate_joon_code(lines):
    if len(lines) < 2:
        return False
    
    start_marker = "하시면 어떻게든 됩니다."
    end_marker = "부트캠프 멘토 그만해야지."
    
    if lines[0].strip() != start_marker:
        return False, start_marker
    if lines[-1].strip() != end_marker:
        return False, end_marker
    
    return True, None

def read_joon_file(filename):
    start_marker = "하시면 어떻게든 됩니다."
    end_marker = "부트캠프 멘토 그만해야지."
    try:
        with open(filename, 'r') as joon_file:
            lines = joon_file.readlines()
            val, message = validate_joon_code(lines)
            if val:
                for line in lines:
                    l = line.strip()
                    if l != start_marker and l != end_marker and l != '':
                        print(l)
            else:
                if message == start_marker:
                    print("에러: 어떻게 하셔도 안되네요?")
                elif message == end_marker:
                    print("에러: 부트캠프 멘토 계속 해야겠네....")

    except FileNotFoundError:
        print(f"에러: 안타깝네요 '{filename}'가 없네요.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("저는 강요 안 해요 ~ 파일 어딨습니까?")
    else:
        filename = sys.argv[1]
        if filename.endswith(".joon"):
            read_joon_file(filename)
        else:
            print("에러: 그래서 내가 쓴 글 읽었니? .joon 어디있나요?")
