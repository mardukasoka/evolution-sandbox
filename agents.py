import random
import math
import operator

ops = [('+', operator.add), ('-', operator.sub), ('*', operator.mul), ('/', lambda a, b: a / b if b != 0 else 1)]

def random_expr():
    return f"{random.randint(1, 10)} {random.choice(['+', '-', '*', '/'])} {random.randint(1, 10)}"

def eval_expr(expr):
    try:
        return eval(expr)
    except:
        return float('inf')

def mutate(expr):
    parts = expr.split()
    idx = random.randint(0, 2)
    if idx % 2 == 0:
        parts[idx] = str(random.randint(1, 10))
    else:
        parts[idx] = random.choice(['+', '-', '*', '/'])
    return ' '.join(parts)

def evolve_agent(name, target, emotion_mod, memory):
    population = [random_expr() for _ in range(5)]
    scored = [(expr, -abs(eval_expr(expr) - target)) for expr in population]
    best_expr, best_score = max(scored, key=lambda x: x[1])
    for _ in range(3 + emotion_mod):
        mutated = mutate(best_expr)
        score = -abs(eval_expr(mutated) - target)
        if score > best_score:
            best_expr, best_score = mutated, score
    memory.store(name, best_expr, best_score)
    return {'agent': name, 'expression': best_expr, 'score': best_score}