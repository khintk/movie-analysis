# Khin Kyaw
# Courtney Overland
# Comp 221: Algorithms
# Shilad Sen

# Imports
import math
from random import shuffle

# Number of movie variables
numMovies = 100


def makeEmpty2DArray (num_movies):
    """Function takes the input number of movie in the dataset and makes a 2D array that has movies in rows,
    and the continents in columns."""""
    Empty2DArray = []
    # Loops over the input movie data and appends it to the empty 2Darray
    for i in range(num_movies):
        EmptyArrayMovies = []
        Empty2DArray.append(EmptyArrayMovies)
    return Empty2DArray


# Test Case:
def test_makeEmpty2DArray():

    assert makeEmpty2DArray(1) == [[]]
    assert makeEmpty2DArray(5) == [[], [], [], [], []]
    assert makeEmpty2DArray(10) == [[], [], [], [], [], [], [], [], [], []]
# test_makeEmpty2DArray()


def readfile(empty2DArray):
    """Function takes an empty 2D array and returns a filled 2D array of data from our movie file. The returned
    2D array is a list of strings (with the first item in the list being the name of the movie and the following items being the
    profits from each country, listed alphabetically)"""""
    data_set = open('movie_dataset.tsv','r')
    movie_dataset = data_set.readlines()
    raw2DArray = []
    # Loops through the data (ie. "movie_dataset.tsv" file)
    for movie in movie_dataset:
        # Splits the elements into individual segments to be added to the array
         element = movie.split()
         raw2DArray.append(element)
    return raw2DArray


