def calculate_span(arr):
    stack = []
    result = []

    stack.append(0)

    result[0] = 1

    n = len(arr)

    for i in range(1, n):
        while(len(stack) > 0 and arr[stack[0]] <= arr[i]):
            stack.pop()

        result[i]
