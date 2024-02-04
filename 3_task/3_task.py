import sys
from pathlib import Path
from colorama import init, Fore, Back, Style


init()

def print_directory_tree(path: Path, prefix = "", should_print_root_dir = True):
    if path.exists() == False:
        print(f"{Fore.RED}{path} does not exist.{Style.RESET_ALL}")
        return
    
    if path.is_dir() == False:
        print(f"{Fore.RED}{path} is not a directory.{Style.RESET_ALL}")
        return
    
    if should_print_root_dir:
        print(f"{Back.MAGENTA}📦{path.name}{Style.RESET_ALL}")

    for i in path.iterdir():
        print(f"{prefix}├─ {"📂" if i.is_dir() else "📜"}{Fore.GREEN if i.is_dir() else Fore.YELLOW}{i.name}{Style.RESET_ALL}")
        if i.is_dir():
            print_directory_tree(i, f"{prefix}│ ", False)

def main():
    if len(sys.argv) < 2:
        print("Invalid arguments.")
    else:
        path = sys.argv[1]
        print_directory_tree(Path(path))

if __name__ == "__main__":
    main()