# Test Case:
def test_readfile():
    empty2DArray = makeEmpty2DArray(100)
    assert readfile(empty2DArray) == [['Captain_America:Civil_War', '0', '190429000', '25200229', '16557300', '41420350', '40802843'], ['Rogue_One:A_Star_Wars_Story', '0', '69484899', '37481197', '11409243', '11409999', '14588970'], ['Finding_Dory', '0', '38052302', '36312640', '9222835', '24781954', '34529711'], ['Zootopia', '0', '235591257', '21369695', '39153348', '17050000', '10675203'], ['The_Jungle_Book', '0', '150140000', '22694801', '20359530', '24351449', '10886275'], ['The_Secret_Life_of_Pets', '0', '58307653', '22428963', '33241623', '22590000', '19065814'], ['Batman_v_Superman:Dawn_of_Justice', '0', '95769365', '22517365', '12683409', '36200000', '36700000'], ['Fantastic_Beasts_and_Where_to_Find_Them', '0', '85963412', '24200000', '24748838', '14400000', '19500000'], ['Deadpool', '0', '0', '33314499', '26002884', '18653169', '20625097'], ['Suicide_Squad', '0', '0', '26126519', '25626359', '27600000', '36600000'], ['Star_Wars_Ep._VII:The_Force_Awakens', '0', '124159138', '67326713', '25952440', '27191173', '27811701'], ['Jurassic_World', '0', '228740000', '38978832', '23420356', '42105404', '29077565'], ['Furious7', '0', '390910000', '33888567', '34016389', '51682039', '46606286'], ['Avengers:Age_of_Ultron', '0', '240110000', '30969152', '34319424', '50940433', '47862465'], ['Minions', '0', '68490000', '23451902', '30015860', '43910109', '37452980'], ['Spectre', '0', '83509789', '25373937', '11584933', '11604067', '8266418'], ['Inside_Out', '0', '15314000', '23400000', '16710083', '31100000', '13938297'], ['Mission:Impossible_Rogue_Nation', '0', '135653541', '11288400', '9940870', '12053845', '9879051'], ['The_Martian', '0', '94932731', '19601155', '17706103', '7759156', '7513748'], ['The_Hunger_Games:Mockingjay_Part2', '0', '21525450', '21422262', '10161646', '20156285', '16890579'], ['Transformers:Age_of_Extinction', '151994', '320000000', '24862352', '45200121', '33534598', '27491390'], ['The_Hobbit:The_Battle_of_the_Five_Armies', '0', '121720000', '27021677', '23962118', '0', '0'], ['Guardians_of_the_Galaxy', '116524', '96470000', '23291983', '37480983', '19648542', '16820519'], ['The_Hunger_Games:Mockingjay_Part1', '0', '36512218', '29791881', '15216903', '23729251', '22463783'], ['Maleficent', '130086', '47720000', '15382553', '37779753', '46172590', '33251828'], ['X-Men:Days_of_Future_Past', '382720', '116490000', '21121336', '22554389', '24581963', '28779414'], ['Captain_America:The_Winter_Soldier', '69744', '115620000', '18390356', '14948380', '25720282', '28319218'], ['The_Amazing_Spider-Man2', '381935', '94430000', '14859113', '20871833', '28460534', '24871027'], ['Dawn_of_the_Planet_of_the_Apes', '90801', '107355317', '17074003', '20640785', '24579285', '24303514'], ['Interstellar', '29198', '121990000', '16971232', '19005801', '5787355', '5059875'], ['Frozen', '167333', '48240000', '26700870', '33436103', '25732202', '0'], ['Iron_Man3', '0', '121200000', '36164486', '44220462', '48566365', '47874596'], ['Despicable_Me2', '39649', '52980000', '32712318', '35110025', '47702364', '35538035'], ['The_Hobbit:The_Desolation_of_Smaug', '0', '74730000', '34565817', '45032050', '18394490', '17821725'], ['The_Hunger_Games:Catching_Fire', '194450', '27920000', '34280264', '23244105', '25157484', '17291146'], ['Fast_and_Furious6', '187041', '66490000', '24693368', '34267107', '35860202', '23027484'], ['Monsters_University', '0', '33720000', '21747029', '20647071', '37608021', '16549029'], ['Gravity', '18411', '70680000', '19580599', '21606484', '17759503', '8823348'], ['Man_of_Steel', '0', '63440000', '22342258', '10424135', '21127388', '16006429'], ['Thor:The_Dark_World', '164215', '55340000', '20494942', '35732140', '23857540', '27751884'], ['The_Avengers', '202368', '0', '54385465', '43677418', '61748523', '63904807'], ['Skyfall', '520651', '0', '49976352', '25243991', '9927335', '14631082'], ['The_Dark_Knight_Rises', '367180', '0', '44179096', '17480637', '31845456', '27097031'], ['The_Hobbit:_An_Unexpected_Journey', '305092', '49730000', '43972634', '43849722', '19184330', '18123942'], ['Ice_Age:Continental_Drift', '91531', '0', '28621749', '50078212', '46845581', '44502217'], ['The_Twilight_Saga:Breaking_Dawn_Part2', '128418', '0', '29891454', '42816364', '29577943', '54249028'], ['The_Amazing_Spider-Man', '313653', '0', '17924071', '21912133', '28742331', '30368653'], ["Madagascar3:Europe's_Most_Wanted", '42738', '0', '25567458', '49354065', '25949927', '28562135'], ['The_Hunger_Games', '65739', '0', '32624716', '13405279', '13913267', '10152708'], ['Men_in_Black3', '211598', '0', '17740460', '0', '16054707', '16225163'], ['Harry_Potter_and_the_Deathly_Hallows:PartII', '0', '0', '51328689', '36817713', '34163720', '35699352'], ['Transformers:Dark_of_the_Moon', '94061', '0', '38820321', '45129718', '30502854', '22312673'], ['Pirates_of_the_Caribbean:On_Stranger_Tides', '0', '0', '29006640', '63661754', '28992018', '30396681'], ['Mission:Impossible—Ghost_Protocol', '107054', '0', '18954599', '12394257', '12997636', '12721841'], ['The_Twilight_Saga:Breaking_Dawn_Part1', '0', '0', '29109682', '31818662', '18856968', '32709793'], ['Kung_Fu_Panda2', '0', '0', '20219645', '31829945', '24391091', '19684571'], ['Fast_Five', '122971', '0', '26794607', '29333777', '25942449', '16679130'], ['The_Hangover_PartII', '0', '0', '35371018', '13262502', '12205269', '16889520'], ['The_Smurfs', '100482', '0', '21457938', '13347700', '21069657', '32849410'], ['Cars2', '0', '0', '20811602', '19915542', '25508290', '16599764'], ['Toy_Story3', '0', '0', '37957715', '6641512', '59382044', '23613926'], ['Alice_in_Wonderland', '38106', '0', '33234316', '42114337', '31347734', '28360362'], ['Harry_Potter_and_the_Deathly_Hallows:PartI', '62336', '0', '41350865', '26306807', '22839997', '23910192'], ['Inception', '106682', '0', '36515403', '21691531', '8919495', '10315556'], ['Shrek_Forever_After', '0', '0', '24485148', '51362770', '28384310', '40037374'], ['The_Twilight_Saga:Eclipse', '47663', '0', '28566737', '26363413', '20600163', '30499010'], ['Iron_Man2', '59572', '0', '22418342', '14762084', '18396680', '15835025'], ['Tangled', '19890', '0', '22555927', '23380205', '14131811', '24341705'], ['Despicable_Me', '0', '0', '21817532', '11143555', '19789795', '13743913'], ['How_to_Train_Your_Dragon', '32008', '0', '16883185', '23460585', '14362388', '11483006'], ['Avatar', '132847', '0', '105779507', '117103251', '44229043', '58218829'], ['Harry_Potter_and_the_Half-Blood_Prince', '80408', '0', '34954004', '18687856', '21185512', '20240271'], ['Ice_Age:Dawn_of_the_Dinosaurs', '47524', '0', '24725499', '44572301', '39389248', '45373371'], ['Transformers:Revenge_of_the_Fallen', '62048', '65837290', '33554033', '18170854', '18895683', '9560181'], ['2012', '175910', '68670540', '18123801', '36608694', '19423924', '25652732'], ['Up', '34845', '0', '25296200', '12073559', '14173033', '10528510'], ['The_Twilight_Saga:New_Moon', '65689', '0', '35164930', '18616430', '18808309', '30613742'], ['Sherlock_Holmes', '79464', '0', '22777578', '16494393', '0', '0'], ['Angels&Demons', '157911', '0', '14065391', '13597356', '13379208', '13858975'], ['The_Hangover', '77103', '0', '17934378', '5220629', '7191582', '8911937'], ['The_Dark_Knight', '50134', '0', '39880001', '8589052', '24966893', '20156555'], ['Indiana_Jones_and_the_Kingdom_of_the_Crystal_Skull', '41357', '0', '27981873', '16876135', '11527839', '13291372'], ['Kung_Fu_Panda', '40511', '26024298', '24764811', '20579860', '22002301', '16379155'], ['Hancock', '187303', '15093944', '19636856', '26059966', '14177721', '13628864'], ['Mamma_Mia!', '20036', '0', '29287446', '9154262', '3133862', '3581745'], ['Madagascar:Escape_2_Africa', '13566', '0', '15093421', '40665152', '16865859', '16949456'], ['Quantum_of_Solace', '283462', '21009412', '20645336', '18054093', '6049052', '7483199'], ['Iron_Man', '49724', '15274332', '18880106', '9386135', '19728577', '14111441'], ['WALL-E', '7971', '0', '14165390', '11694482', '17679805', '6304500'], ['The_Chronicles_of_Narnia:Prince_Caspian', '22088', '0', '13181570', '14770821', '19278912', '7488057'], ['Pirates_of_the_Caribbean:At_World’s_End', '0', '16970000', '29085288', '30850884', '24332139', '0'], ['Harry_Potter_and_the_Order_of_the_Phoenix', '0', '19410000', '29409933', '16326219', '24736826', '0'], ['Spider-Man3', '0', '18924747', '19667403', '13884488', '36846766', '0'], ['Shrek_the_Third', '0', '982214', '28594698', '23049938', '24122638', '0'], ['Transformers', '0', '37218823', '23929895', '15138081', '17976243', '0'], ['Ratatouille', '0', '2871850', '13240587', '10146232', '16103100', '0'], ['I_am_Legend', '0', '0', '0', '0', '0', '0'], ['The_Simpsons_Movie', '0', '0', '26654369', '7655636', '15295868', '0'], ['National_Treasure2:Book_of_Secrets', '0', '0', '11790412', '13627491', '10601378', '0'], ['300', '269928', '0', '12304031', '10040438', '10101034', '0']]
