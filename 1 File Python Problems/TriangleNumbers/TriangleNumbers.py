
def triangleNumber(n:int):
    return (n*(n+1) // 2)

if __name__ == "__main__":
    n = input("Enter a number to find out it's triangle.")
    print(triangleNumber(int(n)))