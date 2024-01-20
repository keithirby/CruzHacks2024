import json

null_tuitin_location = []
null_tuition = []
null_location = []
whole_data = []


with open('output.txt', 'r') as file:
    for line in file:
        data = json.loads(line)
        colleges = data['results']

        for college in colleges:
            if college['latest.cost.tuition.in_state'] == None and college['latest.cost.tuition.out_of_state'] == None:
                if college['location.lat'] == None and college['location.lon'] == None:
                    null_tuitin_location.append(college)
                else:
                    null_tuition.append(college)
            elif college['location.lat'] == None or college['location.lon'] == None:
                null_location.append(college)
            else:
                whole_data.append(college)

with open('null_tuition_location.txt', 'w') as file:
    json.dump(null_tuitin_location, file, indent=2)

with open('null_tuition.txt', 'w') as file:
    json.dump(null_tuition, file, indent=2)

with open('null_location.txt', 'w') as file:
    json.dump(null_location, file, indent=2)

with open('whole_data.txt', 'w') as file:
    json.dump(whole_data, file, indent=2)