# test_readfile


def convertData(dataset):
    """Function takes our filled 2D array of information (ie. profits per country per movie) and converts the data from
    strings into integers."""""
    processed2DArray = makeEmpty2DArray(101)
    for row in range(100):
        for column in range(7):
            if column == 0:
                processed2DArray[row].append(dataset[row][column])
            else:
                processed2DArray[row].append(int(dataset[row][column]))
    return processed2DArray


# Test Case:
def test_convertData():
    empty2DArray = makeEmpty2DArray(100)
    rawData = readfile((empty2DArray))
    assert convertData(rawData) == [['Captain_America:Civil_War', 0, 190429000, 25200229, 16557300, 41420350, 40802843], ['Rogue_One:A_Star_Wars_Story', 0, 69484899, 37481197, 11409243, 11409999, 14588970], ['Finding_Dory', 0, 38052302, 36312640, 9222835, 24781954, 34529711], ['Zootopia', 0, 235591257, 21369695, 39153348, 17050000, 10675203], ['The_Jungle_Book', 0, 150140000, 22694801, 20359530, 24351449, 10886275], ['The_Secret_Life_of_Pets', 0, 58307653, 22428963, 33241623, 22590000, 19065814], ['Batman_v_Superman:Dawn_of_Justice', 0, 95769365, 22517365, 12683409, 36200000, 36700000], ['Fantastic_Beasts_and_Where_to_Find_Them', 0, 85963412, 24200000, 24748838, 14400000, 19500000], ['Deadpool', 0, 0, 33314499, 26002884, 18653169, 20625097], ['Suicide_Squad', 0, 0, 26126519, 25626359, 27600000, 36600000], ['Star_Wars_Ep._VII:The_Force_Awakens', 0, 124159138, 67326713, 25952440, 27191173, 27811701], ['Jurassic_World', 0, 228740000, 38978832, 23420356, 42105404, 29077565], ['Furious7', 0, 390910000, 33888567, 34016389, 51682039, 46606286], ['Avengers:Age_of_Ultron', 0, 240110000, 30969152, 34319424, 50940433, 47862465], ['Minions', 0, 68490000, 23451902, 30015860, 43910109, 37452980], ['Spectre', 0, 83509789, 25373937, 11584933, 11604067, 8266418], ['Inside_Out', 0, 15314000, 23400000, 16710083, 31100000, 13938297], ['Mission:Impossible_Rogue_Nation', 0, 135653541, 11288400, 9940870, 12053845, 9879051], ['The_Martian', 0, 94932731, 19601155, 17706103, 7759156, 7513748], ['The_Hunger_Games:Mockingjay_Part2', 0, 21525450, 21422262, 10161646, 20156285, 16890579], ['Transformers:Age_of_Extinction', 151994, 320000000, 24862352, 45200121, 33534598, 27491390], ['The_Hobbit:The_Battle_of_the_Five_Armies', 0, 121720000, 27021677, 23962118, 0, 0], ['Guardians_of_the_Galaxy', 116524, 96470000, 23291983, 37480983, 19648542, 16820519], ['The_Hunger_Games:Mockingjay_Part1', 0, 36512218, 29791881, 15216903, 23729251, 22463783], ['Maleficent', 130086, 47720000, 15382553, 37779753, 46172590, 33251828], ['X-Men:Days_of_Future_Past', 382720, 116490000, 21121336, 22554389, 24581963, 28779414], ['Captain_America:The_Winter_Soldier', 69744, 115620000, 18390356, 14948380, 25720282, 28319218], ['The_Amazing_Spider-Man2', 381935, 94430000, 14859113, 20871833, 28460534, 24871027], ['Dawn_of_the_Planet_of_the_Apes', 90801, 107355317, 17074003, 20640785, 24579285, 24303514], ['Interstellar', 29198, 121990000, 16971232, 19005801, 5787355, 5059875], ['Frozen', 167333, 48240000, 26700870, 33436103, 25732202, 0], ['Iron_Man3', 0, 121200000, 36164486, 44220462, 48566365, 47874596], ['Despicable_Me2', 39649, 52980000, 32712318, 35110025, 47702364, 35538035], ['The_Hobbit:The_Desolation_of_Smaug', 0, 74730000, 34565817, 45032050, 18394490, 17821725], ['The_Hunger_Games:Catching_Fire', 194450, 27920000, 34280264, 23244105, 25157484, 17291146], ['Fast_and_Furious6', 187041, 66490000, 24693368, 34267107, 35860202, 23027484], ['Monsters_University', 0, 33720000, 21747029, 20647071, 37608021, 16549029], ['Gravity', 18411, 70680000, 19580599, 21606484, 17759503, 8823348], ['Man_of_Steel', 0, 63440000, 22342258, 10424135, 21127388, 16006429], ['Thor:The_Dark_World', 164215, 55340000, 20494942, 35732140, 23857540, 27751884], ['The_Avengers', 202368, 0, 54385465, 43677418, 61748523, 63904807], ['Skyfall', 520651, 0, 49976352, 25243991, 9927335, 14631082], ['The_Dark_Knight_Rises', 367180, 0, 44179096, 17480637, 31845456, 27097031], ['The_Hobbit:_An_Unexpected_Journey', 305092, 49730000, 43972634, 43849722, 19184330, 18123942], ['Ice_Age:Continental_Drift', 91531, 0, 28621749, 50078212, 46845581, 44502217], ['The_Twilight_Saga:Breaking_Dawn_Part2', 128418, 0, 29891454, 42816364, 29577943, 54249028], ['The_Amazing_Spider-Man', 313653, 0, 17924071, 21912133, 28742331, 30368653], ["Madagascar3:Europe's_Most_Wanted", 42738, 0, 25567458, 49354065, 25949927, 28562135], ['The_Hunger_Games', 65739, 0, 32624716, 13405279, 13913267, 10152708], ['Men_in_Black3', 211598, 0, 17740460, 0, 16054707, 16225163], ['Harry_Potter_and_the_Deathly_Hallows:PartII', 0, 0, 51328689, 36817713, 34163720, 35699352], ['Transformers:Dark_of_the_Moon', 94061, 0, 38820321, 45129718, 30502854, 22312673], ['Pirates_of_the_Caribbean:On_Stranger_Tides', 0, 0, 29006640, 63661754, 28992018, 30396681], ['Mission:Impossible—Ghost_Protocol', 107054, 0, 18954599, 12394257, 12997636, 12721841], ['The_Twilight_Saga:Breaking_Dawn_Part1', 0, 0, 29109682, 31818662, 18856968, 32709793], ['Kung_Fu_Panda2', 0, 0, 20219645, 31829945, 24391091, 19684571], ['Fast_Five', 122971, 0, 26794607, 29333777, 25942449, 16679130], ['The_Hangover_PartII', 0, 0, 35371018, 13262502, 12205269, 16889520], ['The_Smurfs', 100482, 0, 21457938, 13347700, 21069657, 32849410], ['Cars2', 0, 0, 20811602, 19915542, 25508290, 16599764], ['Toy_Story3', 0, 0, 37957715, 6641512, 59382044, 23613926], ['Alice_in_Wonderland', 38106, 0, 33234316, 42114337, 31347734, 28360362], ['Harry_Potter_and_the_Deathly_Hallows:PartI', 62336, 0, 41350865, 26306807, 22839997, 23910192], ['Inception', 106682, 0, 36515403, 21691531, 8919495, 10315556], ['Shrek_Forever_After', 0, 0, 24485148, 51362770, 28384310, 40037374], ['The_Twilight_Saga:Eclipse', 47663, 0, 28566737, 26363413, 20600163, 30499010], ['Iron_Man2', 59572, 0, 22418342, 14762084, 18396680, 15835025], ['Tangled', 19890, 0, 22555927, 23380205, 14131811, 24341705], ['Despicable_Me', 0, 0, 21817532, 11143555, 19789795, 13743913], ['How_to_Train_Your_Dragon', 32008, 0, 16883185, 23460585, 14362388, 11483006], ['Avatar', 132847, 0, 105779507, 117103251, 44229043, 58218829], ['Harry_Potter_and_the_Half-Blood_Prince', 80408, 0, 34954004, 18687856, 21185512, 20240271], ['Ice_Age:Dawn_of_the_Dinosaurs', 47524, 0, 24725499, 44572301, 39389248, 45373371], ['Transformers:Revenge_of_the_Fallen', 62048, 65837290, 33554033, 18170854, 18895683, 9560181], ['2012', 175910, 68670540, 18123801, 36608694, 19423924, 25652732], ['Up', 34845, 0, 25296200, 12073559, 14173033, 10528510], ['The_Twilight_Saga:New_Moon', 65689, 0, 35164930, 18616430, 18808309, 30613742], ['Sherlock_Holmes', 79464, 0, 22777578, 16494393, 0, 0], ['Angels&Demons', 157911, 0, 14065391, 13597356, 13379208, 13858975], ['The_Hangover', 77103, 0, 17934378, 5220629, 7191582, 8911937], ['The_Dark_Knight', 50134, 0, 39880001, 8589052, 24966893, 20156555], ['Indiana_Jones_and_the_Kingdom_of_the_Crystal_Skull', 41357, 0, 27981873, 16876135, 11527839, 13291372], ['Kung_Fu_Panda', 40511, 26024298, 24764811, 20579860, 22002301, 16379155], ['Hancock', 187303, 15093944, 19636856, 26059966, 14177721, 13628864], ['Mamma_Mia!', 20036, 0, 29287446, 9154262, 3133862, 3581745], ['Madagascar:Escape_2_Africa', 13566, 0, 15093421, 40665152, 16865859, 16949456], ['Quantum_of_Solace', 283462, 21009412, 20645336, 18054093, 6049052, 7483199], ['Iron_Man', 49724, 15274332, 18880106, 9386135, 19728577, 14111441], ['WALL-E', 7971, 0, 14165390, 11694482, 17679805, 6304500], ['The_Chronicles_of_Narnia:Prince_Caspian', 22088, 0, 13181570, 14770821, 19278912, 7488057], ['Pirates_of_the_Caribbean:At_World’s_End', 0, 16970000, 29085288, 30850884, 24332139, 0], ['Harry_Potter_and_the_Order_of_the_Phoenix', 0, 19410000, 29409933, 16326219, 24736826, 0], ['Spider-Man3', 0, 18924747, 19667403, 13884488, 36846766, 0], ['Shrek_the_Third', 0, 982214, 28594698, 23049938, 24122638, 0], ['Transformers', 0, 37218823, 23929895, 15138081, 17976243, 0], ['Ratatouille', 0, 2871850, 13240587, 10146232, 16103100, 0], ['I_am_Legend', 0, 0, 0, 0, 0, 0], ['The_Simpsons_Movie', 0, 0, 26654369, 7655636, 15295868, 0], ['National_Treasure2:Book_of_Secrets', 0, 0, 11790412, 13627491, 10601378, 0], ['300', 269928, 0, 12304031, 10040438, 10101034, 0], []]
