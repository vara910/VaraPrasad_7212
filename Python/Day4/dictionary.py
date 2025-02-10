d1={}
print("Empty dictionary-",d1)

d2={"spam":2,"eggs":3}
print("Dictionary with items(keys:values)-",d2)

d3={"food":{"idly":1,"dosa":2}}
print("Nested dictionary-",d3)
print("accessing item- ",d3["food"])
print("Accesing nested item-",d3["food"]["idly"])

d4=dict(name="vamshi",age="22")
print("converting into dictionary",d4)

lst1=["10","20","30","40"]
lst2=[1,2,3,4]

d5=dict(zip(lst1,lst2))
print("zipping 2 different lists as key value pairs: ",d5)

d6=dict.fromkeys(["a","b"])
print(d6)

print("printing keys of d5",d5.keys())
print("printing values of d5",d5.values())
print("printing key+value of d5",d5.items())

d7=d5.copy()
print("The copied data of d5 is d7:",d7)

print("Alternate method for accessing is using get",d5.get("10")) #D.get(key,default)

print("delete a pair for dictionary",d7.pop("10"))
print(d7)
