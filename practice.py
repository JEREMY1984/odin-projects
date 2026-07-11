#open a file called note.txt and append text to it
with open("note.txt","a") as my_file:
    my_file.write("testing inside the room11\n")
    my_file.write("trying to write outside the room")
print( "text written successfully!")
