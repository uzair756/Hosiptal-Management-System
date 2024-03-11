# importing pandas
import pandas as pd
# read csv files
patients_table = pd.read_csv("patients_table.csv")
doctors_table = pd.read_csv("doctors_table.csv")
appointment_table = pd.read_csv("appointment_table.csv")

# defining functions for each option

# taking inputs from the user for a new record in the search function
def inputs_add1():
    while True:
        try:
            Patient_ID = int(input(" Enter Patient_ID: "))
            # checking if input id is already present in the table
            # restricts from adding dublicates
            # avoids redundancy
            same_id = patients_table[patients_table['Patient_ID'] == Patient_ID]
            if same_id.empty == False:
                print(" Patient ID already exists, please try again. ")
            else:
                break

        except:
            print(" Invalid input please try again! ")

    while True:
        try:
            Patient_Name = input(" Enter Patient_Name: ")

            break
        except:
            print(" Invalid input please try again! ")

    while True:
        try:
            Age = int(input(" Enter Age: "))

            break
        except:
            print(" Invalid input please try again! ")
    while True:
        try:
            Gender = input(" Enter Gender: ")

            break
        except:
            print(" Invalid input please try again! ")

    while True:
        try:
            Contact = int(input(" Enter Contact number: "))

            break
        except:
            print(" Invalid input please try again! ")
    while True:
        try:
            Day = input(" Enter The Day: ")

            break
        except:
            print(" Invalid input please try again! ")
    while True:
        try:
            Dr_Specialisation = input(" Enter The specialization: ")
            same_specialisation = doctors_table[doctors_table['Dr_Specialisation'] == Dr_Specialisation]
            if same_specialisation.empty == True:
                print(" Invalid input please try again! ")
            else:
                break
        except:
            print(" Invalid input please try again! ")

    return Patient_ID, Patient_Name, Age, Gender, Contact, Day, Dr_Specialisation

def Add_Data(patient_ID, patient_Name, age, gender, contact, day, dr_Specialisation):

    # saving inputs to a dictionary
    dict1 = {'Patient_ID': patient_ID , 'Patient_Name':patient_Name , 'Age': age,
            "Gender": gender, "Contact": contact, 'Day' : day , 'Dr_Specialisation' : dr_Specialisation}
    patients_table.loc[len(patients_table)] = dict1

    # mapping doctor's name and appointment time from the doctor's table into the patient's table
    mapping_Doctor_Name = dict(doctors_table[['Dr_Specialisation','Doctor_Name']].values)
    patients_table['Doctor_Name'] = patients_table['Dr_Specialisation'].map(mapping_Doctor_Name)
    mapping_Time = dict(doctors_table[['Dr_Specialisation','Time']].values)
    patients_table['Appointment_Time'] = patients_table['Dr_Specialisation'].map(mapping_Time)

    # saving record to the patient's table
    patients_table.to_csv("patients_table.csv", index=False)

def Add_Data2(patient_ID):

    # saving inputs to a dictionary
    dict2 = {'Patient_ID': patient_ID}
    appointment_table.loc[len(appointment_table)] = dict2

    # mapping patient's name, doctor's name and appointment time from the patient's table into the appointment's table
    mapping_Patient_Name = dict(patients_table[['Patient_ID','Patient_Name']].values)
    appointment_table['Patient_Name'] = appointment_table['Patient_ID'].map(mapping_Patient_Name)
    mapping_Doctor_Name = dict(patients_table[['Patient_ID','Doctor_Name']].values)
    appointment_table['Doctor_Name'] = appointment_table['Patient_ID'].map(mapping_Doctor_Name)
    mapping_Time = dict(patients_table[['Patient_ID','Appointment_Time']].values)
    appointment_table['Appointment_Time'] = appointment_table['Patient_ID'].map(mapping_Time)

    # saving record to the appointment's table
    appointment_table.to_csv("appointment_table.csv", index=False)