# test_convertData()


def makeClusters(dataset,numClusters,numMovies):
    """Function takes in our data set which has just been converted from strings to integers, the number of clusters
    we want to make from the data, and the number of movies in the data in total. It works by randomly shuffling the
    data and then assigning each data a cluster based on the remainder value when teh index is divided by the number
    of clusters we are trying to make. In the end the function returns a list of all the clusters."""""
    list_of_clusters = makeEmpty2DArray(numClusters)
    shuffle(dataset)
    for i in range(numMovies):
        index = i % numClusters
        if index == 0:
            list_of_clusters[0].append(dataset[i])
        elif index == 1:
            list_of_clusters[1].append(dataset[i])
        elif index == 2:
            list_of_clusters[2].append(dataset[i])
        elif index == 3:
            list_of_clusters[3].append(dataset[i])
        else:
            list_of_clusters[4].append(dataset[i])
    return list_of_clusters


# Testing Method:

# empty2DArray = makeEmpty2DArray(100)
# rawData = readfile((empty2DArray))
# processedData = convertData(rawData)
# fiveRandomClusters = makeClusters(processedData,5,100)
# print(fiveRandomClusters)

def calculateDistance(movie,centroids,lenColumns):
    """Function takes in all the movies, all the current centroids, and length of the columns in the function, and returns the centroid
    values. It works by using the Euclidean distance to find the length between each movie's data (ie. the profits
    from each continent) and all the centroids."""""
    centroidValues = {}
    centroidIndex = 0
    for centroid in centroids:
        distance = 0
        for index in range(1,lenColumns):
            d = (movie[index] - centroid[index]) * (movie[index] - centroid[index])
            distance = distance + d
        squarerootDistance = math.sqrt(distance)
        centroidValues[centroidIndex] = squarerootDistance
        centroidIndex = centroidIndex + 1
    return centroidValues


