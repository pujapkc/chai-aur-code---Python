Weather = {"Summer":"hot","winter":"cold","Autumn":"fresh"}

#get() to get the values of keys in dictionaries
print(Weather.get("Summer"))

#for loop to print weather

for weather_types in Weather:
    print(weather_types) 


#to print both keys and values

for weather_types in Weather:
    print(weather_types, Weather[weather_types])    


#one more syntax type to print key and value

for key,value in Weather.items():
    print(key,value)


    
