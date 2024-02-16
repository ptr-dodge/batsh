import argparse
import os
import requests
import subprocess

def read_code_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except Exception as e:
        print("Error reading file:", str(e))
        return None

def generate_output_file_name(input_file, target):
    base_name, ext = os.path.splitext(os.path.basename(input_file))
    if target == "bash":
        return base_name + ".sh"
    elif target == "winbat":
        return base_name + ".bat"

def get_output_directory(target):
    if target == "bash":
        return os.path.dirname(os.path.abspath(__file__))
    elif target == "winbat":
        return os.path.dirname(os.path.abspath(__file__))

def do_compile(target, code, output_file, silent):
    api_url = "https://batsh.org/compile"
    payload = {
        'target': target,
        'code': code
    }

    try:
        response = requests.post(api_url, data=payload)
        if response.status_code == 200:
            data = response.json()
            if 'err' in data:
                if not silent:
                    print("Error:", data['err'])
            else:
                output_dir = get_output_directory(target)
                os.makedirs(output_dir, exist_ok=True)
                output_path = os.path.join(output_dir, output_file)
                with open(output_path, 'w') as f:
                    f.write(data['code'])
                if not silent:
                    print("Compilation successful. Output written to", output_path)
        else:
            if not silent:
                print("Failed to compile:", response.text)
    except Exception as e:
        if not silent:
            print("An error occurred:", str(e))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Compile Batsh code to Bash or Winbat")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--bash", action="store_true", help="Compile Batsh code to Bash")
    group.add_argument("--winbat", action="store_true", help="Compile Batsh code to Winbat")
    parser.add_argument("-i", "--input", required=True, help="Input Batsh code file")
    parser.add_argument("-o", "--output", required=True, help="Output Batsh code file")
    parser.add_argument("--silent", action="store_true", help="Suppress verbose output")
    args = parser.parse_args()

    if args.bash:
        target = "bash"
    elif args.winbat:
        target = "winbat"

    input_file = os.path.abspath(args.input)  # Get absolute path for the input file
    code = read_code_from_file(input_file)
    if code:
        output_file = generate_output_file_name(input_file, target)
        do_compile(target, code, output_file, args.silent)
