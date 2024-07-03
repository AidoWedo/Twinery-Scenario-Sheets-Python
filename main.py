import json
import requests

def json_to_twine(json_url, twine_file):
    response = requests.get(json_url)
    data = response.json()

    twine_content = "::Start\n"
    
    # Process Scenario Overview
    for item in data.get("scenarioOverview", []):
        character = item.get("Character", "")
        scene = item.get("Scene", "")
        conversation = item.get("Text/Conversation", "")
        background = item.get("Background/Setting", "")
        twine_content += f"You are {character} in the {scene}. {background}\n\n{conversation}\n\n[[Next->Branch1]]\n\n"
    
    # Process Branch 1
    twine_content += "::Branch1\n"
    for item in data.get("branch1", []):
        scene = item.get("Scene", "")
        conversation = item.get("Text/Conversation", "")
        consequence = item.get("Consequence", "")
        twine_content += f"{scene}\n\n{conversation}\n\n{consequence}\n\n[[Continue->Branch2]]\n\n"
    
    # Process Branch 2
    twine_content += "::Branch2\n"
    for item in data.get("branch2", []):
        scene = item.get("Scene", "")
        conversation = item.get("Text/Conversation", "")
        consequence = item.get("Consequence", "")
        twine_content += f"{scene}\n\n{conversation}\n\n{consequence}\n\n[[Continue->ChoicesAndConsequences]]\n\n"
    
    # Process Choices and Consequences
    twine_content += "::ChoicesAndConsequences\n"
    for item in data.get("choicesAndConsequences", []):
        scene = item.get("Scene", "")
        choice = item.get("Choice", "")
        consequence = item.get("Consequence", "")
        twine_content += f"{scene}\n\nChoice: {choice}\n\nConsequence: {consequence}\n\n[[Next->TryToImprovise]]\n\n"
    
    # Process Try to Improvise
    twine_content += "::TryToImprovise\n"
    for item in data.get("tryToImprovise", []):
        scene = item.get("Scene", "")
        conversation = item.get("Text/Conversation", "")
        consequence = item.get("Consequence", "")
        twine_content += f"{scene}\n\n{conversation}\n\n{consequence}\n\n[[Next->Contemplate]]\n\n"
    
    # Process Contemplate
    twine_content += "::Contemplate\n"
    for item in data.get("contemplate", []):
        scene = item.get("Scene", "")
        conversation = item.get("Text/Conversation", "")
        reflection = item.get("Reflection", "")
        twine_content += f"{scene}\n\n{conversation}\n\nReflection: {reflection}\n\n[[End]]\n\n"
    
    with open(twine_file, 'w') as f:
        f.write(twine_content)

# Example usage
json_url = 'https://script.google.com/macros/s/replace with you url'  # Replace with your actual deployment URL
twine_file = 'scenario.twee'
json_to_twine(json_url, twine_file)
