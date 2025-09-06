import os
import requests
import json
import subprocess

def LLM_analyze(del_lines, patch, add_lines, patch_last, funcs):
    # Placeholder for LLM analysis logic
    result = {
        "del_lines": del_lines,
        "patch": patch,
        "add_lines": add_lines,
        "patch_last": patch_last,
        "funcs": funcs,
        "analysis": "LLM analysis result"
    }
    return json.dumps(result)

def LLM_vulfix(description, patch):
    # Placeholder for LLM vulnerability fix detection logic
    if "vulnerability fix" in description:
        return 1
    return 0

def delete_folder_if_smaller_than_1gb(folder_path):
    total_size = get_folder_size(folder_path)
    if total_size < 1 * 1024 * 1024 * 1024:
        subprocess.run(["rm", "-rf", folder_path])

def file_download(url, save_path):
    response = requests.get(url)
    with open(save_path, 'wb') as file:
        file.write(response.content)

def find_function_define(root_node, code, line_number):
    # Placeholder for function definition finding logic
    function_name = "example_function"
    function_code = "void example_function() {}"
    return function_code, function_name

def get_add_lines(patch):
    lines = patch.split('\n')
    add_lines = [line for line in lines if line.startswith('+')]
    del_lines = [line for line in lines if line.startswith('-')]
    return del_lines if del_lines else add_lines

def get_commit(filepath, repo, sha):
    command = f"git log --pretty=format:'%H' {filepath}"
    result = run_git_command(command, repo)
    return result.split('\n')

def get_commit_information(repo_url):
    response = requests.get(repo_url)
    return response.json()

def get_file_history(repo_path, file_path):
    command = f"git log --follow --pretty=format:'%H' {file_path}"
    result = run_git_command(command, repo_path)
    return result.split('\n')

def get_folder_size(folder_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(folder_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size

def get_func(file_path, line_number):
    # Placeholder for function extraction logic
    function_name = "example_function"
    function_code = "void example_function() {}"
    return function_code, function_name

def get_functions(commit):
    # Placeholder for function extraction logic from commit
    modified_functions = ["example_function"]
    return modified_functions

def get_line(patch):
    lines = patch.split('\n')
    line_numbers = [i + 3 for i, line in enumerate(lines) if line.startswith('-')]
    return line_numbers

def get_repo(url):
    repo_name = url.split('/')[-1]
    return repo_name

def run_git_command(command, repo_path):
    try:
        result = subprocess.run(command, cwd=repo_path, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return str(e)

def url_change(url):
    repo_url = url.replace("https://github.com/", "git@github.com:")
    return repo_url

def vul_intro_check(commit_infor):
    modified_files = [file['filename'] for file in commit_infor['files']]
    return modified_files