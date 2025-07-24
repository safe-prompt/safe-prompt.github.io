import subprocess

def install_package(package):
    subprocess.run(["apt", "install", "-y", package])
    print(f"Installed {package}")

# Example usage
install_package('nginx')
