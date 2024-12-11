from pulp import LpMaximize, LpProblem, LpStatus, lpSum, LpVariable

model = LpProblem(name="small-problem", sense=LpMaximize)

x = LpVariable(name="x", lowBound=0)
y = LpVariable(name="y", lowBound=0)

model += (-30 * x + 36 * y >= 294, "red_constraint")
model += (-10 * x - 27 * y >= -2788, "blue_constraint")
model += (-40 * x + 9 * y <= -1324, "yellow_constraint")

obj_func = 103 * x + 113 * y
model += obj_func
status = model.solve()
print(model.objective.value())
# model = LpProblem(name="small-problem")
#
# x = LpVariable(name="x", lowBound=0)
# y = LpVariable(name="y", lowBound=0)
#
# model += (7 * x + 6 * y >= 395, "red_constraint")
# model += (-21 * x + 3 * y >= -1101, "blue_constraint")
# model += (-42 * x - 6 * y >= -2502, "yellow_constraint")
# model += (-56 * x + 3 * y <= -2599, "green_constraint")
#
# obj_func = 190 * x + 129 * y
# model += obj_func
# status = model.solve()
# print(model.objective.value())

# model = LpProblem(name="small-problem")
#
# x = LpVariable(name="x", lowBound=0)
# y = LpVariable(name="y", lowBound=0)
#
# model += (9 * x + 12 * y >= 885, "red_constraint")
# model += (-81 * x - 6 * y >= -5109, "blue_constraint")
# model += (-72 * x + 6 * y <= -3306, "yellow_constraint")
#
# obj_func = 139 * x + 120 * y
# model += obj_func
# status = model.solve()
# print(model.objective.value())