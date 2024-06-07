
class File:
    @staticmethod
    def write_file(password, hashed_password):
        with open("passwords.txt", "a") as file:
            file.write(f"Password: {password}, Hashed: {hashed_password}\n")
    @staticmethod
    def read_file():
        with open("problem_solver/file/passwords.txt", "r") as file:
            for line in file:
                line = line.strip()
                if line:
                    parts = line.split(",")
                    if len(parts) != 2:
                        raise ValueError("Invalid line format")
                    hashed_password = parts[1].strip().replace("Hashed: ", "")
                    return hashed_password
        raise ValueError("No password found in file")