#Test Case:
def test_calculateDistance():
    movie = ["x", 0, 1, 2, 3, 4, 5]
    centroids = [["a", 1, 2, 3, 4, 5, 6], ["b", 0, 0, 0, 0, 0, 0], ["c", 1, 1, 1, 1, 1, 1], ["d", 5, 5, 5, 5, 5, 5],
                 ["e", 2, 2, 2, 2, 2, 2]]
    assert calculateDistance(movie,centroids,7) == {0: 2.449489742783178, 1: 7.416198487095663, 2: 5.5677643628300215, 3: 7.416198487095663, 4: 4.358898943540674}
# test_calculateDistance()


def findParentCentroid(centroidValuePairs):
    """Function checks to see which centroid each piece of movie data is closest to. This is used for when we recluster
    and because it determines the new groupings and which cluster each movie data will move to. The centroid which has
    the smallest Euclidean distance from each piece of data (ie. the parent centroid) is returned."""""
    minimum_Value = centroidValuePairs[0]
    parent_Centroid = 0
    current_Centroid = 0
    for index in range(len(centroidValuePairs)):
        if (centroidValuePairs[index]) < minimum_Value:
            minimum_Value = centroidValuePairs[index]
            parent_Centroid = current_Centroid
        current_Centroid = current_Centroid + 1
    return parent_Centroid


