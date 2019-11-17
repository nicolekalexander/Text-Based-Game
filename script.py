import json
import time

file_path = "story.json"
#variable story that opens and reads whatever file is at the file_path
story = open(file_path, "r").read()
story_json = json.loads(story)
scenes = story_json["scenes"]

def get_scene(scene_id):
    for scene in scenes:
        if (scene["id"] == scene_id):
            print(scene["text"] + "\n")
            time.sleep(3)
            print("What are you going to do?")
            time.sleep(2)
            for choice in (scene["choices"]):
                print(str(choice["scene_id"]) + ". " + choice["text"])
            time.sleep(2)
            selected_scene = input("Enter your choice.")
            get_scene(selected_scene)

print(story_json["title"] + " by " + story_json["author"] + "\n")
time.sleep(2)
print(story_json["intro"] + "\n")
time.sleep(2)
get_scene(1)