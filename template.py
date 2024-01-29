import os

dirs=[
   os.path.join("data","raw"),
   os.path.join("data","processed"),
   "notebooks",
   "saved_models",
   "src",
   "data_given",
]

for dir_ in dirs:
    os.makedirs(dir_,exist_ok=True)
    with open(os.path.join(dir_,".gitkeep"),"w") as f:
        pass
file_=[
     "dvc.yaml",
     "params.yaml",
     ".gitignore",
     os.path.join("src","__init__.py"),
    #  "README.md",
]

for files in file_:
    with open(files,"w") as f:
        pass