from collections import defaultdict

def map_fun(text):
    words=text.strip().split()
    mapped=[]
    for word in words:
        mapped.append((word.lower(),1))
    return mapped

def sort(mapped):
    data=defaultdict(list)
    for word,count in mapped:
        data[word].append(count)
    return data

def reduce(data):
    r_data={}
    for word,count in data.items():
        r_data[word]=sum(count)
    return r_data

text="dog is dog cat is cat"    
mapped=map_fun(text)
data=sort(mapped)
r_data=reduce(data)

for word,count in r_data.items():
    print(f"{word}:{count}")





