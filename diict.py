point = (1, 2, 3)

print (type(point))

student = {
    "name" : "Rajee",
    "age" : 20,
    "year" : 2025,
    "likes" : "cats"
}

student["age"] = 200
student["yearns"] = "for greatness"

del student["age"]

print(student)

scores = [90, 85, 88, 92]
scores.append(95)

scores[1] = 89

print(scores)

location = (31.5, 74.3)
location[0] = 32.0

#error cause touple can't be changed

student = {"nwme" : "Zein", "age": 20}
student["course"] = "AI"
print(student)
