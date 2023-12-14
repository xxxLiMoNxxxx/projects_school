
current_weight = 0
kg_max = 530
current_people = 0
people_max = 7

for i in range(7):
    
    
  weight = int(input("Введіть масу першого чоловіка: "))
  if (current_weight + weight <= kg_max):
    if (current_people + 1 <= people_max):
      current_people+=1
      current_weight+=weight
      weight = int(input("Введіть масу другого чоловіка: "))
      if (current_weight + weight <= kg_max):
        if (current_people + 1 <= people_max):
          current_people+=1
          current_weight+=weight
          weight = int(input("Введіть масу третього чоловіка: "))
          if (current_weight + weight <= kg_max):
            if (current_people + 1 <= people_max):
              current_people+=1
              current_weight+=weight
              weight = int(input("Введіть масу четвертого чоловіка: "))
              if (current_weight + weight <= kg_max):
                if (current_people + 1 <= people_max):
                  current_people+=1
                  current_weight+=weight
                  weight = int(input("Введіть масу п`ятого чоловіка: "))
                  if (current_weight + weight <= kg_max):
                    if (current_people + 1 <= people_max):
                      current_people+=1
                      current_weight+=weight
                      weight = int(input("Введіть масу шостого чоловіка: "))
                      if (current_weight + weight <= kg_max):
                        if (current_people + 1 <= people_max):
                          current_people+=1
                          current_weight+=weight
                          weight = int(input("Введіть масу сьомого чоловіка: "))
                          if (current_weight + weight <= kg_max):
                            if (current_people + 1 <= people_max):
                              current_people+=1
                              current_weight+=weight
                              print("В ліфт зайшло максимум людей!")
                              break
                              if (current_people>=people_max):
                                print("Ліфт не поїде")
                                break
                              elif (current_weight + weight >= kg_max):
                                print("Ліфт не поїде")
                                break
                            elif (current_people + 1 >= people_max):
                              print("Ліфт не поїде")
                              break
                          elif (current_weight + weight >= kg_max):
                            print("Ліфт не поїде")
                            break
                        elif (current_people + 1 >= people_max):
                          print("Ліфт не поїде")
                          break
                      elif (current_weight + weight >= kg_max):
                        print("Ліфт не поїде")
                        break
                    elif (current_people + 1 >= people_max):
                      print("Ліфт не поїде")
                      break
                  elif (current_weight + weight >= kg_max):
                    print("Ліфт не поїде")
                    break
                elif (current_people + 1 >= people_max):
                  print("Ліфт не поїде")
                  break
              elif (current_weight + weight >= kg_max):
                print("Ліфт не поїде")
                break
            elif (current_people + 1 >= people_max):
              print("Ліфт не поїде")
              break
          elif (current_weight + weight >= kg_max):
            print("Ліфт не поїде")
            break
        elif (current_people + 1 >= people_max):
          print("Ліфт не поїде")
          break
      elif (current_weight + weight >= kg_max):
        print("Ліфт не поїде")
        break
    elif (current_people + 1 >= people_max):
      print("Ліфт не поїде")
      break
  elif (current_weight + weight >= kg_max):
    print("Ліфт не поїде")
    break