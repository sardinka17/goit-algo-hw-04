def get_cats_info(path):
    cats_list = []
    
    try:
        with open(path, "r", encoding="utf-8") as cats:
            while True:
                line = cats.readline()
                
                if not line:
                    break

                id, name, age = line.replace("\n", "").split(",")
                cat_info_dict = {"id": id, "name": name, "age": age}
                cats_list.append(cat_info_dict)
    except FileNotFoundError:
        print(f"{path} file is not found.")
    except IOError:
        print(f"{path} file is corrupted.")

    return cats_list
