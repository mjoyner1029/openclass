weather = int(input("what is the weather today in fahrenheit?:"))
event = input("what kind of event is it?(formal/casual):")

if weather < 59:
    if event == "formal":
        print("a Warm formal suit")
    else:
        print("cozy sweater and jeans")
elif weather >= 59:
   if event == "formal":
      print("light formal suit")
else:
    print("t-shirt and shorts")