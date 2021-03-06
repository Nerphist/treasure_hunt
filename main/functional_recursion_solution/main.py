def search_for_treasure(matrix, coordinate=11, runs=0, result='') -> str:
    x, y = map(lambda a: int(a) - 1, str(coordinate))
    cell_value = matrix[x][y]
    result += f'{coordinate} '
    runs += 1
    return result[:-1] if cell_value == coordinate else search_for_treasure(matrix, cell_value, runs,
                                                                            result) if runs < len(
        matrix) ** 2 else 'The map has no solution'
