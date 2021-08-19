import math

with open('input.txt') as f:
    lines = f.readlines()

    start_position = lines[0].split()
    obstacles = lines[1].split()[0]
    commands = lines[1].split()[1]

    print('Start:', start_position)
    print('Obstacles:', obstacles)
    print('Commands:', commands)

    obstacle_list = []

    for i in range(2,12):
        obstacle = lines[i].split()
        obstacle_list.append(obstacle)

    command_list = []

    for i in lines[12:]:
        command = i.split()
        command_list.append(command)


    current_position = [int(start_position[0]), int(start_position[1]), start_position[2]]
    
    def distance(a,b):
        answer = math.sqrt(a**2 + b**2)
        return answer

    max_distance = distance(int(current_position[0]),int(current_position[1]))
    print(max_distance)

    direction = ['N', 'E', 'S', 'W']

    for comm in command_list:
        comm_direction = comm[0]
        if comm_direction == 'R':
            current_dir = current_position[2]
            if current_dir == 'N':
                current_dir = 'E'
            elif current_dir == 'E':
                current_dir = 'S'
            elif current_dir == 'S':
                current_dir = 'W'
            else:
                current_dir = 'N'

            current_position[2] = current_dir

        elif comm_direction == 'L':
            current_dir = current_position[2]
            if current_dir == 'N':
                current_dir = 'W'
            elif current_dir == 'E':
                current_dir = 'N'
            elif current_dir == 'S':
                current_dir = 'E'
            else:
                current_dir = 'S'

            current_position[2] = current_dir

        else:
            steps = int(comm[1])
            current_dir = current_position[2]

            if current_dir == 'N':
                

                for obs in obstacle_list:
                    obs = [int(obs[0]), int(obs[1])]
                    if (int(obs[0]) == int(current_position[0])) and (obs[1] > int(current_position[1])) and (steps > abs(obs[1]-int(current_position[1]))):
                        current_position[1] = obs[1] - 1
                        break
                    else:
                        new_y = int(current_position[1]) + steps
                        current_position[1] = new_y
                        break
            elif current_dir == 'E':
                

                for obs in obstacle_list:
                    obs = [int(obs[0]), int(obs[1])]
                    if (obs[1] == current_position[1]) and (obs[0] > current_position[0]) and (steps > abs(obs[0]-current_position[0])):
                        current_position[0] = obs[0] - 1
                        break
                    else:
                        new_x = int(current_position[0]) + steps
                        current_position[0] = new_x
                        break
            elif current_dir == 'S':
                

                for obs in obstacle_list:
                    obs = [int(obs[0]), int(obs[1])]
                    if (obs[0] == current_position[0]) and (obs[1] < current_position[1]) and (steps > abs(obs[1]-current_position[1])):
                        current_position[1] = obs[1] + 1
                        break
                    else:
                        new_y = int(current_position[1]) - steps
                        current_position[1] = new_y
                        break
            else:
                
                for obs in obstacle_list:
                    obs = [int(obs[0]), int(obs[1])]
                    if (obs[1] == current_position[1]) and (obs[0] < current_position[0]) and (steps > abs(obs[0]-current_position[0])):
                        current_position[0] = obs[0] + 1
                        break
                    else:
                        new_x = int(current_position[0]) - steps
                        current_position[0] = new_x
                        break
            
            current_distance = distance(int(current_position[0]), int(current_position[1]))
            if current_distance > max_distance:
                max_distance = current_distance

        

    print(round(max_distance,2))



