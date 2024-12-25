def matrix_min(matrix):
    min_value = float('inf')
    min_index = (-1, -1)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] < min_value:
                min_value = matrix[i][j]
                min_index = (i, j)

    return min_value, min_index


def find_opt_supply(A, B, C):
    sumA = sum(A)
    sumB = sum(B)
    fake_value = 2147483647

    if sumA != sumB:
        if sumA < sumB:
            A.append(sumB - sumA)
            C.append([fake_value] * len(B))
            print(f"Запасов поставщиков недостаточно, введен фиктивный поставщик {len(A)}")
        else:
            B.append(sumA - sumB)
            for i in range(len(A)):
                C[i].append(fake_value)
            print(f"Запросов потребителей недостаточно, введен фиктивный потребитель {len(B)}")

    plan = [[0] * len(B) for _ in range(len(A))]
    total_cost = 0

    while any(A) and any(B):
        min_value, (i, j) = matrix_min(C)

        if min_value == float('inf'):
            break

        qty = min(A[i], B[j])
        plan[i][j] = qty
        A[i] -= qty
        B[j] -= qty

        if C[i][j] != fake_value:
            total_cost += qty * C[i][j]


        if A[i] == 0:
            for k in range(len(C[i])):
                C[i][k] = float('inf')
        if B[j] == 0:
            for k in range(len(C)):
                C[k][j] = float('inf')
        [print(''.join(str(x))) for x in plan]

    return plan, total_cost


def calculate_total_plan_cost(plan, cost_matrix):
    total_cost = 0

    for i in range(len(plan)):
        for j in range(len(plan[i])):
            if cost_matrix[i][j] != 2147483647:
                total_cost += plan[i][j] * cost_matrix[i][j]

    return total_cost


def main():
    A = [220, 190, 50, 70]
    B = [120, 150, 80]
    C = [
        [3, 5, 5],
        [3, 2, 3],
        [2, 3, 4],
        [4, 1, 3]
    ]
    plan, total_cost = find_opt_supply(A, B, C)

    print("План поставок")
    for row in plan:
        print(row)
    print(f"Стоимость плана поставок {total_cost}")


if __name__ == '__main__':
    main()