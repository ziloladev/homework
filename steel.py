import json
#1-misol
data1 = {"Model" : "Gentra", "Rang" : "Qizil", "Yil":2024, "Narh":15000}
data1_json = json.dumps(data1)
print(data1_json)

#2-misol
talaba = {"ism":"Hasan","familiya":"Husanov","tyil":2000}
talaba_json = json.dumps(talaba)
print(f"Talabaning ismi:{talaba['ism']} Talabaning familiyasi:{talaba["familiya"]}")

# 3-misol
with open('data.json','w') as f:
    json.dump(data1,f)

with open('talaba.json','w') as f:
    json.dump(talaba,f)
