codeup = [
    " ****  ***  ***   ***** *   * ****",
    "*     *   * *  *  *     *   * *   *",
    "*     *   * *   * *     *   * *   *",
    "*     *   * *   * ****  *   * ****",
    "*     *   * *   * *     *   * *",
    "*     *   * *  *  *     *   * *",
    " ****  ***  ***   *****  ***  *"
]
n, m = map(int, input().split())
for i in codeup:
    r = ''
    for j in i:
        r += j * n
    for k in range(m):  
        print(r)