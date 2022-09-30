#a dictionary cannot have duplicate items 

dish ={ "fruits": ["apple","mango","banana"],
        "happy" :"joyful",
        1:2,
        "sdish":{"no":"you"}

}
print(dish.keys())
print(dish.values())
print(dish.items())

#updting dictionary

mod1 ={ "fast":"quick",
        "friend":"companion"

}
dish.update(mod1)
print(dish)
print(dish[1])
print(dish["happy"])
#.get methods returns null if key is not present hence no error 
print(dish.get("sad"))