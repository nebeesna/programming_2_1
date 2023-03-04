import math

memory_size = int(input("Please set memory size: "))
width = int(input("Please set max output width: "))

memory = []  # список з пам'яттю
for i in range(memory_size):
    memory.append('_')
print("Type 'help' for additional info.")
com = ""
block_id = []  # список  <block_id>
block_id_end = []
while com != "exit":
    print("\nChoose command: ")
    command = input()
    str_com = command.split(" ")
    com = str_com[0]

    if com == "help":
        print("""Available commands: 
        help  - show this help
        exit  - exit this program
        print - print memory blocks map
        allocate <num> - allocate <num> cells. Returns block first cell number
        free <num> - free block with first cell number <num>
        """)
        continue

    elif com == "print":
        n = math.ceil(memory_size / width)  # к-сть рядків
        num_len = 0
        in_advance = 0
        for i in range(n):
            for j in range(width):
                if j == 0:
                    if (i * width + j) in block_id:
                        if (i * width + j) in block_id_end:
                            print("\n|" + str(i * width + j) + "|", end='')
                        else:
                            num_len = len(str(i * width + j))
                            print("\n|" + str(i * width + j) + (2 - num_len) * memory[(i * width + j)], end='')
                    elif (i * width + j) in block_id_end:
                        print("\n|" + memory[(i * width + j)] + "|", end='')
                    else:
                        print("\n|" + 2 * memory[i * width + j], end='')
                elif j == width - 1:
                    if (i * width + j) in block_id:
                        # if (i * width + j) in block_id_end:
                        if (i * width + j - 1) in block_id_end:
                            num_len = len(str(i * width + j))
                            print(str(i * width + j) + (2 - num_len) * memory[(i * width + j)] + "|", end='')
                        else:
                            num_len = len(str(i * width + j))
                            print("|" + str(i * width + j) + "|", end='')
                    else:
                        print(2 * memory[(i * width + j)] + "|", end='')
                else:
                    if (i * width + j) in block_id:
                        if (i * width + j) in block_id_end:
                            if (i * width + j - 1) in block_id_end:
                                num_len = len(str(i * width + j))
                                print(str(i * width + j) + "|", end='')
                            else:
                                print("|" + str(i * width + j) + "|", end='')
                        elif (i * width + j - 1) in block_id_end:
                            num_len = len(str(i * width + j))
                            print(str(i * width + j) + (2 - num_len) * memory[(i * width + j)], end='')
                        else:
                            num_len = len(str(i * width + j))
                            if num_len >= 2:
                                print("|" + str(int((i * width + j)/10)), end='')
                                in_advance = (i * width + j) % 10
                            else:
                                print("|" + str(i * width + j), end='')
                    elif (i * width + j - 1) in block_id and in_advance != 0:
                        print(str(in_advance) + memory[(i * width + j)], end='')
                        in_advance = 0
                    elif (i * width + j) in block_id_end:
                        print(memory[(i * width + j)] + "|", end='')
                    elif (i * width + j) == memory_size - 1:
                        print(2 * memory[(i * width + j)] + "|", end='')
                        break
                    else:
                        print(2 * memory[(i * width + j)], end='')
        continue

    elif com == "allocate":
        num_cells = int(str_com[1])
        is_free = False
        for i in range(memory_size):
            if memory[i] == '_' and i + num_cells < memory_size + 1:
                for j in range(num_cells):
                    if memory[j + i] == '_':
                        is_free = True
                    else:
                        is_free = False
                        break
                if is_free:
                    block_id.append(i)
                    block_id_end.append(i + num_cells - 1)
                    block_id.sort()
                    block_id_end.sort()
                    print(i)
                    for j in range(num_cells):
                        memory[i + j] = 'x'
                    break
        if not is_free:
            print("out of range")
        continue

    elif com == "free":
        num_cells = int(str_com[1])
        if block_id.index(num_cells) == len(block_id) - 1:
            for i in range(memory_size - num_cells):
                if memory[i + num_cells] == 'x':
                    memory[i + num_cells] = '_'
                else:
                    break
            block_id_end.remove(block_id_end[block_id.index(num_cells)])
            block_id.remove(num_cells)
        else:
            next_cell = block_id[block_id.index(num_cells) + 1]
            for i in range(next_cell - num_cells):
                if memory[i + num_cells] == 'x':
                    memory[i + num_cells] = '_'
                else:
                    break
            block_id_end.remove(block_id_end[block_id.index(num_cells)])
            block_id.remove(num_cells)
        continue

    elif com == "exit":
        print("Bye!")
        break

    else:
        print("Enter available command!")
