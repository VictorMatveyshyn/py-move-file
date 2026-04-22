import os


def move_file(command: str) -> str:

    arguments = command.split()
    if len(arguments) != 3:
        return "Too few parameter(s)"
    if arguments[0] != "mv":
        return "Not a valid command"

    source_file = arguments[1]
    destination_dir = arguments[2].split("/")
    if arguments[2][-1] != "/":
        destination_file = destination_dir.pop()
    else:
        destination_file = source_file

    common_dir = ""

    if len(destination_dir) != 0:
        for directory in destination_dir:
            common_dir = os.path.join(common_dir, directory)
            try:
                os.mkdir(common_dir)
                pass
            except FileExistsError:
                pass

    common_dir = os.path.join(common_dir, destination_file)
    try:
        with (open(source_file, "r") as file_in,
              open(common_dir, "w") as file_out):
            file_out.write(file_in.read())
    except FileNotFoundError as e:
        return str(e)
    except PermissionError as e:
        return str(e)

    os.remove(source_file)
    return (f"File {source_file} has been moved to "
            f"{common_dir}")