#Test Case:
def test_findParentCentroid():
    centroidValuePairs={0:1,1:1,2:3,3:0,4:4}
    assert findParentCentroid(centroidValuePairs) == 3
# test_findParentCentroid()


def calNewCentroid(cluster,num_columns):
    """Function takes in a cluster and the number of columns in the data set and calculates the new location of the centroid
    from the newly composed clusters. It does this by adding all the profit values from each continent from each movie together
    and then dividing by the number of movies in the cluster. This give us an average profit value for each continent which
    used to make a center centroid point."""""
    newcentroid = ["x",0,0,0,0,0,0]

    for row in range(len(cluster)):
        for column in range(1,num_columns):
            newcentroid[column] = newcentroid[column] + cluster[row][column]

    averagecentroid = ["x"]
    for index in range(1,num_columns):
        averagecentroid.append(newcentroid[index]/len(cluster))

    return averagecentroid

# Testing Method:

# empty2DArray = makeEmpty2DArray(100)
# rawData = readfile((empty2DArray))
# processedData = convertData(rawData)
# fiveRandomClusters = makeClusters(processedData,5,100)
# newCentroid = calNewCentroid(fiveRandomClusters[0],7)
# print(newCentroid)


def calculateDistanceCentroids(movie, centroid, numColumns):
    """Function takes in all the movies in our dataset, a centroid, and the number of columns. It then uses the Euclidean
    distance formula to find all the data in the cluster's distance from that specified cluster. This distance
     is returned."""""
    distance = 0
    for index in range(1, numColumns):
        d = (movie[index] - centroid[index]) * (movie[index] - centroid[index])
        distance = distance + d
    squarerootDistance = math.sqrt(distance)
    return squarerootDistance


