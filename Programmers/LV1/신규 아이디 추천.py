def solution(new_id):

    #1
    new_id = new_id.lower()

    #2
    characters = "~!@#$%^&*()=+[{]}:?,<>/"
    for i in range(len(characters)):
        new_id = new_id.replace(characters[i], "")

    #3 답 봄
    while ".." in new_id:
        new_id = new_id.replace("..", ".")

    #4
    if len(new_id) > 0 and new_id[0] == ".":
        new_id = new_id[1:]
    if len(new_id) > 0 and new_id[-1] == ".":
        new_id = new_id[:-1]

    #5
    if len(new_id) == 0:
        new_id = "a";

    #6
    if len(new_id) > 15:
        new_id = new_id[:15]
    if len(new_id) > 0 and new_id[-1] == ".":
        new_id = new_id[:-1]

    #7
    if len(new_id) <= 2:
        while len(new_id) < 3:
            new_id += new_id[-1]

    answer = new_id
    return answer