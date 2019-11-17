import json


file_path = "story.json"

#variable story that opens and reads whatever file is at the file_path
story = open(file_path, "r").read()
story_json = json.loads(story)
print(story_json["intro"])
