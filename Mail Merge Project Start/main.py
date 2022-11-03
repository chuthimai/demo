#Create a letter using starting_letter.txt
#for each name in invited_names.txt
with open("../Mail Merge Project Start/Input/Names/invited_names.txt", mode="r") as file_name:
    names = file_name.read()

names = names.split('\n')
with open("../Mail Merge Project Start/Input/Letters/starting_letter.txt") as file_content:
    content = file_content.read()

for name in names:
    with open(f"../Mail Merge Project Start/Output/ReadyToSend/invited_{name}.txt", mode="w") as file:
        content_complete = content.replace("[name]", name)
        file.write(content_complete)
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
