import sys

class Joon:
    def __init__(self) -> None:
        self.data = {}
        self.start_marker = "하시면 어떻게든 됩니다."
        self.end_marker = "부트캠프 멘토 그만해야지."
        self.operators = ["네?", "에?", "워터밤"]
    
    def read_joon_file(self, filename) -> None:
        try:
            with open(filename, 'r', encoding="UTF-8") as joon_file:
                lines = joon_file.readlines()
                val, message = self.validate_joon_code(lines)
                if val:
                    for line in lines:
                        l = line.strip()
                        if l != self.start_marker and l != self.end_marker and l != '' and not l.startswith('#'):
                            self.check_type(l)
                else:
                    if message == self.start_marker:
                        print("에러: 어떻게 하셔도 안되네요?")
                    elif message == self.end_marker:
                        print("에러: 부트캠프 멘토 계속 해야겠네....")

        except FileNotFoundError:
            print(f"에러: 안타깝네요 '{filename}'가 없네요.")
    
    def validate_joon_code(self, lines) -> bool and str:
        if len(lines) < 2:
            return False, "여러분 그럴 시간에 코드 한 줄 더 쓰세요."
        
        start_marker = "하시면 어떻게든 됩니다."
        end_marker = "부트캠프 멘토 그만해야지."
        
        if lines[0].strip() != start_marker:
            return False, start_marker
        if lines[-1].strip() != end_marker:
            return False, end_marker
        
        return True, None
    
    # calculate values from 네?, 에?, and 워터밤
    def calculate_val(self, line) -> int:
        pass

    def check_type(self, line) -> str:
        if "님이말씀해보세요" in line:
            pass
        elif "님?" in line:
            pass
        elif "자러가시는거에요" in line:
            pass
        elif "님맥사세요" in line:
            pass
        elif "그냥여쭤^^보는거에요" in line:
            pass
    
    # 님이말씀해보세요
    def parse_var(self, line):
        pass

    # 님?
    def parse_assign(self, line):
        pass

    # 자러가시는거에요
    def parse_loop(self, line):
        pass

    # 님맥사세요
    def parse_output(self, line):
        pass

    # 그냥여쭤^^보는거에요
    def parse_condition(self, line):
        pass