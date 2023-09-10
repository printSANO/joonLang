import sys

class Joon:
    def __init__(self) -> None:
        self.data = {}
        self.start_marker = "하시면 어떻게든 됩니다."
        self.end_marker = "부트캠프 멘토 그만해야지."
    
    def read_joon_file(self, filename) -> None:
        try:
            with open(filename, 'r', encoding="UTF-8") as joon_file:
                lines = joon_file.readlines()
                val, message = self.validate_joon_code(lines)
                if val:
                    for line in lines:
                        l = line.strip()
                        if l != self.start_marker and l != self.end_marker and l != '':
                            print(l)
                else:
                    if message == self.start_marker:
                        print("에러: 어떻게 하셔도 안되네요?")
                    elif message == self.end_marker:
                        print("에러: 부트캠프 멘토 계속 해야겠네....")

        except FileNotFoundError:
            print(f"에러: 안타깝네요 '{filename}'가 없네요.")
    
    def validate_joon_code(self, lines) -> bool and str:
        if len(lines) < 2:
            return False
        
        start_marker = "하시면 어떻게든 됩니다."
        end_marker = "부트캠프 멘토 그만해야지."
        
        if lines[0].strip() != start_marker:
            return False, start_marker
        if lines[-1].strip() != end_marker:
            return False, end_marker
        
        return True, None

        