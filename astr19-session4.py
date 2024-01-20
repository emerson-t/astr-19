def main():                       #define main program
    Cat = {                       #name the dictionary/class
        "name"      :    "Cat",
        "arm_L"     :    6.5,     #inches
        "leg_L"     :    10.0,    #inches
        "eyes"      :    2,
        "tail"      :    True,    
        "furry"     :    True     
    }

#print the 
    print("Favorite animal:",Cat["name"])
    print("\nArm length (in):",Cat["arm_L"])
    print("Leg length (in):",Cat["leg_L"])
    print("Number of eyes:",Cat["eyes"])
    print("Has tail:",Cat["tail"])
    print("Is furry:",Cat["furry"])


#if the main() function exists, run it
if __name__ == "__main__":
    main()


#you can add other instructions below
#will be executed after the main() program