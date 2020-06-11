# unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
# completed_models = []
#
# while unprinted_designs:
#     current_design = unprinted_designs.pop()
#     print("Printing model: " + current_design)
#     completed_models.append(current_design)
#
#
# print("\nThe following models have been printed: ")
# for completed_model in completed_models:
#     print(completed_model)
from printing_functions import *

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
