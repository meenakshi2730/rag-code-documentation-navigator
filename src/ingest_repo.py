import os

def load_code_files(repo_path):
    code_files = []
    for root, _, files in os.walk(repo_path):
        for file in files:
            if file.endswith((".py", ".js", ".java", ".cpp")):
                code_files.append(os.path.join(root, file))
    return code_files

if __name__ == "__main__":
    repo_path = "sample_repo"
    files = load_code_files(repo_path)
    print(f"Found {len(files)} code files")
