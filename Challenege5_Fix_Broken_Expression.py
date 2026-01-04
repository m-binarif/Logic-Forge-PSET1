def fix_broken_expression(expr):

    def is_valid(text):
        open_count = 0
        for ch in text:
            if ch == '(':
                open_count += 1
            elif ch == ')':
                if open_count == 0:
                    return False
                open_count -= 1
        return open_count == 0

    queue = [expr]
    checked = {expr}
    answers = []
    level_done = False

    while queue:
        current_expr = queue.pop(0)

        if is_valid(current_expr):
            answers.append(current_expr)
            level_done = True

        if level_done:
            continue

        for idx in range(len(current_expr)):
            if current_expr[idx] != '(' and current_expr[idx] != ')':
                continue

            next_expr = current_expr[:idx] + current_expr[idx+1:]

            if next_expr not in checked:
                checked.add(next_expr)
                queue.append(next_expr)

    return answers

print(fix_broken_expression("()())()"))

print(fix_broken_expression("(a)())()"))

print(fix_broken_expression(")("))

print(fix_broken_expression("((("))

print(fix_broken_expression("abc"))
