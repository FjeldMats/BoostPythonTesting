#!/usr/bin/python3.10

import classes
c = classes.World()
print(c)
c.set("Hello")
c.many(["1", "2", "3"])
print(c.greet())
