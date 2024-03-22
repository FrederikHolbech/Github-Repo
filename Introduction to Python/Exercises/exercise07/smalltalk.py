
mood_in_scale = int(input("How are you doing, on a scale from 1 to 5?"))
    
if not type(mood_in_scale) is int or mood_in_scale>5:
    print = "That isn't on the scale"
if mood_in_scale > 3:
    result_mood = "That is lovely to hear!"
if mood_in_scale < 2:
    result_mood = "I am sorry to hear"
print(result_mood)

weather_opinion = input("Do you like the weather today?")
if not weather_opinion in ["Yes","No"]:
    result_weather = "That doesn't answer the question"
if weather_opinion == "Yes":
    result_weather = "Me too, it is lovely today"
if weather_opinion == "No":
    result_weather = "Yeah it is pretty grey outside"

print(result_weather)

