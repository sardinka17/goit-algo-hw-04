def total_salary(path):
    total = 0
    average = 0
    salaries_dict = dict()

    try:
        with open(path, "r", encoding="utf-8") as salaries:
            while True:
                line = salaries.readline()

                if not line:
                    break

                name, salary = line.replace("\n", "").split(",")
                salaries_dict[name] = int(salary)
        
        for value in salaries_dict.values():
            total += value
    
        average = total // len(salaries_dict.keys())
    except FileNotFoundError:
        print(f"{path} file was not found.")
    except IOError:
        print(f"{path} file is corrupted.")
    
    return (total, average)