# Test Case:
def test_calculateDistanceCentroids():
    movie = ["x",1,2,3,4,5,6]
    centroid = ["c",2,3,4,5,6,7]
    assert calculateDistanceCentroids(movie,centroid,7) == 2.449489742783178
# test_calculateDistanceCentroids()


def kmeanValue(cluster, centroid, numColumns):
    """Function takes a cluster, the centroid of that cluster, and the number of columns in that cluster. The goal
    of this function is to calculate the distance between the points in this cluster and it's current centroid. This
    distance is returned."""""
    distance = 0
    for row in range(len(cluster)):
        dataPoint = cluster[row]
        pointDistance = calculateDistanceCentroids(dataPoint,centroid,numColumns)
        distance = distance + pointDistance
    # averageDistance = distance
    return distance

# Testing Method:
# print(kmeanValue(["c",2,3,4,5,6,7],[["a",1,2,3,4,5,6],["b",1,2,3,4,5,6],["c",1,2,3,4,5,6],["d",1,2,3,4,5,6]],7))


def listCentroids(clusters,numcolumn):
    """"Function takes in all the clusters and the number of columns in the dataset
    and returns a list of all the centroids for these clusters. It does this by looping over the clusters and using
    the calNewCentroid method to find the specified centroids and add them to a list."""""
    centroids = []
    # Loop over the cluster
    for cluster in clusters:
        # Calculate the centroid for each cluster
        centroid = calNewCentroid(cluster,numcolumn)
        # Add this centroid to the list
        centroids.append(centroid)
    return centroids

# Testing Method:

