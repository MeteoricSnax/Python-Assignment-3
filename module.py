def get_population_of_english_and_nonenglish_speaking(look_up_list, year):
    english_speaking = [5100]
    
    print('nr 1 er befolkningstallet for australien, canada, irland, new zealand, storbritannien og usa. nr 2 er resten af verdenen')
    
    population_of_englishspeakers = []
    
    for i in range(len(english_speaking)):
        
        population_of_englishspeakers = look_up_list[np.where((look_up_list[:,3] == english_speaking[i]) & (look_up_list[:,0] == year))]    
    
    population_of_nonenglishspeakers = []
          
    population_of_nonenglishspeakers = look_up_list[(look_up_list[:,0] == year) & (look_up_list[:,3] != english_speaking)]
    
    
    sum_of_englishspeakers = population_of_englishspeakers[:,4].sum()
    
    sum_of_nonenglishspeakers = population_of_nonenglishspeakers[:,4].sum()
    
    return sum_of_englishspeakers, sum_of_nonenglishspeakers

def speaking_a_language(mask, n=None):
    if n:
        all_people_speaking= dd[mask & (dd[:,3]== n)]
    else:
        all_people_speaking= dd[mask]
    
    sum_of_people = all_people_speaking[:,4].sum()
    return sum_of_people

def get_population(look_up_list, land_code, year):
    population = []
    for i in range(len(land_code)):
        population = look_up_list[(look_up_list[:,3] == land_code[i]) & (look_up_list[:,0] == year)]
        
    return population[:,4].sum()

def get_population_from_year(look_up_list, year):
    population = look_up_list[(look_up_list[:,0] == year)]
    print(population)
    return population[:,4].sum()