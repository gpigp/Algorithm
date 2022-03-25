def solution(fees, records):

    base_time, base_fee, per_time, per_fee = fees

    time_ = dict()

    while len(records) > 0:
        first_car = records[0].split()
        first_car_num = first_car[1]
        first_car_hour = int(first_car[0][:2])
        first_car_min = int(first_car[0][3:])
        car_index = [0]
        for i, r in enumerate(records[1:]):
            if first_car_num == r.split()[1]:
                car_index.append(i+1)

        car_index_ = car_index
        total_time = 0        
        while len(car_index) > 1:
            hour_ = int(records[car_index[1]].split()[0][:2]) - int(records[car_index[0]].split()[0][:2])
            min_ = int(records[car_index[1]].split()[0][3:]) - int(records[car_index[0]].split()[0][3:])
            if min_ < 0:
                hour_ -= 1
                min_ = 60 + min_
            total_time += (hour_*60) + (min_)
            car_index = car_index[2:]
        else:
            if len(car_index) == 1:
                last_car_hour = int(records[car_index[0]].split()[0][:2])
                last_car_min = int(records[car_index[0]].split()[0][3:])
                total_time += (23-last_car_hour)*60 + (59-last_car_min)

        time_[first_car_num] = total_time

        records = [records[i] for i in range(len(records)) if i not in car_index_]

    time_ = dict(sorted(time_.items()))
    answer = []
    print(time_)
    for t in time_.values():
        total_fee = 0
        if t > base_time:
            add_fee = t-base_time
            print(add_fee)
            if add_fee%per_time == 0:
                total_fee = add_fee/per_time*per_fee
                # print(total_fee)
            else:
                total_fee = (add_fee//per_time+1)*per_fee
                # print(total_fee)
            total_fee += base_fee 
        else:
            total_fee = base_fee
        # print(total_fee)
        answer.append(total_fee)

    return answer