
f = open("new.csv", "a")
import json
thisdict = {
"name": "Hima",
"age": 22,
"marks": 98
}
result = json.dumps(thisdict)
f.write(result)
f.close()
f = open("new.csv", "r")
print(f.read())
