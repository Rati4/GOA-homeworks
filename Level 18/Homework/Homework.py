#ახსენით and ოპერატორი თქვენი სიტყვებით. and აღნიშნავას როცა მაგალითდ ორი False რომ გვაქვს და ერთი True ის გადაიქცევა False.
# 3) ახსენით or ოპერატორი თქვენი სიტყვებით. or აღნიშნავს როცა ერთი True_ა რამდენიც იყოს False მაინც True იქნება


#4) გაამარტივეთ მოცემული კოდი:

print((True or False) and (True and True))
print((True or False) and (False or False))
print((False and True) or (True and False))
print((False or False) and (True or True))
print((True and True) or (False and True))
print((False or True) and (True and False))
print((False and False) or (False or True))
print((True or False) and (False or True))
print((True and False) or (True and False))
print((True and True) or (True and False))
print((False and False) or (True or bool(5)  )
print((True or True) and (False and False))
print((False or True) and (True or True))
print((True and False) or (True and False))

print((True or (True or False)) and (True and True)

#გამარტივების მაგალითი:

print((True or (True and True)) and (False or False))
# (True or True) and False -> True and False -> False