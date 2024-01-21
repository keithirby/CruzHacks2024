# Open the HTML file, read its content, and make changes
with open("test.html", "r") as file:
    content = file.read()

# Make changes to the content as needed (e.g., using string manipulation or regex)
modified_content = content.replace("test", "new_text")

# Save the modified content back to the HTML file
with open("your_file.html", "w") as file:
    file.write(modified_content)