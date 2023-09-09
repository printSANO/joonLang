import sys

def validate_joon_code(lines):
    if len(lines) < 2:
        return False
    
    start_marker = "하시면 어떻게든 됩니다."
    end_marker = "그것이 팀준이니까."
    
    if lines[0].strip() != start_marker or lines[-1].strip() != end_marker:
        return False
    
    return True

def read_joon_file(filename):
    start_marker = "하시면 어떻게든 됩니다."
    end_marker = "그것이 팀준이니까."
    try:
        with open(filename, 'r') as joon_file:
            lines = joon_file.readlines()
            if validate_joon_code(lines):
                for line in lines:
                    l = line.strip()
                    if l != start_marker and l != end_marker and l != '':
                        print(l)  # Print each line, removing leading/trailing whitespace
            else:
                print("Error: The code block does not start with '하시면 어떻게든 됩니다.' or end with '그것이 팀준이니까.'")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python joon_interpreter.py <filename.joon>")
    else:
        filename = sys.argv[1]
        if filename.endswith(".joon"):
            read_joon_file(filename)
        else:
            print("Error: The file should have a '.joon' extension.")