# empty2DArray = makeEmpty2DArray(100)
# rawData = readfile((empty2DArray))
# processedData = convertData(rawData)
# fiveRandomClusters = makeClusters(processedData,5,100)
# print(fiveRandomClusters)
# print(listCentroids([[["a",1,2,3,4,5,6]],[["b",3,5,6,1,2,3]]],7))


def reCluster(dataset, listOfCentroids,numclusters,nummovies,numcolumns):
    """"Function takes in the dataset, a list of all the centroids, the number of clusters, the number of movies, and
    the number of columns used in the data. The goal of this function is to regroup the data based on the parent centroids
    (ie. the movie goes to the cluster where it has the smallest distance to the centroid. These new clusters are returned
    in the end. This function uses the findParentCentroid method and depending on the return number from this function,
    the movies will be told which cluster they will be grouped in."""""
    newclusters = makeEmpty2DArray(numclusters)

    for row in range(nummovies):
        distances = calculateDistance(dataset[row], listOfCentroids, numcolumns)
        parent_centroid = findParentCentroid(distances)
        if parent_centroid == 0:
            newclusters[0].append(dataset[row])
        elif parent_centroid == 1:
            newclusters[1].append(dataset[row])
        elif parent_centroid == 2:
            newclusters[2].append(dataset[row])
        elif parent_centroid == 3:
            newclusters[3].append(dataset[row])
        elif parent_centroid == 4:
            newclusters[4].append(dataset[row])
    return dataset

# Testing Method:

# empty2DArray = makeEmpty2DArray(100)
# rawData = readfile((empty2DArray))
# processedData = convertData(rawData)
# fiveRandomClusters = makeClusters(processedData,5,100)
# newCentroid = calNewCentroid(fiveRandomClusters[0],7)
# print(newCentroid)
# print(reCluster(processedData,newCentroid,5,100,7))


def kMean(dataset,old_centroids):
    """Function takes in the dataset and list of old centroid points and returns the average distance of the points from the new centroids which have been
    created when the clusters are remade. The function returns the distance of the points from the centroid."""""
    #Reclusters the movies
    newclusters = reCluster(dataset, old_centroids)
    #Finds the new centroids for these new clusters
    newcentroids=listCentroids(newclusters,7)
    kmeanclusters = []
    index=0
    #Loops through each cluster and finds the distance the centroid moved from the old clustering system to the new system
    for cluster in newclusters:
        kmeaneachcluster = 0
        for movie in cluster:
            distancefromnewcentroid = calculateDistanceCentroids(movie,newcentroids[index],7)
            kmeaneachcluster = kmeaneachcluster + distancefromnewcentroid
        kmeanclusters.append(kmeaneachcluster)
        index = index + 1
    return kmeanclusters


def stopData(oldPointsCentroidsDistance, NewPointsCentroidsDistance):
    """"Function takes in the old centroid point's distance and the new point centroid distance. Because at the beginning we will see
    a significant distance change from new to old centroid point for each cluster, after, the distance will exponentially decrease until
    it hits a plateau point. At some point the changes will become insignifcant, and this function works by checking to see if the distance
    have reached their plateau point."""""
    value = 1
    for i in range(5):
        if(NewPointsCentroidsDistance[i] < oldPointsCentroidsDistance[i]):
            value = value + 1

    if value == 5:
        return True
    else:
        return False

def main():
    emptyArray = makeEmpty2DArray(100)
    raw2DArray = readfile(emptyArray)
    processed2DArray = convertData(raw2DArray)
    RandomClusters = makeClusters(processed2DArray)
    centroids = listCentroids(RandomClusters)

    # calcultes the distance of this distance using kmeans
    kmean = kMean(RandomClusters, centroids)
    stoppingPoint = False
    while stoppingPoint == False:

        #calculates the centroids from the resulting clusters after the first round of kmeans, appends new centroids to list
        new_Cluster = reCluster(RandomClusters, centroids)
        current_centroids = listCentroids(new_Cluster)
        current_kmean = kMean(new_Cluster, current_centroids)
        stopData = stopData(kmean, current_kmean)
        if stopData == False:
            break
        else:
            kmean == current_kmean
    #Finds the kmeans value from the second round of clustering to compare to the first
    current_kmean = kMean(reCluster(RandomClusters, old_centroids), current_centroids)
    stop = stopData(kmean, current_kmean)
    return new_Cluster


#main()
#_________________________________________________________________________


