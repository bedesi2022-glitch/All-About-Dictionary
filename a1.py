student_data = {
    "id1": {"name": "Jincy" , "class": "LKG", "Subject_Integration": "English,Math,Science"},

    "id2": {"name": "Rajasthan Royals" , "class": "LKG", "Subject_Integration": "English,Math,Science"},
    "id3": {"name": "Royal Challengers Bengaluru" , "class": "LKG", "Subject_Integration": "English,Math,Science"},
    "id4": {"name": "Jincy" , "class": "LKG", "Subject_Integration": "English,Math,Science"},
}
result = {}
seen_keys = []
for student_id, details in student_data.items():
    unique_key = (details["name"],details["class"],
    details["Subject_Integration"])
if unique_key not in seen_keys:
    seen_keys.append(unique_key)
    result[student_id] = details
for k,v in result.items():
    print(k,":",v)