def search_app():
    add_count, search_count, find_count = 0, 0, 0
    again2 = True
    while again2:
        while True:
            try:
                search_id = eval(input(" Enter id of patient to search: "))
                break

            except:
                print(" Invalid input please try again! ")

        output = patients_table[patients_table['Patient_ID'] == search_id]
        search_count += 1

        if output.empty:
            while True:
                error = input(" ID not found! Do you want to add record?:[y/n] ")
                if error.lower() == 'y':

                    # calling inputs_add1 for input from user, then taking values returned as arguement for Add_Data and Add_Data2
                    Patient_ID, Patient_Name, Age, Gender, Contact, Day, Dr_Specialisation = inputs_add1()
                    Add_Data(Patient_ID, Patient_Name, Age, Gender, Contact, Day, Dr_Specialisation)
                    Add_Data2(Patient_ID)

                    # comparing input id with ids from the appointment table
                    # storing the matching record in a variable
                    output2 = appointment_table[appointment_table['Patient_ID'] == Patient_ID]
                    print(
                        "\n *********************************************************** \n           ~ P A T I E N T   R E C O R D   A D D E D ~ \n")
                    print(output2)
                    print("\n *********************************************************** \n")
                    add_count += 1

                error2 = input(" Do you want to search again?:[y/n] ")
                if error2.lower() == 'n':
                    again2 = False
                    print("\n ********************************** \n", search_count, " R E C O R D S   S E A R C H E D")
                    print("", find_count, " R E C O R D S   F O U N D \n", add_count, " R E C O R D S   A D D E D \n \n **********************************")
                    break
                else:
                    break

        else:
            find_count += 1
            print("\n ***************************************************************************************************************** \n                                            ~ P A T I E N T   R E C O R D ~ ")
            print('\n', output ,'\n')
            print(" ***************************************************************************************************************** ")
            againchoice = input(" Do you want to search again?:[y/n] ")
            if againchoice.lower()=="n":
                print("\n ********************************** \n", search_count, " R E C O R D S   S E A R C H E D")
                print("", find_count, " R E C O R D S   F O U N D \n", add_count, " R E C O R D S   A D D E D \n \n **********************************")
                break

def print_table():
    print(patients_table)
    return


# Start of program:

while True:
    while True:
        try:
            print( "\n ***************************************** \n ~ A P P O I N T M E N T   P R O G R A M ~ \n \n (1) Add an Appointment \n (2) Search an Appointment"
            " \n (3) Print Patient's Table \n (4) Exit \n \n ***************************************** ")
            choice1 = eval(input(" E N T E R   Y O U R   C H O I C E :  "))
            print( "\n *****************************************" )

            break
        except:
            print(" Invalid input please try again! ")
    if choice1 == 1:

        # calling inputs_add1 for input from user, then taking values returned as arguement for Add_Data and Add_Data2
        Patient_ID, Patient_Name, Age, Gender, Contact, Day, Dr_Specialisation = inputs_add1()
        Add_Data(Patient_ID, Patient_Name, Age, Gender, Contact, Day, Dr_Specialisation)
        Add_Data2(Patient_ID)

        # comparing input id with ids from the appointment table
        # storing the matching record in a variable
        output2 = appointment_table[appointment_table['Patient_ID'] == Patient_ID]

        print("\n *********************************************************** \n      ~ P A T I E N T   R E C O R D   A D D E D ~ \n")
        print(output2)
        print("\n *********************************************************** ")

    elif choice1 == 2:
        search_app()

    elif choice1 == 3:
        print("\n **************************************************************************************************************** \n                                       ~ P A T I E N T   T A B L E ~  \n")
        print_table()
        print("\n **************************************************************************************************************** ")

    elif choice1 == 4:
        print("\n ******************************************* \n T H A N K   Y O U   A N D   G O O D B Y E ! \n \n *******************************************")
        break

    else:
        print("\n **********************************************")
        print(" Invalid entry. Please enter a number from 1-4. ")
        print("\n **********************************************")        