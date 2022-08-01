import os

for f in os.listdir("../"):
    path = f"../{f}"
    if not os.path.isdir(path):
        continue
    if path == "../scripts":
        continue
    for code_file in os.listdir(path):
        if not code_file.endswith(".py"):
            continue
        full_file_name = path + "/" + code_file
        with open(full_file_name, "r") as fr:
            code = fr.read()
        with open(path + "/CODE.md", "w") as fw:
            fw.write(f"```python\n{code}\n```\n")
    if os.path.exists(path + "/NOTES.md"):
        os.remove(path + "/NOTES.md")