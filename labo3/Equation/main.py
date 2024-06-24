from Equation import Equation
from QuadraticEquation import QuadraticEquation
from BiQuadraticEquation import BiQuadraticEquation

file_names = ("input01.txt", "input02.txt", "input03.txt")
output_context = ""

for file_name in file_names:
    with open(file_name, 'r') as file:
        TITLE = f"\n\n{file_name}\n\n"
        output_context += TITLE

        all_equations = []
        zero_roots = []
        one_root = []
        two_roots = []
        three_roots = []
        four_roots = []
        inf_roots = []

        for line in file:
            line = [int(d) for d in line.split()]
            if len(line) == 2:
                equation = Equation(*line)
            elif len(line) == 3:
                equation = QuadraticEquation(*line)
            else:
                a = line[0]
                b = line[2]
                c = line[4]
                equation = BiQuadraticEquation(a, b, c)

            solution = equation.solve()
            if isinstance(solution, tuple):
                solution_count = len(solution)
                if solution_count == 0:
                    zero_roots.append(equation)
                elif solution_count == 1:
                    one_root.append(equation)
                elif solution_count == 2:
                    two_roots.append(equation)
                elif solution_count == 3:
                    three_roots.append(equation)
                elif solution_count == 4:
                    four_roots.append(equation)
            else:
                inf_roots.append(equation)

            all_equations.append((equation, solution))


        equations_by_roots = {
            "Немає розв'язків": zero_roots,
            "Один розв'язок": one_root,
            "Два розв'язки": two_roots,
            "Три розв'язки": three_roots,
            "Чотири розв'язки": four_roots,
            "Нескінченна кількість розв'язків": inf_roots
        }

        for key, equations in equations_by_roots.items():
            if equations:
                output_context += f"{key}:\n"
                for equation in equations:
                    output_context += f"{equation}\n"

        # Find equation with minimum and maximum root among equations with exactly one root
        if one_root:
            min_root_equation = min(one_root, key=lambda x: x.solve())
            max_root_equation = max(one_root, key=lambda x: x.solve())
            output_context += f"\nРівняння з найменшим розв'язком:\n{min_root_equation}\n"
            output_context += f"Рівняння з найбільшим розв'язком:\n{max_root_equation}\n"

# Write output to file
with open('output.txt', 'w', encoding='utf-8') as output:
    output.write(output_context)
