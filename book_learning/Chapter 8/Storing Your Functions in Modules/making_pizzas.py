# Section:Importing an Entire Module

import pizza

# To access any method from the pizza file, use the following syntax:
# module_name.function_name()

# from pizza import make_pizza
#
# This is an additional way to import, but allows you to be more specific about
# what method(s) or class you want to import versus an entire file/directory. To
# import more than one function sperate the function names with commas.
#
# You can also use `from pizza import *` to import all functions from the file.
# This is not the best approach, but people do use it.
#
# General syntax for doing this is:
# `from module_name import *`

pizza.make_pizza(16, "pepperoni")
pizza.make_pizza(12, "mushrooms", "green peppers", "extra cheese")

# If we were to have used the `from pizza import make_pizza` import, the method
# calls would look a little different.
#
# For Example:
# make_pizza(16, "pepperoni")
# make_pizza(12, "mushrooms", "green peppers", "extra cheese")


# You can also give an imported function an alias when importing. For example,
# you could do this: `from pizza import make_pizza as mp`. So, instead of
# using the function name, `make_pizza` to call the function you would use `mp`.
#
# For Example:
# mp(16, "pepperoni")
# mp(12, "mushrooms", "green peppers", "extra cheese")
#
# The general syntax for providing an alias is:
# `from module_name import function_name as fn`

# Aliasing also works for importing files. So instead of our current import we
# could have used `import pizza as p`. So our method calls would look like this:
#
# p.make_pizza(16, "pepperoni")
# p.make_pizza(12, "mushrooms", "green peppers", "extra cheese")
#
# The general syntax is:
# `import module_name as mn`
