#!/usr/bin/python3
str = "Python is an interpreted, object-oriented, high-level programming language with dynamic semantics. Its high-level built in data structures, combined with dynamic typing and dynamic binding, make it very attractive for Rapid Application Development."

str = str[26:41] + str[53:65] + str[74:80] + str[0:6]
print("{}".format(str))
