```python
import os

for f in os.listdir("../leetcode"):
    path = f"../leetcode/{f}"
    print(f"Checking path {path}")
    if not os.path.isdir(path):
        continue
    if path == "../scripts":
        continue
    for code_file in os.listdir(path):
        if not code_file.endswith(".py"):
            continue
        full_file_name = path + "/" + code_file
        print(f"Found python code: {full_file_name}")
        with open(full_file_name, "r") as fr:
            code = fr.read()
        with open(path + "/CODE.md", "w") as fw:
            fw.write(f"```python\n{code}\n```\n")
        print(f"Wrote: {path}/CODE.md")
    if os.path.exists(path + "/NOTES.md"):
        print(f"Removing: {path}/NOTES.md")
        os.remove(path + "/NOTES.md")

```
