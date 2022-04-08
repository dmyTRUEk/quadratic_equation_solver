# quadratic equation

from math import sqrt



class UnreachableException(Exception):
    pass

def unreachable():
    raise UnreachableException()



# def solve_quadratic_equation(a: float, b: float, c: float) -> (float, float) | None | str:
def solve_quadratic_equation(a: float, b: float, c: float) -> '(float, float) | float | str | None':
    if a == 0:
        # linear equation: bx + c = 0   =>   x = -c/b
        if b != 0:
            return -c/b
        else:
            # return "if `a` is zero, then `b` must be non zero"
            if c == 0:
                return "`x` can be any Real Number."
            else:
                return None

    discriminant = b*b - 4*a*c
    # print(f"{discriminant = }")

    # match discriminant:
    if discriminant < 0:    # case discriminant if discriminant < 0:
        # print("d < 0")
        return None
    elif discriminant == 0: # case discriminant if discriminant == 0:
        # print("d = 0")
        x = -b / (2 * a)
        return x
    elif discriminant > 0:  # case discriminant if discriminant > 0:
        # print("d > 0")
        x1 = (-b - sqrt(discriminant)) / (2 * a)
        x2 = (-b + sqrt(discriminant)) / (2 * a)
        return x1, x2
    else:                   # case _:
        unreachable()



def parse_inputed_str_to_a_b_c(s: str) -> '(float, float, float) | str':
    l = s.split(' ')
    try:
        a, b, c = l
    except ValueError as _:
        return f"expected 3 values, but {len(l)} got"
    except Exception as _:
        # # TODO:
        # print(f"Error in parse_inputed_str_to_a_b_c: `{type(exception)}`: `{exception}`.")
        # return None
        unreachable()

    try:
        a = float(a)
    except ValueError as _:
        return f"expected 3 float values, but `a` is not float: `a`=\"{a}\""

    try:
        b = float(b)
    except ValueError as _:
        return f"expected 3 float values, but `b` is not float: `b`=\"{b}\""

    try:
        c = float(c)
    except ValueError as _:
        return f"expected 3 float values, but `c` is not float: `c`=\"{c}\""

    return a, b, c




def parse_inputed_str_to_answer(inputed_str: str) -> (int, str):
    parse_result = parse_inputed_str_to_a_b_c(inputed_str)
    if not isinstance(parse_result, tuple):
        error_text = parse_result
        return -1, f"Error occured while parsing input: `{error_text}`."
    a, b, c = parse_result
    solution_result = solve_quadratic_equation(a, b, c)

    # match solution_result:
    if solution_result == None:                 # case None:
        return -1, f"Equation `{a}x² + {b}x + {c} = 0` have no real solutions."
    elif isinstance(solution_result, str):      # case str(error_str):
        error_str = solution_result
        return -1, f"{error_str}"
    elif isinstance(solution_result, tuple):    # case float(x1), float(x2):
        x1, x2 = solution_result
        return 0, f"Solutions of equation `{a}x² + {b}x + {c} = 0` is: `x1` = {x1}, `x2` = {x2}."
    elif isinstance(solution_result, float):    # case float(x):
        x = solution_result
        return 0, f"Solutions of equation `{a}x² + {b}x + {c} = 0` is: `x` = {x}."
    else:                                       # case _:
        unreachable()





def main() -> int:
    print("This is Quadratic Equation solver: finds solutions for `ax² + bx + c = 0`.")
    inputed_str = input("Input `a`, `b`, `c` separated by space: ")
    res_code, answer = parse_inputed_str_to_answer(inputed_str)
    print(answer)
    return res_code



