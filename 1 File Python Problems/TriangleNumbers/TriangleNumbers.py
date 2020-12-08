"""
Basic Problem Summary:
    For a given integer, n
    Print the addition of all the values from 0 to n.

    Example Input: 4
    Example Output: 10
"""
def triangleNumber(n:int):
    return (n*(n+1) // 2)

if __name__ == "__main__":
    n = input("Enter a number to find out it's triangle.")
    print(triangleNumber(int(n)))