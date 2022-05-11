# A lambda is an anonymous function that returns some form of data.
# parameters are optional
# lambda cannot be multiline
# lambda parameter : expression

triple = lambda n: n * 3
print(triple(10))

concat_strings = lambda a, b, c: a[0] + b[0] + c[0]
print(concat_strings("World", "Wide", "Web"))

# when using a lambda you need both if and else
my_func = lambda num: "High" if num > 50 else "Low"
print(my_func(60))