def tests():
    test_cases = [
        # data, expected result

        # wrong input:
        ("", (-1, 'Error occured while parsing input: `expected 3 values, but 1 got`.')),
        ("1", (-1, 'Error occured while parsing input: `expected 3 values, but 1 got`.')),
        ("1 2", (-1, 'Error occured while parsing input: `expected 3 values, but 2 got`.')),
        ("1 2 3 4", (-1, 'Error occured while parsing input: `expected 3 values, but 4 got`.')),
        ("a", (-1, 'Error occured while parsing input: `expected 3 values, but 1 got`.')),
        ("1 b", (-1, 'Error occured while parsing input: `expected 3 values, but 2 got`.')),
        ("a 2 3", (-1, 'Error occured while parsing input: `expected 3 float values, but `a` is not float: `a`="a"`.')),
        ("1 b 3", (-1, 'Error occured while parsing input: `expected 3 float values, but `b` is not float: `b`="b"`.')),
        ("1 2 c", (-1, 'Error occured while parsing input: `expected 3 float values, but `c` is not float: `c`="c"`.')),
        ("1 2 3 d", (-1, 'Error occured while parsing input: `expected 3 values, but 4 got`.')),

        # linear equations:
        ("0 0 0", (-1, "`x` can be any Real Number.")),
        ("0 0 1", (-1, "Equation `0.0x² + 0.0x + 1.0 = 0` have no real solutions.")),
        ("0 0 -1", (-1, "Equation `0.0x² + 0.0x + -1.0 = 0` have no real solutions.")),
        ("0 1 0", (0, 'Solutions of equation `0.0x² + 1.0x + 0.0 = 0` is: `x` = -0.0.')),
        ("0 1 1", (0, 'Solutions of equation `0.0x² + 1.0x + 1.0 = 0` is: `x` = -1.0.')),
        ("0 2 1", (0, 'Solutions of equation `0.0x² + 2.0x + 1.0 = 0` is: `x` = -0.5.')),
        ("0 1 2", (0, 'Solutions of equation `0.0x² + 1.0x + 2.0 = 0` is: `x` = -2.0.')),
        ("0 2 -1", (0, 'Solutions of equation `0.0x² + 2.0x + -1.0 = 0` is: `x` = 0.5.')),
        ("0 1 -2", (0, 'Solutions of equation `0.0x² + 1.0x + -2.0 = 0` is: `x` = 2.0.')),
        ("0 -2 1", (0, 'Solutions of equation `0.0x² + -2.0x + 1.0 = 0` is: `x` = 0.5.')),
        ("0 -1 2", (0, 'Solutions of equation `0.0x² + -1.0x + 2.0 = 0` is: `x` = 2.0.')),

        # a = 1
        ("1 0 1", (-1, "Equation `1.0x² + 0.0x + 1.0 = 0` have no real solutions.")),
        ("1 0 -1", (0, 'Solutions of equation `1.0x² + 0.0x + -1.0 = 0` is: `x1` = -1.0, `x2` = 1.0.')),

        # a = 2
        ("2 0 0", (0, 'Solutions of equation `2.0x² + 0.0x + 0.0 = 0` is: `x` = -0.0.')),
        ("2 0 1", (-1, 'Equation `2.0x² + 0.0x + 1.0 = 0` have no real solutions.')),
        ("2 0 -1", (0, 'Solutions of equation `2.0x² + 0.0x + -1.0 = 0` is: `x1` = -0.7071067811865476, `x2` = 0.7071067811865476.')),
        ("2 1 1", (-1, 'Equation `2.0x² + 1.0x + 1.0 = 0` have no real solutions.')),
        ("2 1 -1", (0, 'Solutions of equation `2.0x² + 1.0x + -1.0 = 0` is: `x1` = -1.0, `x2` = 0.5.')),
        ("2 -1 1", (-1, 'Equation `2.0x² + -1.0x + 1.0 = 0` have no real solutions.')),
        ("2 -1 -1", (0, 'Solutions of equation `2.0x² + -1.0x + -1.0 = 0` is: `x1` = -0.5, `x2` = 1.0.')),

        ("1 0 2", (-1, 'Equation `1.0x² + 0.0x + 2.0 = 0` have no real solutions.')),
        ("1 0 -2", (0, 'Solutions of equation `1.0x² + 0.0x + -2.0 = 0` is: `x1` = -1.4142135623730951, `x2` = 1.4142135623730951.')),
        ("1 1 2", (-1, 'Equation `1.0x² + 1.0x + 2.0 = 0` have no real solutions.')),
        ("1 1 -2", (0, 'Solutions of equation `1.0x² + 1.0x + -2.0 = 0` is: `x1` = -2.0, `x2` = 1.0.')),
        ("1 -1 2", (-1, 'Equation `1.0x² + -1.0x + 2.0 = 0` have no real solutions.')),
        ("1 -1 -2", (0, 'Solutions of equation `1.0x² + -1.0x + -2.0 = 0` is: `x1` = -1.0, `x2` = 2.0.')),

        ("-2 0 0", (0, 'Solutions of equation `-2.0x² + 0.0x + 0.0 = 0` is: `x` = 0.0.')),
        ("-2 0 1", (0, 'Solutions of equation `-2.0x² + 0.0x + 1.0 = 0` is: `x1` = 0.7071067811865476, `x2` = -0.7071067811865476.')),
        ("-2 0 -1", (-1, 'Equation `-2.0x² + 0.0x + -1.0 = 0` have no real solutions.')),
        ("-2 -1 0", (0, 'Solutions of equation `-2.0x² + -1.0x + 0.0 = 0` is: `x1` = -0.0, `x2` = -0.5.')),
        ("-2 1 1", (0, 'Solutions of equation `-2.0x² + 1.0x + 1.0 = 0` is: `x1` = 1.0, `x2` = -0.5.')),
        ("-2 1 -1", (-1, 'Equation `-2.0x² + 1.0x + -1.0 = 0` have no real solutions.')),
        ("-2 -1 1", (0, 'Solutions of equation `-2.0x² + -1.0x + 1.0 = 0` is: `x1` = 0.5, `x2` = -1.0.')),
        ("-2 -1 -1", (-1, 'Equation `-2.0x² + -1.0x + -1.0 = 0` have no real solutions.')),
    ]
    print("Running tests:\n")
    wrong_tests_amount = 0
    ok_tests_amount = 0
    for test_case in test_cases:
        expected = test_case[1]
        data = test_case[0]
        actual = parse_inputed_str_to_answer(data)
        if expected == actual:
            # print(f"OK: test {data}")
            ok_tests_amount += 1
        else:
            print(f"WRONG ANSWER: test \"{data}\":\n    {expected = }\n    {actual   = }")
            wrong_tests_amount += 1
    print()
    if wrong_tests_amount == 0:
        print(f"All {ok_tests_amount} tests OK.")
    else:
        print(f"Tests result: {ok_tests_amount} tests OK, {wrong_tests_amount} tests WRONG.")



if __name__ == "__main__":
    tests()
    print(3*'\n', end='')
    main()



