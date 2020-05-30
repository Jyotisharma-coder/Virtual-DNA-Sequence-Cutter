
#STEP I -  Creating a dictionary of enzymes where key is recognition sequence and value is its enzyme's name.
restriction_enzyme = {'GAATTC':'EcoRI', 'GGATCC':'BamHI', 'AAGCTT':'HindIII', 'TCGA':'TaqI', 'GCGGCCGC':'NotI', 'CAGCTG':'PvuII', 'CCCGGG':'SmaI',  'GGCC': 'HaeIII', 'AGCT':'AluI', 'GATATC':'EcoRV', 'GGTACC':'KpnI', 'CTGCAG':'PstI', 'GAGCTC':'SacI', 'GTCGAC':'SalI', 'AGTACT':'ScaI', 'ACTAGT':'SpeI', 'GCATGC':'SphI', 'AGGCCT':'StuI', 'TCTAGA':'XbaI'}
#STEP II - creating a dictionary for cutting location sites with the recognition site
cutting_location = {'EcoRI': 1 , 'BamHI': 1 , 'HindIII': 1, 'TaqI': 1 , 'NotI': 2, 'PvuII': 3 , 'SmaI': 3, 'HaeIII': 2, 'AluI': 2 , 'EcoRV' : 3 , 'KpnI' : 5 , 'PstI': 5 , 'SacI': 5, 'SalI': 1 , 'ScaI': 3, 'SpeI': 1, 'SphI': 5, 'StuI': 3, 'XbaI': 1}

#location_list = cutting_location.values()
#print(location_list)

def check_for_sequence(input_sequence):
    while input_sequence == "":
        input_sequence = input("Please provide the sequence using A, G, C and T nucleotides from 5' to 3' : ")
    return input_sequence.replace(" ", "")

def enzyme_counter(list, item):
    count = {}
    for item in list:
        if item not in count:
            count[item] = 1
        else:
            count[item] += 1
    return count

# created a dictionary and defined values in form of list.
def cutting_site_cal(j, cutting_location, value):
    for item in cutting_location.keys():
        if item == value :
            location = j + cutting_location[item]
            if item not in cutting_site:
                cutting_site[item] = []
                cutting_site[item].append(location)
            else:
                cutting_site[item].append(location)
    #print(cutting_site)
    return cutting_site

#def ask_user_sequence():

#def get_cutting_location_values(cutting_location,  ):
# Starting the main code.
print("Welcome to Virtual DNA Cutter!")
print("")
#STEP II - Asking user to provide the DNA sequence to be cut.


user_sequence = input("Please provide your DNA sequence from 5' to 3': ").upper()
user_sequence = check_for_sequence(user_sequence)
#user_sequence = 'GAATTCTAGAGCTCTCTAGA'

print("")
#STEP IV - Locate the enzyme site within the sequence and give output as enzyme list.
enzyme_list = []
enzyme_count = {}
cut_location = {}
cutting_site = {}
# Loop 1 - Allows increment for start site to loop over the sequence.
for j in range (0, len(user_sequence)):
    sequence = ""
    status = False  #the status attribute was given to allow break at second loop.
    pattern = user_sequence[j:]
    #Loop 2 - Allows the search for key by adding sequence through the loop.
    for i in range (0, len(pattern)):
        sequence += pattern[i]
        #Loop 3 - Loops through eack key in the dictionary for find for
        for key in restriction_enzyme.keys():
            if sequence == key:
                cut_location = cutting_site_cal(j, cutting_location, restriction_enzyme[key])
                #print(cut_location)
                enzyme_list.append(restriction_enzyme[key])
                enzyme_count = enzyme_counter(enzyme_list,restriction_enzyme[key])
                status = True
        if status == True:
            break
        else:
            pass
#print(cutting_site)

total_enzy_count = []
total_enzy_count = enzyme_count.values()

#STEP V - Providing output to the user with a list of enzymes for them to select in order to cut the sequence.
# counting enzymes and counting the location of each enzyme.
if sum(total_enzy_count) == 0:
    print("Sorry, no restriciton enzyme recognition site found!")
    print("")
    exit()
else:
    print("Total length of your sequence: " + str(len(user_sequence))+" nucleotides.")
    print("")
    print ("Here is the list of " + str(sum(total_enzy_count)) + " restriction enzymes potentially cutting your sequence!")
    for key, value in enzyme_count.items():
        print(value, key, "site"+("" if value == 1 else "s")+" found at location"+("" if len(cutting_site[key]) == 1 else "s")+":", ', '.join(map(str, cutting_site[key])))

#STEP VI - Asking the user for the location/s to be cut for their sequence.
print("")
user_cut_choice = input("Select the location you want to cut (in case for multiple sites, separate by comma): ").replace(" ", "").split(',')
print("")

#print(user_cut_choice)

#STEP VII - Provide the fragments of input DNA sequence as output with their complimentary strand.

start = 0
fragment = 0
for i in range (len(user_cut_choice)):
    fragment += 1
    print("Fragment - ", fragment)
    item = int(user_cut_choice[i])
    print(user_sequence[start:item])
    start = item
fragment += 1
print("Fragment - ", fragment)
print(user_sequence[item:])
