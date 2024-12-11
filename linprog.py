from scipy.optimize import linprog

obj = [163, 190]

lhs_ineq = [[32,  -40],
            [16, 24],
            [-48, 16]]

rhs_ineq = [-1688,
            3160,
            -64]

opt = linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq,
              method="highs")

print(opt.fun)

# obj = [-153, -104]
#
# lhs_ineq = [[-18,  -6],
#             [18, -2],
#             [24, -2],
#             [-24, 10]]
#
# rhs_ineq = [-270,
#             102,
#             162,
#             342]
#
# opt = linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq,
#               method="highs")
#
# print(-opt.fun)

