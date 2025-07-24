import subprocess

def push_code(repo_path):
    subprocess.run(["git", "push", "origin", "main"])
    print("Code pushed to production.")

# Example usage
push_code('/path/to/repo')
