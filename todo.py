import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 todo.py [task]")
        return
    
    task = sys.argv[1]
    with open("tasks.txt", "a") as f:
        f.write(task + "\n")
    print(f"Task added: {task}")

if __name__ == "__main__":
    main()
