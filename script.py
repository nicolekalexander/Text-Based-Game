#import packages
import json #imports json data package
import time #imports time data package
#variables
file_path = "story.json" #variable named file_path stores story.json file
story = open(file_path, "r").read() #variable named story opens and reads story.json file
story_json = json.loads(story) # variable named story_json stores the loaded enchanted forest therapist story
scenes = story_json["scenes"] # variable named scenes with a value of scene attribute being accessed from story_json object
#function definition
def get_intro():
    print(story_json["title"] + " by " + story_json["author"] + "\n")
    time.sleep(2)
    print(story_json["intro"] + "\n")
    time.sleep(2)

def get_scene(scene_id):
    for scene in scenes:
        if (scene["id"] == scene_id):
            print(scene["text"] + "\n")
            time.sleep(3)
            scene_id_choices = []
            for choice in (scene["choices"]):
                scene_id_choices.append(choice["scene_id"])
                print(str(choice["scene_id"]) + ". " + choice["text"])
            time.sleep(2)
            while True:
                try:
                    selected_scene = input("Enter your choice: ")
                    if selected_scene in scene_id_choices:
                        break
                except: 
                    print("Oops. Enter a number.")
                print("That's not one of your options, silly.")    
            get_scene(selected_scene)
#starting game 
get_intro()
get_scene(1)