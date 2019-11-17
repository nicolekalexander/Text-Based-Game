#import packages
import json
import time

#variables
file_path = "story.json"
story = open(file_path, "r").read()
story_json = json.loads(story)
scenes = story_json["scenes"]

#function definition
def get_scene(scene_id):
    for scene in scenes:
        if (scene["id"] == scene_id):
            print(scene["text"] + "\n")
            time.sleep(3)
            for choice in (scene["choices"]):
                print(str(choice["scene_id"]) + ". " + choice["text"])
            time.sleep(2)
            selected_scene = input("Enter your choice.")
            get_scene(selected_scene)

def get_intro():
    print(story_json["title"] + " by " + story_json["author"] + "\n")
    time.sleep(2)
    print(story_json["intro"] + "\n")
    time.sleep(2)


#starting game
get_intro()
get_scene(1)