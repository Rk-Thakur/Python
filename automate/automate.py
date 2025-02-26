import os
import subprocess

# Configuration
REPO_PATH = "./application/"  # Change this to your Flutter project path
BRANCH = "main"  # Change this to your branch name
COMMIT_MESSAGE = "Automated commit: Updated Flutter app project file only"

def run_command(command, cwd=None):
    """Runs a shell command in the specified directory."""
    result = subprocess.run(command, shell=True, cwd=cwd, text=True, capture_output=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
        exit(1)
    return result.stdout.strip()

def push_code():
    print("Navigating to the Flutter project directory...")
    if not os.path.exists(REPO_PATH):
        print("Error: Specified repo path does not exist.")
        return

    print("Adding changes to Git...")
    run_command("git add .", cwd=REPO_PATH)

    print("Committing changes...")
    run_command(f'git commit -m "{COMMIT_MESSAGE}"', cwd=REPO_PATH)

    print(f"Pushing code to {BRANCH} branch...")
    run_command(f"git push origin {BRANCH}", cwd=REPO_PATH)

    print("Code pushed successfully!")

if __name__ == "__main__":
    push_code()
