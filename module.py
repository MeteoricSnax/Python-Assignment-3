import numpy as np

def get_from_csv(file_name):
    return np.genfromtxt(file_name, delimiter=',', dtype=np.uint, skip_header=1)

def speaking_a_language(dd, mask, n=None):
    if n:
        all_people_speaking = dd[mask & (dd[:,3] == n)]
    else:
        all_people_speaking = dd[mask]
    
    sum_of_people = all_people_speaking[:,4].sum()
    return sum_of_people

def get_english_and_non_speakers(dd):
    english_speaking_country = {1: 5314, 2: 5390, 3: 5502, 4: 5514, 5: 5170, 6: 5142}
    mask = ((dd[:,0]== 2015))
    english = np.array([speaking_a_language(dd, mask, statecode)for statecode in english_speaking_country.values()])
    return english.sum(), (speaking_a_language(dd, mask) - english.sum())

def get_population_from_mask(dd, mask):
    population = dd[mask]
    return population[:,4].sum()

def get_population_from_year(look_up_list, year):
    population = look_up_list[(look_up_list[:,0] == year)]
    return population[:,4].sum()

def x_values_sum(data , column_name_number):
    a_data_dict ={}
    for year in np.unique(data[:,column_name_number]):
        mask = (data[:,0]==year)
        a_data_dict[year] = sum(data[mask][:,4])
    return a_data_dict

def get_amount_of_age(data, mask):
    dataset = data[mask]
    amount = {}
    for i in range(len(dataset)):
        if dataset[i, 2] in amount:
            amount[dataset[i, 2]] += dataset[i, 4]
        else:
            amount[dataset[i, 2]] = dataset[i, 4]
    return amount

def mask_maker(dd, age_min, age_max, area):
    mask = ((dd[:,0] == 2015) & (dd[:,2] >= age_min) & (dd[:,2] <= age_max) & (dd[:,1] == area))
    return mask

def get_amount(dd, max_age_of_area, area_number):
    loop_times = int((max_age_of_area / 10) + 1)
    final_amount = {}
    area = area_number
    for i in range(loop_times):
        min_age = i*10
        max_age = (i*10)+10
        temp_mask = mask_maker(dd, min_age, (min_age +9), area)
        temp_amount = get_amount_of_age(dd, temp_mask)
        temp_key = str(min_age) + "-" + str(max_age)
        temp_value = 0
        for i in temp_amount:
            temp_value += temp_amount[i]
        final_amount[temp_key] = temp_value
    return final_amount
