import logging


def evaluating_formula(schoolboy, formula):
    try:
        solution = eval(formula)
    except (SyntaxError, Exception) as exc:
        fail_reason = "Unable to evaluate formula '{}', because: '{}'".format(
                formula, exc)
        logging.error(fail_reason)
        schoolboy.fail(reason=fail_reason)
    else:
        logging.info("Evaluated formula '%s' to '%s'", formula, solution)
        schoolboy.raise_hand(solution)
