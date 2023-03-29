import random
import time
import emoji
import sys
import os
import pickle
menu = 1
while menu==1:
  print(('\n              '),end = ''),print('Arena'+emoji.emojize(':stadium:'),end = ''),print('              ')
  gra1 = int(input('\n1 - Nowa gra'+emoji.emojize(':crossed_swords:', language='alias')+'\n2 - Wczytaj gre'+emoji.emojize(':scroll:', language='alias')+'\n3 - Informacje'+emoji.emojize(':blue_book:', language='alias')+'\n4 - Wyjscie'+emoji.emojize(':cross_mark:', language='alias')+'\n=>'))
  if gra1 == 1:
    akthp = 100
    maxhp = 100
    zloto = 50
    poziom = 1
    exp = 0
    maxexp = 100
    mikstury = 2
    ilosc_trucizn = 0
    ilosc_mieczy = 0
    obrazeniaD = 0
    obrazeniaT = 0
    obrazeniaW = 0
    zbroja = 0
    tarcza = 0
    miecz = 0
    mieszkanie = 0
    trofeum1 = 0
    trofeum2 = 0
    trofeum3 = 0
    trofeum4 = 0
    trofeum5 = 0
    jaszczur = 0
    break
  elif gra1 == 2:
    with open("zapis.pkl", "rb") as f:
        akthp = pickle.load(f)
        maxhp = pickle.load(f)
        zloto = pickle.load(f)
        poziom = pickle.load(f)
        exp = pickle.load(f)
        maxexp = pickle.load(f)
        mikstury = pickle.load(f)
        ilosc_trucizn = pickle.load(f)
        ilosc_mieczy = pickle.load(f)
        obrazeniaD = pickle.load(f)
        obrazeniaT = pickle.load(f)
        obrazeniaW = pickle.load(f)
        zbroja = pickle.load(f)
        tarcza = pickle.load(f)
        miecz = pickle.load(f)
        mieszkanie = pickle.load(f)
        trofeum1 = pickle.load(f)
        trofeum2 = pickle.load(f) 
        trofeum3 = pickle.load(f)
        trofeum4 = pickle.load(f)
        trofeum5 = pickle.load(f)
        jaszczur = pickle.load(f)
    break
  elif gra1 ==3:
    info = int(input('1 - O grze\n2 - Instrukcje\n3 - Powrot\n=>'))
    if info==1:
      print('Wykonal Hubert Jedruchniewicz\nCzas pracy: ~45 godzin')
      continue
    elif info==2:
      print('Tawerna\n-Mozesz tam spac (potrzebna losowa ilosc zlota,losowa regeneracja zycia)\n-U handlarza kupujesz i sprzedajesz przedmioty (Miecz - im drozszy tym wiecej obrazen zadaje,Tarcza - mozliwosc zablokowania jednego ataku przeciwnika,')
      print('Ulepszenie zbroi - na stale dodaje 5 maksymalnego HP,Sprzedaz miecza - zyskujesz 20 szt. zlota niezaleznie od rodzaju miecza)')
      print('Namiot medyka\n-Opatrzenie ran (zwieksza ilosc aktualnego HP)\n-Zakupy u medyka (Mikstura - moze przywrocic HP w trakcie walki,Trucizna - po rzuceniu zadaje obrazenia w kazdej rundzie)')
      print('Sklep wiedzmy\n-Magiczne stwory pomagajace w walce (Ognik - na stale ulepsza twoje piesci lub miecz,Jaszczur - towarzyszy ci podczas walk,zadaje dodatkowe obrazenia w kazdej rundzie)')
      print('Przydatna rada - kazda runda obejmuje atak twojego bohatera i atak przeciwnika (wiec mimo ze np. oboje posiadacie malo HP, to po twoim ataku walke wygra przeciwnik)')
      print('Wniosek: aby wygrac walke musisz posiadac na tyle duzo HP, zeby po zakonczeniu rundy zostalo ci jeszcze przynajmniej 1 HP')
      continue
    elif info==3:
      continue
    else:
      print('Podano niewlasciwa liczbe')
      continue                                                              
  elif gra1 == 4:
    sys.exit()
  else:
    print('Podano niewlasciwa liczbe')
    continue
while akthp>0 or zloto>0:
       print('\nAktualne statystyki:\nPoziom: '+str(poziom)+' ('+str(exp)+'/'+str(maxexp)+') EXP'+emoji.emojize(':purple_circle:', language='alias')+'\nHP: '+str(akthp)+'/'+str(maxhp)+emoji.emojize(':red_heart:', language='alias')+'\nZloto: '+str(zloto)+emoji.emojize(':money_bag:', language='alias')+'\nMikstury: ' +str(mikstury)+emoji.emojize(':fire_extinguisher:', language='alias')+'\nTrucizna: '+str(ilosc_trucizn)+emoji.emojize(':test_tube:', language='alias')+'\nTarcza: '+str(tarcza)+emoji.emojize(':shield:', language='alias'))
       print(('Miecz: '),end='')
       if miecz== 0:
         print('brak'+'\U0001f5e1')
       elif miecz== 1:
         print('Zelazny miecz'+'\U0001f5e1')
       elif miecz== 2:
         print('Srebrny miecz'+'\U0001f5e1')
       elif miecz== 3:
         print('Mistrzowski miecz'+'\U0001f5e1')
       elif miecz== 4:
         print('Magiczny miecz'+'\U0001f5e1')
       elif miecz== 5:
         print('Starozytny miecz'+'\U0001f5e1')
       elif miecz== 6:
         print('Boski miecz'+'\U0001f5e1')
       else: exit
       print('\nWybierz miejsce podrozy:')
       docelowe = int(input('1 - Tawerna'+emoji.emojize(':houses:', language='alias')+'\n2 - Namiot medyka'+emoji.emojize(':camping:', language='alias')+'\n3 - Arena'+emoji.emojize(':stadium:', language='alias')+'\n4 - Rynek miasta'+emoji.emojize(':castle:', language='alias')+'\n5 - Zapisz gre'+emoji.emojize(':scroll:', language='alias')+'\n6 - Wyjscie z gry'+emoji.emojize(':cross_mark:', language='alias')+'\n=>'))
       if docelowe == 1:
        print('\nTawerna'+emoji.emojize(':beer:', language='alias')+'\nWybierz aktywnosc:')
        tawerna = int(input('1 - Przespij sie'+emoji.emojize(':last_quarter_moon_face:', language='alias')+'\n2 - Handlarz'+emoji.emojize(':person_in_tuxedo:', language='alias')+'\n3 - Wyjscie'+emoji.emojize(':cross_mark:', language='alias')+'\n=>'))
        if tawerna==1 and zloto>=12 and akthp!=maxhp:
          akthp += random.randint(5,90)
          oplata = random.randint(5,12)
          zloto-=oplata
          print('\n'+emoji.emojize(':bed:', language='alias'),end =''),time.sleep(0.6),print(('\U0001f4a4'),end = ''),time.sleep(0.6),print(('\U0001f4a4'),end = ''),time.sleep(0.6),print(('\U0001f4a4'),end = ''),time.sleep(0.6),print('\U0001f4a4'),time.sleep(0.6)
          if akthp>maxhp:
            akthp = akthp-(akthp-maxhp)
            continue
          else:
            continue
        elif tawerna == 1 and akthp == maxhp and zloto>=12:
          print('Masz maksymalna liczbe HP')
          continue
        elif tawerna == 1 and zloto<12:
          print('Masz za malo pieniedzy')
          continue
        elif tawerna==2:
          handlarz =int(input('\nHandlarz\nWybierz przedmiot:\n1 - Zelazny miecz - 25 szt. zlota\n2 - Srebrny miecz - 50 szt. zlota\n3 - Mistrzowski miecz - 100 szt. zlota\n4 - Ulepszenie zbroi - 10 szt. zlota\n5 - Tarcza - 10 szt. zlota\n\nSprzedaz:\n6 - Sprzedaj miecz\n\n7 - Wyjscie'+emoji.emojize(':cross_mark:', language='alias')+'\n=>'))
          if handlarz == 1 and ilosc_mieczy==0 and zloto>=25:
            obrazeniaD = 2
            zloto-=25
            ilosc_mieczy += 1
            miecz = 1
            print('Zakupiono Zelazny miecz')
            continue
          elif handlarz == 2 and ilosc_mieczy==0 and zloto>=50:
            obrazeniaD = 5
            zloto-=50
            ilosc_mieczy += 1
            miecz = 2
            print('Zakupiono Srebrny miecz')
            continue
          elif handlarz == 3 and ilosc_mieczy==0 and zloto>=100:
            obrazeniaD = 11
            zloto-=100
            ilosc_mieczy += 1
            miecz = 3
            print('Zakupiono Mistrzowski miecz')
            continue
          elif handlarz == 4 and zloto>=10 and zbroja<10:
            maxhp += 4
            akthp += 4
            zloto -= 10
            zbroja += 1
            print('Zakupiono Uleszenie zbroi')
            continue
          elif (handlarz == 1 or handlarz == 2 or handlarz == 3) and ilosc_mieczy==1:
            print('Posiadasz juz miecz. Sprzedaj go, aby zakupic inny')
            continue
          elif handlarz ==  4 and zbroja == 10:
            print('Posiadasz maksymalne ulepszenie zbroi')
            continue
          elif handlarz == 6 and ilosc_mieczy == 1:
            print('Sprzedano aktualnie uzywany miecz')
            obrazeniaD = 0
            zloto += 20
            ilosc_mieczy -= 1
            miecz = 'brak'
            continue
          elif handlarz == 6 and ilosc_mieczy == 0:
            print('Nie posiadasz miecza')
            continue
          elif handlarz == 5 and tarcza<1 and zloto >=10:
            print('Zakupiono tarcze')
            zloto -= 10
            tarcza += 1
            continue
          elif handlarz == 5 and tarcza>=1:
            print('Posiadasz juz tarcze')
            continue
          elif handlarz == 7:
            continue
          else: print('Podano niewlasciwa liczbe lub masz za malo zlota')
          continue
        elif tawerna == 3:
          continue
        elif tawerna == 1 and zloto < 10:
          print('Masz za malo zlota zeby przespac sie w tawernie')
        else: print('Podano niewlasciwa liczbe')
        continue
       elif docelowe == 2:
        print('\nNamiot Medyka\nWybierz aktywnosc:')
        medyk = int(input('1 - Opatrz rany'+emoji.emojize(':adhesive_bandage:', language='alias')+'\n2 - Kup mikstury'+emoji.emojize(':elf:', language='alias')+'\n3 - Wyjscie'+emoji.emojize(':cross_mark:', language='alias')+'\n=> '))
        if medyk == 1:
          usluga =int(input('Wybierz usluge:\n1 - Podstawowy opatrunek (+20 HP) - 5 szt. zlota\n2 - Zatrzymanie krwawienia (+45 HP) - 10 szt. zlota\n3 - Usztywnienie zlamania (+90 HP) - 20 szt. zlota\n4 - Wyjscie'+emoji.emojize(':cross_mark:', language='alias')+'\n=>' ))
          if usluga == 1 and akthp<=(maxhp-20) and zloto>=5:
            akthp += 20
            zloto -= 5
            print('Zakupiono Podstawowy opatrunek')
            continue
          elif usluga == 2 and akthp<=(maxhp-45) and zloto>=10:
            akthp += 45
            zloto -= 10
            print('Zakupiono usluge zatrzymania krwawienia')
            continue
          elif usluga == 3 and akthp<=(maxhp-92) and zloto>=20:
            akthp += 92
            zloto -= 20
            print('Zakupiono usluge usztywnienia zlamania')
            continue
          elif usluga == 1 and akthp>(maxhp-20) and zloto>=5:
            print("Nie jestes tak powaznie ranny")
            continue
          elif usluga == 2 and akthp>(maxhp-45) and zloto>=10:
            print("Nie jestes tak powaznie ranny")
            continue
          elif usluga == 3 and akthp>(maxhp-92) and zloto>=20:
            print("Nie jestes tak powaznie ranny")
            continue
          elif usluga == 4:
            continue
          else: print('Podano niewlasciwa liczbe lub masz za malo zlota')
        elif medyk == 2:
          sklepMedyk =int(input('Wybierz miksture:\n1 - Mikstura podstawowa (+15 HP) - 5 szt. zlota\n(Podstawowe leczenie w trakcie walki. Ograniczona ilosc w ekwipunku : 2)\n2 - Trucizna - 7 szt. zlota\n(Po uzyciu w trakcie walki zadaje przeciwnikowi obrazenia rowne: 3 co runde.)\n3 - Wyjscie'+emoji.emojize(':cross_mark:', language='alias')+'\n=>) '))
          if sklepMedyk == 1 and mikstury<2:
            mikstury += 1
            zloto -= 5
            print('Zakupiono miksture')
            continue
          elif sklepMedyk == 1 and mikstury>=2 and zloto>=5:
            print('Posiadasz maksymalna liczbe mikstur')
            continue
          elif sklepMedyk == 2 and zloto>=7:
            ilosc_trucizn += 1
            zloto -= 7
            print('Zakupiono trucizne')
            continue
          elif sklepMedyk == 3:
            continue
          else: print('Podano niewlasciwa liczbe lub masz za malo zlota')
        elif  medyk == 3:
          continue
        else: print('Podano niewlasciwa liczbe')
       elif docelowe == 3:
        arena = int(input('\nArena\n\nWybierz arene:\n1 - Arena Treningowa'+emoji.emojize(':star:', language='alias')+'(Poziom 1-3)\n2 - Arena Poczatkujacych'+emoji.emojize(':star::star:', language='alias')+'(Poziom 4-9)\n3 - Arena Wojownikow'+emoji.emojize(':star::star::star:', language='alias')+'(Poziom 10-15)\n4 - Arena Mistrzowska'+emoji.emojize(':trophy:', language='alias')+'(Poziom 16-21)\n5 - Arena Krolewska'+emoji.emojize(':crown:', language='alias')+' (Poziom 22+)\n6 - Wyjscie'+emoji.emojize(':cross_mark:', language='alias')+'\n=>'))
        if arena == 1:
          wrog1 = int(input('Wybierz przeciwinika:\n(Sortowane od najprostszego do najtrudniejszego)\n1 - Jednoreki bandyta'+emoji.emojize(':person_pouting:', language='alias')+'\n2 - Wilk'+emoji.emojize(':wolf:', language='alias')+'\n3 - Pijany kowal'+emoji.emojize(':old_man:', language='alias')+'\n4 - Wyjscie\n=>'))
          if wrog1 == 1:
            runda = 1
            hp1 = 40
            mhp = 40
            oexp = 25
            ozloto = 10
            obrazeniaT = 0
            nazwa1 = 'Jednoreki bandyta'
            ap1 = random.randint(5,7)
            while hp1>0 and akthp>0:
              print('\nRunda '+str(runda))
              print('\nAktualne statystyki:\nHP: '+str(akthp)+'/'+str(maxhp)+'\nMikstury: ' +str(mikstury)+'\nTrucizna: '+str(ilosc_trucizn)+'\nTarcza: '+str(tarcza))
              ruch = int(input('\nWrog: ' +str(nazwa1)+'\nHP: '+str(hp1)+'/'+str(mhp)+'\n\nWybierz akcje:\n1 - Atakuj'+emoji.emojize(':fist:', language='alias')+'\n2 - Wypij miksture'+emoji.emojize(':fire_extinguisher:', language='alias')+'\n3 - Rzuc trucizne'+emoji.emojize(':test_tube:', language='alias')+'\n4 - Uciekaj'+emoji.emojize(':leg:', language='alias')+'\n=>'))
              if ruch == 1:
                hp1 -= (random.randint(6,10)+obrazeniaD+obrazeniaT+obrazeniaW)
                print('Wykonujesz atak\n')
                print(emoji.emojize(':man:', language='alias'),end = ''),time.sleep(0.6),print('\U0001f5e1',end = ''),time.sleep(0.6),print(emoji.emojize(':person_pouting:', language='alias'),end = ''),print(emoji.emojize(':collision:', language='alias'),end = ''),time.sleep(0.6)
                print('\n\nRuch przeciwnika\n')
                if tarcza == 1:
                  uTarczy = int(input('Uzyc tarczy?\n1 - Tak\n2 - Nie\n=>'))
                  if uTarczy == 1:
                    print(emoji.emojize(':man:', language='alias'),end = ''),print(emoji.emojize(':shield:'),end = ''),time.sleep(0.6),print(emoji.emojize(':hammer:', language='alias'),end = ''),print(emoji.emojize(':person_pouting:', language='alias'),end = ''),time.sleep(0.6),print(emoji.emojize(':red_question_mark:', language='alias')),time.sleep(0.6)
                    runda += 1
                    tarcza -= 1
                    continue
                  else:
                   akthp -= ap1
                   print(emoji.emojize(':man:', language='alias'),end = ''),time.sleep(0.6),print(emoji.emojize(':collision:'),end = ''),print(emoji.emojize(':hammer:', language='alias'),end = ''),print(emoji.emojize(':person_pouting:', language='alias')),time.sleep(0.6)
                   runda += 1
                   continue
                else:
                  akthp -= ap1
                  print(emoji.emojize(':man:', language='alias'),end = ''),time.sleep(0.6),print(emoji.emojize(':collision:'),end = ''),print(emoji.emojize(':hammer:', language='alias'),end = ''),print(emoji.emojize(':person_pouting:', language='alias')),time.sleep(0.6)
                  runda += 1
                  continue
              elif ruch == 2 and mikstury>=1 and akthp<=(maxhp-15):
                akthp += 15
                mikstury -= 1
                print('Pijesz miksture\n')
                print(emoji.emojize(':man:', language='alias'),end = ''),print(emoji.emojize(':fire_extinguisher:', language='alias'),end = ''),time.sleep(0.6),print(emoji.emojize(':anger:', language='alias')),time.sleep(0.6)
                continue
              elif ruch == 2 and mikstury<1:
                print('Nie posiadasz mikstur')
                continue
              elif ruch == 2 and mikstury>=1 and akthp>(maxhp-15):
                print('Masz za duzo HP, nie mozesz wypic mikstury')
                continue
              elif ruch == 3 and ilosc_trucizn>=1:
                obrazeniaT += 3
                ilosc_trucizn -=1
                print(emoji.emojize(':man:', language='alias'),end = ''),time.sleep(0.6),print(emoji.emojize(':dashing_away:'),end = ''),time.sleep(0.6),print(emoji.emojize(':dashing_away:', language='alias'),end = ''),time.sleep(0.6),print(emoji.emojize(':test_tube:', language='alias'),end = ''),print(emoji.emojize(':collision:', language='alias'),end = ''),print(emoji.emojize(':person_pouting:', language='alias')),time.sleep(0.6)
                continue
              elif ruch == 3 and ilosc_trucizn<1:
                print('Nie posiadasz trucizn')
                continue
              elif ruch == 4:
                print('Uciekasz z areny\nWidownia nasmiewa sie z ciebie\nTracisz 10'+'% '+'EXPa\n')
                if maxexp*0.1<=exp:
                  exp = exp-(maxexp*0.1)
                  break
                else:
                  exp = 0
                  break
              else:
                print('\nPodano niewlasciowa liczbe')
            if akthp>0 and ruch!=4:
              print('\nWygrywasz walke! '+emoji.emojize(':sports_medal:', language='alias'))
              print('Otrzymane zloto: '+str(ozloto))
              print('Otrzymany EXP: '+str(oexp))
              zloto+=ozloto
              if oexp+exp>=maxexp:
                poziom += 1
                exp = 0
                maxexp += 50
                maxhp += 5
                akthp += 5
                print('Awansujesz na kolejny poziom! '+emoji.emojize(':sparkles:', language='alias'))
                continue
              else:
                exp+= oexp
                continue
            elif ruch ==4:
              continue
            else:
              print('\nZostajesz pokonany '+emoji.emojize(':skull:', language='alias')+'\n\nPrzegrywasz walke\n\nKONIEC GRY '+emoji.emojize(':crying_face:', language='alias'))
              koniec = int(input('\n1 - Zagraj od nowa\n2 - Wyjdz\n=>'))
              if koniec == 1:
                akthp = 100
                maxhp = 100
                zloto = 50
                poziom = 1
                exp = 0
                maxexp = 100
                mikstury = 2
                ilosc_trucizn = 0
                ilosc_mieczy = 0
                obrazeniaD = 0
                obrazeniaT = 0
                zbroja = 0
                tarcza = 0
                miecz = 'brak'
                continue
              else:
                exit
          elif wrog1 == 2:
            runda = 1
            hp1 = 60
            mhp = 60
            oexp = 40
            ozloto = 20
            obrazeniaT = 0
            nazwa1 = 'Wilk'
            ap1 = random.randint(8,10)
            while hp1>0 and akthp>0:
              print('\nRunda '+str(runda))
              print('\nAktualne statystyki:\nHP: '+str(akthp)+'/'+str(maxhp)+'\nMikstury: ' +str(mikstury)+'\nTrucizna: '+str(ilosc_trucizn)+'\nTarcza: '+str(tarcza))
              ruch = int(input('\nWrog: ' +str(nazwa1)+'\nHP: '+str(hp1)+'/'+str(mhp)+'\n\nWybierz akcje:\n1 - Atakuj'+emoji.emojize(':fist:', language='alias')+'\n2 - Wypij miksture'+emoji.emojize(':fire_extinguisher:', language='alias')+'\n3 - Rzuc trucizne'+emoji.emojize(':test_tube:', language='alias')+'\n4 - Uciekaj'+emoji.emojize(':leg:', language='alias')+'\n=>'))
              if ruch == 1:
                hp1 -= (random.randint(6,10)+obrazeniaD+obrazeniaT+obrazeniaW)
                print('Wykonujesz atak\n')
                print(emoji.emojize(':man:', language='alias'),end = ''),time.sleep(0.6),print('\U0001f5e1',end = ''),time.sleep(0.6),print(emoji.emojize(':wolf:', language='alias'),end = ''),print(emoji.emojize(':collision:', language='alias'),end = ''),time.sleep(0.6)
                print('\n\nRuch przeciwnika\n')
                if tarcza == 1:
                  uTarczy = int(input('Uzyc tarczy?\n1 - Tak\n2 - Nie\n=>'))
                  if uTarczy == 1:
                    print(emoji.emojize(':man:', language='alias'),end = ''),print(emoji.emojize(':shield:'),end = ''),time.sleep(0.6),print(emoji.emojize(':collision:', language='alias'),end = ''),print(emoji.emojize(':wolf:', language='alias'),end = ''),time.sleep(0.6),print(emoji.emojize(':red_question_mark:', language='alias')),time.sleep(0.6)
                    runda += 1
                    tarcza -= 1
                    continue
                  else:
                   akthp -= ap1
                   print(emoji.emojize(':man:', language='alias'),end = ''),time.sleep(0.6),print(emoji.emojize(':collision:'),end = ''),print(emoji.emojize(':wolf:', language='alias')),time.sleep(0.6)
                   runda += 1
                   continue
                else:
                  akthp -= ap1
                  print(emoji.emojize(':man:', language='alias'),end = ''),time.sleep(0.6),print(emoji.emojize(':collision:'),end = ''),print(emoji.emojize(':wolf:', language='alias')),time.sleep(0.6)
                  runda += 1
                  continue
              elif ruch == 2 and mikstury>=1 and akthp<=(maxhp-15):
                akthp += 15
                mikstury -= 1
                print('Pijesz miksture\n')
                print(emoji.emojize(':man:', language='alias'),end = ''),print(emoji.emojize(':fire_extinguisher:', language='alias'),end = ''),time.sleep(0.6),print(emoji.emojize(':anger:', language='alias')),time.sleep(0.6)
                continue
              elif ruch == 2 and mikstury<1:
                print('Nie posiadasz mikstur')
                continue
              elif ruch == 2 and mikstury>=1 and akthp>(maxhp-15):
                print('Masz za duzo HP, nie mozesz wypic mikstury')
                continue
              elif ruch == 3 and ilosc_trucizn>=1:
                obrazeniaT += 3
                ilosc_trucizn -=1
                print(emoji.emojize(':man:', language='alias'),end = ''),time.sleep(0.6),print(emoji.emojize(':dashing_away:'),end = ''),time.sleep(0.6),print(emoji.emojize(':dashing_away:', language='alias'),end = ''),time.sleep(0.6),print(emoji.emojize(':test_tube:', language='alias'),end = ''),print(emoji.emojize(':collision:', language='alias'),end = ''),print(emoji.emojize(':wolf:', language='alias')),time.sleep(0.6)
                continue
              elif ruch == 3 and ilosc_trucizn<1:
                print('Nie posiadasz trucizn')
                continue
              elif ruch == 4:
                print('Uciekasz z areny\nWidownia nasmiewa sie z ciebie\nTracisz 10'+'% '+'EXPa\n')
                if maxexp*0.1<=exp:
                  exp = exp-(maxexp*0.1)
                  break
                else:
                  exp = 0
                  break
              else:
                print('\nPodano niewlasciowa liczbe')
            if akthp>0 and ruch!=4:
              print('\nWygrywasz walke! '+emoji.emojize(':sports_medal:', language='alias'))
              print('Otrzymane zloto: '+str(ozloto))
              print('Otrzymany EXP: '+str(oexp))
              zloto+=ozloto
              if oexp+exp>=maxexp:
                poziom += 1
                exp = 0
                maxexp += 50
                maxhp += 5
                akthp += 5
                print('Awansujesz na kolejny poziom! '+emoji.emojize(':sparkles:', language='alias'))
                continue
              else:
                exp+= oexp
                continue
            elif ruch ==4:
              continue
            else:
              print('\nZostajesz pokonany '+emoji.emojize(':skull:', language='alias')+'\n\nPrzegrywasz walke\n\nKONIEC GRY '+emoji.emojize(':crying_face:', language='alias'))
              koniec = int(input('\n1 - Zagraj od nowa\n2 - Wyjdz\n=>'))
              if koniec == 1:
                akthp = 100
                maxhp = 100
                zloto = 50
                poziom = 1
                exp = 0
                maxexp = 100
                mikstury = 2
                ilosc_trucizn = 0
                ilosc_mieczy = 0
                obrazeniaD = 0
                obrazeniaT = 0
                zbroja = 0
                tarcza = 0
                miecz = 'brak'
                continue
              else:
                exit 
          elif wrog1 == 3:
            runda = 1
            hp1 = 85
            mhp = 85
            oexp = 70
            ozloto = 35
            obrazeniaT = 0
            nazwa1 = 'Pijany kowal'
            ap1 = random.randint(11,12)
            while hp1>0 and akthp>0:
              print('\nRunda '+str(runda))
              print('\nAktualne statystyki:\nHP: '+str(akthp)+'/'+str(maxhp)+'\nMikstury: ' +str(mikstury)+'\nTrucizna: '+str(ilosc_trucizn)+'\nTarcza: '+str(tarcza))
              ruch = int(input('\nWrog: ' +str(nazwa1)+'\nHP: '+str(hp1)+'/'+str(mhp)+'\n\nWybierz akcje:\n1 - Atakuj'+emoji.emojize(':fist:', language='alias')+'\n2 - Wypij miksture'+emoji.emojize(':fire_extinguisher:', language='alias')+'\n3 - Rzuc trucizne'+emoji.emojize(':test_tube:', language='alias')+'\n4 - Uciekaj'+emoji.emojize(':leg:', language='alias')+'\n=>'))
              if ruch == 1:
                hp1 -= (random.randint(6,10)+obrazeniaD+obrazeniaT+obrazeniaW)
                print('Wykonujesz atak\n')
                print(emoji.emojize(':man:', language='alias'),end = ''),time.sleep(0.6),print('\U0001f5e1',end = ''),time.sleep(0.6),print(emoji.emojize(':old_man:', language='alias'),end = ''),print(emoji.emojize(':collision:', language='alias'),end = ''),time.sleep(0.6)
                print('\n\nRuch przeciwnika\n')
                if tarcza == 1:
                  uTarczy = int(input('Uzyc tarczy?\n1 - Tak\n2 - Nie\n=>'))
                  if uTarczy == 1:
                    print(emoji.emojize(':man:', language='alias'),end = ''),print(emoji.emojize(':shield:'),end = ''),time.sleep(0.6),print('\U0001F529',end = ''),print(emoji.emojize(':old_man:', language='alias'),end = ''),time.sleep(0.6),print(emoji.emojize(':red_question_mark:', language='alias')),time.sleep(0.6)
                    runda += 1
                    tarcza -= 1
                    continue
                  else:
                   akthp -= ap1
                   print(emoji.emojize(':man:', language='alias'),end = ''),time.sleep(0.6),print(emoji.emojize(':collision:'),end = ''),print('\U0001F529',end = ''),print(emoji.emojize(':old_man:', language='alias')),time.sleep(0.6)
                   runda += 1
                   continue
                else:
                  akthp -= ap1
                  print(emoji.emojize(':man:', language='alias'),end = ''),time.sleep(0.6),print(emoji.emojize(':collision:'),end = ''),print('\U0001F529',end = ''),print(emoji.emojize(':old_man:', language='alias')),time.sleep(0.6)
                  runda += 1
                  continue
              elif ruch == 2 and mikstury>=1 and akthp<=(maxhp-15):
                akthp += 15
                mikstury -= 1
                print('Pijesz miksture\n')
                print(emoji.emojize(':man:', language='alias'),end = ''),print(emoji.emojize(':fire_extinguisher:', language='alias'),end = ''),time.sleep(0.6),print(emoji.emojize(':anger:', language='alias')),time.sleep(0.6)
                continue
              elif ruch == 2 and mikstury<1:
                print('Nie posiadasz mikstur')
                continue
              elif ruch == 2 and mikstury>=1 and akthp>(maxhp-15):
                print('Masz za duzo HP, nie mozesz wypic mikstury')
                continue
              elif ruch == 3 and ilosc_trucizn>=1:
                obrazeniaT += 3
                ilosc_trucizn -=1
                print(emoji.emojize(':man:', language='alias'),end = ''),time.sleep(0.6),print(emoji.emojize(':dashing_away:'),end = ''),time.sleep(0.6),print(emoji.emojize(':dashing_away:', language='alias'),end = ''),time.sleep(0.6),print(emoji.emojize(':test_tube:', language='alias'),end = ''),print(emoji.emojize(':collision:', language='alias'),end = ''),print(emoji.emojize(':old_man:', language='alias')),time.sleep(0.6)
                continue
              elif ruch == 3 and ilosc_trucizn<1:
                print('Nie posiadasz trucizn')
                continue
              elif ruch == 4:
                print('Uciekasz z areny\nWidownia nasmiewa sie z ciebie\nTracisz 10'+'% '+'EXPa\n')
                if maxexp*0.1<=exp:
                  exp = exp-(maxexp*0.1)
                  break
                else:
                  exp = 0
                  break
              else:
                print('\nPodano niewlasciowa liczbe')
            if akthp>0 and ruch!=4:
              print('\nWygrywasz walke! '+emoji.emojize(':sports_medal:', language='alias'))
              print('Otrzymane zloto: '+str(ozloto))
              print('Otrzymany EXP: '+str(oexp))
              zloto+=ozloto
              trofeum1 = 1
              if oexp+exp>=maxexp:
                poziom += 1
                exp = 0
                maxexp += 50
                maxhp += 5
                akthp += 5
                print('Awansujesz na kolejny poziom! '+emoji.emojize(':sparkles:', language='alias'))
                continue
              else:
                exp+= oexp
                continue
            elif ruch ==4:
              continue
            else:
              print('\nZostajesz pokonany '+emoji.emojize(':skull:', language='alias')+'\n\nPrzegrywasz walke\n\nKONIEC GRY '+emoji.emojize(':crying_face:', language='alias'))
              koniec = int(input('\n1 - Zagraj od nowa\n2 - Wyjdz\n=>'))
              if koniec == 1:
                akthp = 100
                maxhp = 100
                zloto = 50
                poziom = 1
                exp = 0
                maxexp = 100
                mikstury = 2
                ilosc_trucizn = 0
                ilosc_mieczy = 0
                obrazeniaD = 0
                obrazeniaT = 0
                zbroja = 0
                tarcza = 0
                miecz = 'brak'
                continue
              else:
                exit
          elif wrog1 == 4:
            continue
          else:
            print('Podano niewlasciowa liczbe')
            continue 
        elif arena == 2 and poziom>=4:
          wrog1 = int(input('Wybierz przeciwinika:\n(Sortowane od najprostszego do najtrudniejszego)\n1 - Zly Wiesniak'+emoji.emojize(':farmer:', language='alias')+'\n2 - Puma'+emoji.emojize(':leopard:', language='alias')+'\n3 - Rzeznik'+emoji.emojize(':man_cook:', language='alias')+'\n4 - Wyjscie\n=>'))
          if wrog1 == 1:
            runda = 1
            hp1 = 100
            mhp = 100
            oexp = 92
            ozloto = 48
            obrazeniaT = 0
            nazwa1 = 'Zly Wiesniak'
            ap1 = random.randint(13,15)
            while hp1>0 and akthp>0:
              print('\nRunda '+str(runda))
              print('\nAktualne statystyki:\nHP: '+str(akthp)+'/'+str(maxhp)+'\nMikstury: ' +str(mikstury)+'\nTrucizna: '+str(ilosc_trucizn)+'\nTarcza: '+str(tarcza))
              ruch = int(input('\nWrog: ' +str(nazwa1)+'\nHP: '+str(hp1)+'/'+str(mhp)+'\n\nWybierz akcje:\n1 - Atakuj'+emoji.emojize(':fist:', language='alias')+'\n2 - Wypij miksture'+emoji.emojize(':fire_extinguisher:', language='alias')+'\n3 - Rzuc trucizne'+emoji.emojize(':test_tube:', language='alias')+'\n4 - Uciekaj'+emoji.emojize(':leg:', language='alias')+'\n=>'))
              if ruch == 1:
                hp1 -= (random.randint(6,10)+obrazeniaD+obrazeniaT+obrazeniaW)
                print('Wykonujesz atak\n')
                print(emoji.emojize(':man:', language='alias'),end = ''),time.sleep(0.6),print('\U0001f5e1',end = ''),time.sleep(0.6),print(emoji.emojize(':farmer:', language='alias'),end = ''),print(emoji.emojize(':collision:', language='alias'),end = ''),time.sleep(0.6)
                print('\n\nRuch przeciwnika\n')
                if tarcza == 1:
                  uTarczy = int(input('Uzyc tarczy?\n1 - Tak\n2 - Nie\n=>'))
                  if uTarczy == 1:
                    print(emoji.emojize(':man:', language='alias'),end = ''),print(emoji.emojize(':shield:'),end = ''),time.sleep(0.6),print(emoji.emojize(':pick: ', language='alias'),end = ''),print(emoji.emojize(':farmer:', language='alias'),end = ''),time.sleep(0.6),print(emoji.emojize(':red_question_mark:', language='alias')),time.sleep(0.6)
                    runda += 1
                    tarcza -= 1
                    continue
                  else:
                   akthp -= ap1
                   print(emoji.emojize(':man:', language='alias'),end = ''),time.sleep(0.6),print(emoji.emojize(':collision:'),end = ''),print(emoji.emojize(':pick: ', language='alias'),end = ''),print(emoji.emojize(':farmer:', language='alias')),time.sleep(0.6)
                   runda += 1
                   continue
                else:
                  akthp -= ap1
                  print(emoji.emojize(':man:', language='alias'),end = ''),time.sleep(0.6),print(emoji.emojize(':collision:'),end = ''),print(emoji.emojize(':pick: ', language='alias'),end = ''),print(emoji.emojize(':farmer:', language='alias')),time.sleep(0.6)
                  runda += 1
                  continue
              elif ruch == 2 and mikstury>=1 and akthp<=(maxhp-15):
                akthp += 15
                mikstury -= 1
                print('Pijesz miksture\n')
                print(emoji.emojize(':man:', language='alias'),end = ''),print(emoji.emojize(':fire_extinguisher:', language='alias'),end = ''),time.sleep(0.6),print(emoji.emojize(':anger:', language='alias')),time.sleep(0.6)
                continue
              elif ruch == 2 and mikstury<1:
                print('Nie posiadasz mikstur')
                continue
              elif ruch == 2 and mikstury>=1 and akthp>(maxhp-15):
                print('Masz za duzo HP, nie mozesz wypic mikstury')
                continue
              elif ruch == 3 and ilosc_trucizn>=1:
                obrazeniaT += 3
                ilosc_trucizn -=1
                print(emoji.emojize(':man:', language='alias'),end = ''),time.sleep(0.6),print(emoji.emojize(':dashing_away:'),end = ''),time.sleep(0.6),print(emoji.emojize(':dashing_away:', language='alias'),end = ''),time.sleep(0.6),print(emoji.emojize(':test_tube:', language='alias'),end = ''),print(emoji.emojize(':collision:', language='alias'),end = ''),print(emoji.emojize(':farmer:', language='alias')),time.sleep(0.6)
                continue
              elif ruch == 3 and ilosc_trucizn<1:
                print('Nie posiadasz trucizn')
                continue
              elif ruch == 4:
                print('Uciekasz z areny\nWidownia nasmiewa sie z ciebie\nTracisz 10'+'% '+'EXPa\n')
                if maxexp*0.1<=exp:
                  exp = exp-(maxexp*0.1)
                  break
                else:
                  exp = 0
                  break
              else:
                print('\nPodano niewlasciowa liczbe')
            if akthp>0 and ruch!=4:
              print('\nWygrywasz walke! '+emoji.emojize(':sports_medal:', language='alias'))
              print('Otrzymane zloto: '+str(ozloto))
              print('Otrzymany EXP: '+str(oexp))
              zloto+=ozloto
              if oexp+exp>=maxexp:
                poziom += 1
                exp = 0
                maxexp += 50
                maxhp += 5
                akthp += 5
                print('Awansujesz na kolejny poziom! '+emoji.emojize(':sparkles:', language='alias'))
                continue
              else:
                exp+= oexp
                continue
            elif ruch ==4:
              continue
            else:
              print('\nZostajesz pokonany '+emoji.emojize(':skull:', language='alias')+'\n\nPrzegrywasz walke\n\nKONIEC GRY '+emoji.emojize(':crying_face:', language='alias'))
              koniec = int(input('\n1 - Zagraj od nowa\n2 - Wyjdz\n=>'))
              if koniec == 1:
                akthp = 100
                maxhp = 100
                zloto = 50
                poziom = 1
                exp = 0
                maxexp = 100
                mikstury = 2
                ilosc_trucizn = 0
                ilosc_mieczy = 0
                obrazeniaD = 0
                obrazeniaT = 0
                zbroja = 0
                tarcza = 0
                miecz = 'brak'
                continue
              else:
                exit
          elif wrog1 == 2:
            runda = 1
            hp1 = 105
            mhp = 105
            oexp = 105
            ozloto = 56
            obrazeniaT = 0
            nazwa1 = 'Puma'
            ap1 = random.randint(17,18)
            while hp1>0 and akthp>0:
              print('\nRunda '+str(runda))
              print('\nAktualne statystyki:\nHP: '+str(akthp)+'/'+str(maxhp)+'\nMikstury: ' +str(mikstury)+'\nTrucizna: '+str(ilosc_trucizn)+'\nTarcza: '+str(tarcza))
              ruch = int(input('\nWrog: ' +str(nazwa1)+'\nHP: '+str(hp1)+'/'+str(mhp)+'\n\nWybierz akcje:\n1 - Atakuj'+emoji.emojize(':fist:', language='alias')+'\n2 - Wypij miksture'+emoji.emojize(':fire_extinguisher:', language='alias')+'\n3 - Rzuc trucizne'+emoji.emojize(':test_tube:', language='alias')+'\n4 - Uciekaj'+emoji.emojize(':leg:', language='alias')+'\n=>'))
              if ruch == 1:
                hp1 -= (random.randint(6,10)+obrazeniaD+obrazeniaT+obrazeniaW)
                print('Wykonujesz atak\n')
                print(emoji.emojize(':man:', language='alias'),end = ''),time.sleep(0.6),print('\U0001f5e1',end = ''),time.sleep(0.6),print(emoji.emojize(':leopard:', language='alias'),end = ''),print(emoji.emojize(':collision:', language='alias'),end = ''),time.sleep(0.6)
                print('\n\nRuch przeciwnika\n')
                if tarcza == 1:
                  uTarczy = int(input('Uzyc tarczy?\n1 - Tak\n2 - Nie\n=>'))
                  if uTarczy == 1:
                    print(emoji.emojize(':man:', language='alias'),end = ''),print(emoji.emojize(':shield:'),end = ''),time.sleep(0.6),print(emoji.emojize(':collision:', language='alias'),end = ''),print(emoji.emojize(':leopard:', language='alias'),end = ''),time.sleep(0.6),print(emoji.emojize(':red_question_mark:', language='alias')),time.sleep(0.6)
                    runda += 1
                    tarcza -= 1
                    continue
                  else:
                   akthp -= ap1
                   print(emoji.emojize(':man:', language='alias'),end = ''),time.sleep(0.6),print(emoji.emojize(':collision:'),end = ''),print(emoji.emojize(':leopard:', language='alias')),time.sleep(0.6)
                   runda += 1
                   continue
                else:
                  akthp -= ap1
                  print(emoji.emojize(':man:', language='alias'),end = ''),time.sleep(0.6),print(emoji.emojize(':collision:'),end = ''),print(emoji.emojize(':leopard:', language='alias')),time.sleep(0.6)
                  runda += 1
                  continue
              elif ruch == 2 and mikstury>=1 and akthp<=(maxhp-15):
                akthp += 15
                mikstury -= 1
                print('Pijesz miksture\n')
                print(emoji.emojize(':man:', language='alias'),end = ''),print(emoji.emojize(':fire_extinguisher:', language='alias'),end = ''),time.sleep(0.6),print(emoji.emojize(':anger:', language='alias')),time.sleep(0.6)
                continue
              elif ruch == 2 and mikstury<1:
                print('Nie posiadasz mikstur')
                continue
              elif ruch == 2 and mikstury>=1 and akthp>(maxhp-15):
                print('Masz za duzo HP, nie mozesz wypic mikstury')
                continue
              elif ruch == 3 and ilosc_trucizn>=1:
                obrazeniaT += 3
                ilosc_trucizn -=1
                print(emoji.emojize(':man:', language='alias'),end = ''),time.sleep(0.6),print(emoji.emojize(':dashing_away:'),end = ''),time.sleep(0.6),print(emoji.emojize(':dashing_away:', language='alias'),end = ''),time.sleep(0.6),print(emoji.emojize(':test_tube:', language='alias'),end = ''),print(emoji.emojize(':collision:', language='alias'),end = ''),print(emoji.emojize(':leopard:', language='alias')),time.sleep(0.6)
                continue
              elif ruch == 3 and ilosc_trucizn<1:
                print('Nie posiadasz trucizn')
                continue
              elif ruch == 4:
                print('Uciekasz z areny\nWidownia nasmiewa sie z ciebie\nTracisz 10'+'% '+'EXPa\n')
                if maxexp*0.1<=exp:
                  exp = exp-(maxexp*0.1)
                  break
                else:
                  exp = 0
                  break
              else:
                print('\nPodano niewlasciowa liczbe')
            if akthp>0 and ruch!=4:
              print('\nWygrywasz walke! '+emoji.emojize(':sports_medal:', language='alias'))
              print('Otrzymane zloto: '+str(ozloto))
              print('Otrzymany EXP: '+str(oexp))
              zloto+=ozloto
              if oexp+exp>=maxexp:
                poziom += 1
                exp = 0
                maxexp += 50
                maxhp += 5
                akthp += 5
                print('Awansujesz na kolejny poziom! '+emoji.emojize(':sparkles:', language='alias'))
                continue
              else:
                exp+= oexp
                continue
            elif ruch ==4:
              continue
            else:
              print('\nZostajesz pokonany '+emoji.emojize(':skull:', language='alias')+'\n\nPrzegrywasz walke\n\nKONIEC GRY '+emoji.emojize(':crying_face:', language='alias'))
              koniec = int(input('\n1 - Zagraj od nowa\n2 - Wyjdz\n=>'))
              if koniec == 1:
                akthp = 100
                maxhp = 100
                zloto = 50
                poziom = 1
                exp = 0
                maxexp = 100
                mikstury = 2
                ilosc_trucizn = 0
                ilosc_mieczy = 0
                obrazeniaD = 0
                obrazeniaT = 0
                zbroja = 0
                tarcza = 0
                miecz = 'brak'
                continue
              else:
                exit 
          elif wrog1 == 3:
            runda = 1
            hp1 = 120
            mhp = 120
            oexp = 125
            ozloto = 65
            obrazeniaT = 0
            nazwa1 = 'Rzeznik'
            ap1 = random.randint(19,21)
            while hp1>0 and akthp>0:
              print('\nRunda '+str(runda))
              print('\nAktualne statystyki:\nHP: '+str(akthp)+'/'+str(maxhp)+'\nMikstury: ' +str(mikstury)+'\nTrucizna: '+str(ilosc_trucizn)+'\nTarcza: '+str(tarcza))
              ruch = int(input('\nWrog: ' +str(nazwa1)+'\nHP: '+str(hp1)+'/'+str(mhp)+'\n\nWybierz akcje:\n1 - Atakuj'+emoji.emojize(':fist:', language='alias')+'\n2 - Wypij miksture'+emoji.emojize(':fire_extinguisher:', language='alias')+'\n3 - Rzuc trucizne'+emoji.emojize(':test_tube:', language='alias')+'\n4 - Uciekaj'+emoji.emojize(':leg:', language='alias')+'\n=>'))
              if ruch == 1:
                hp1 -= (random.randint(6,10)+obrazeniaD+obrazeniaT+obrazeniaW)
                print('Wykonujesz atak\n')
                print(emoji.emojize(':man:', language='alias'),end = ''),time.sleep(0.6),print('\U0001f5e1',end = ''),time.sleep(0.6),print(emoji.emojize(':man_cook:', language='alias'),end = ''),print(emoji.emojize(':collision:', language='alias'),end = ''),time.sleep(0.6)
                print('\n\nRuch przeciwnika\n')
                if tarcza == 1:
                  uTarczy = int(input('Uzyc tarczy?\n1 - Tak\n2 - Nie\n=>'))
                  if uTarczy == 1:
                    print(emoji.emojize(':man:', language='alias'),end = ''),print(emoji.emojize(':shield:'),end = ''),time.sleep(0.6),print('\U0001FA9A',end = ''),print(emoji.emojize(':man_cook:', language='alias'),end = ''),time.sleep(0.6),print(emoji.emojize(':red_question_mark:', language='alias')),time.sleep(0.6)
                    runda += 1
                    tarcza -= 1
                    continue
                  else:
                   akthp -= ap1
                   print(emoji.emojize(':man:', language='alias'),end = ''),time.sleep(0.6),print(emoji.emojize(':collision:'),end = ''),print('\U0001FA9A',end = ''),print(emoji.emojize(':man_cook:', language='alias')),time.sleep(0.6)
                   runda += 1
                   continue
                else:
                  akthp -= ap1
                  print(emoji.emojize(':man:', language='alias'),end = ''),time.sleep(0.6),print(emoji.emojize(':collision:'),end = ''),print('\U0001FA9A',end = ''),print(emoji.emojize(':man_cook:', language='alias')),time.sleep(0.6)
                  runda += 1
                  continue
              elif ruch == 2 and mikstury>=1 and akthp<=(maxhp-15):
                akthp += 15
                mikstury -= 1
                print('Pijesz miksture\n')
                print(emoji.emojize(':man:', language='alias'),end = ''),print(emoji.emojize(':fire_extinguisher:', language='alias'),end = ''),time.sleep(0.6),print(emoji.emojize(':anger:', language='alias')),time.sleep(0.6)
                continue
              elif ruch == 2 and mikstury<1:
                print('Nie posiadasz mikstur')
                continue
              elif ruch == 2 and mikstury>=1 and akthp>(maxhp-15):
                print('Masz za duzo HP, nie mozesz wypic mikstury')
                continue
              elif ruch == 3 and ilosc_trucizn>=1:
                obrazeniaT += 3
                ilosc_trucizn -=1
                print(emoji.emojize(':man:', language='alias'),end = ''),time.sleep(0.6),print(emoji.emojize(':dashing_away:'),end = ''),time.sleep(0.6),print(emoji.emojize(':dashing_away:', language='alias'),end = ''),time.sleep(0.6),print(emoji.emojize(':test_tube:', language='alias'),end = ''),print(emoji.emojize(':collision:', language='alias'),end = ''),print(emoji.emojize(':man_cook:', language='alias')),time.sleep(0.6)
                continue
              elif ruch == 3 and ilosc_trucizn<1:
                print('Nie posiadasz trucizn')
                continue
              elif ruch == 4:
                print('Uciekasz z areny\nWidownia nasmiewa sie z ciebie\nTracisz 10'+'% '+'EXPa\n')
                if maxexp*0.1<=exp:
                  exp = exp-(maxexp*0.1)
                  break
                else:
                  exp = 0
                  break
              else:
                print('\nPodano niewlasciowa liczbe')
            if akthp>0 and ruch!=4:
              print('\nWygrywasz walke! '+emoji.emojize(':sports_medal:', language='alias'))
              print('Otrzymane zloto: '+str(ozloto))
              print('Otrzymany EXP: '+str(oexp))
              zloto+=ozloto
              trofeum2 = 1
              if oexp+exp>=maxexp:
                poziom += 1
                exp = 0
                maxexp += 50
                maxhp += 5
                akthp += 5
                print('Awansujesz na kolejny poziom! '+emoji.emojize(':sparkles:', language='alias'))
                continue
              else:
                exp+= oexp
                continue
            elif ruch ==4:
              continue
            else:
              print('\nZostajesz pokonany '+emoji.emojize(':skull:', language='alias')+'\n\nPrzegrywasz walke\n\nKONIEC GRY '+emoji.emojize(':crying_face:', language='alias'))
              koniec = int(input('\n1 - Zagraj od nowa\n2 - Wyjdz\n=>'))
              if koniec == 1:
                akthp = 100
                maxhp = 100
                zloto = 50
                poziom = 1
                exp = 0
                maxexp = 100
                mikstury = 2
                ilosc_trucizn = 0
                ilosc_mieczy = 0
                obrazeniaD = 0
                obrazeniaT = 0
                zbroja = 0
                tarcza = 0
                miecz = 'brak'
                continue
              else:
                exit
          elif wrog1 == 4:
            continue
          else:
            print('Podano niewlasciowa liczbe')
            continue
        elif arena == 2 and poziom <4:
          print('Masz za niski poziom zeby walczyc na tej arenie')
          continue
        elif arena == 3 and poziom>=10:
          wrog1 = int(input('Wybierz przeciwinika:\n(Sortowane od najprostszego do najtrudniejszego)\n1 - Gladiator'+emoji.emojize(':guard:', language='alias')+'\n2 - Niedzwiedz'+emoji.emojize(':bear:', language='alias')+'\n3 - Dowodca armii'+('\U0001F472')+'\n4 - Wyjscie\n=>'))
          if wrog1 == 1:
            runda = 1
            hp1 = 130
            mhp = 130
            oexp = 140
            ozloto = 73
            obrazeniaT = 0
            nazwa1 = 'Gladiator'
            ap1 = random.randint(22,23)
            while hp1>0 and akthp>0:
              print('\nRunda '+str(runda))
              print('\nAktualne statystyki:\nHP: '+str(akthp)+'/'+str(maxhp)+'\nMikstury: ' +str(mikstury)+'\nTrucizna: '+str(ilosc_trucizn)+'\nTarcza: '+str(tarcza))
              ruch = int(input('\nWrog: ' +str(nazwa1)+'\nHP: '+str(hp1)+'/'+str(mhp)+'\n\nWybierz akcje:\n1 - Atakuj'+emoji.emojize(':fist:', language='alias')+'\n2 - Wypij miksture'+emoji.emojize(':fire_extinguisher:', language='alias')+'\n3 - Rzuc trucizne'+emoji.emojize(':test_tube:', language='alias')+'\n4 - Uciekaj'+emoji.emojize(':leg:', language='alias')+'\n=>'))
              if ruch == 1:
                hp1 -= (random.randint(6,10)+obrazeniaD+obrazeniaT+obrazeniaW)
                print('Wykonujesz atak\n')
                print(emoji.emojize(':man:', language='alias'),end = ''),time.sleep(0.6),print('\U0001f5e1',end = ''),time.sleep(0.6),print(emoji.emojize(':guard:', language='alias'),end = ''),print(emoji.emojize(':collision:', language='alias'),end = ''),time.sleep(0.6)
                print('\n\nRuch przeciwnika\n')
                if tarcza == 1:
                  uTarczy = int(input('Uzyc tarczy?\n1 - Tak\n2 - Nie\n=>'))
                  if uTarczy == 1:
                    print(emoji.emojize(':man:', language='alias'),end = ''),print(emoji.emojize(':shield:'),end = ''),time.sleep(0.6),print(emoji.emojize(':axe:', language='alias'),end = ''),print(emoji.emojize(':guard:', language='alias'),end = ''),time.sleep(0.6),print(emoji.emojize(':red_question_mark:', language='alias')),time.sleep(0.6)
                    runda += 1
                    tarcza -= 1
                    continue
                  else:
                   akthp -= ap1
                   print(emoji.emojize(':man:', language='alias'),end = ''),time.sleep(0.6),print(emoji.emojize(':collision:'),end = ''),print(emoji.emojize(':axe:', language='alias'),end = ''),print(emoji.emojize(':guard:', language='alias')),time.sleep(0.6)
                   runda += 1
                   continue
                else:
                  akthp -= ap1
                  print(emoji.emojize(':man:', language='alias'),end = ''),time.sleep(0.6),print(emoji.emojize(':collision:'),end = ''),print(emoji.emojize(':axe:', language='alias'),end = ''),print(emoji.emojize(':guard:', language='alias')),time.sleep(0.6)
                  runda += 1
                  continue
              elif ruch == 2 and mikstury>=1 and akthp<=(maxhp-15):
                akthp += 15
                mikstury -= 1
                print('Pijesz miksture\n')
                print(emoji.emojize(':man:', language='alias'),end = ''),print(emoji.emojize(':fire_extinguisher:', language='alias'),end = ''),time.sleep(0.6),print(emoji.emojize(':anger:', language='alias')),time.sleep(0.6)
                continue
              elif ruch == 2 and mikstury<1:
                print('Nie posiadasz mikstur')
                continue
              elif ruch == 2 and mikstury>=1 and akthp>(maxhp-15):
                print('Masz za duzo HP, nie mozesz wypic mikstury')
                continue
              elif ruch == 3 and ilosc_trucizn>=1:
                obrazeniaT += 3
                ilosc_trucizn -=1
                print(emoji.emojize(':man:', language='alias'),end = ''),time.sleep(0.6),print(emoji.emojize(':dashing_away:'),end = ''),time.sleep(0.6),print(emoji.emojize(':dashing_away:', language='alias'),end = ''),time.sleep(0.6),print(emoji.emojize(':test_tube:', language='alias'),end = ''),print(emoji.emojize(':collision:', language='alias'),end = ''),print(emoji.emojize(':guard:', language='alias')),time.sleep(0.6)
                continue
              elif ruch == 3 and ilosc_trucizn<1:
                print('Nie posiadasz trucizn')
                continue
              elif ruch == 4:
                print('Uciekasz z areny\nWidownia nasmiewa sie z ciebie\nTracisz 10'+'% '+'EXPa\n')
                if maxexp*0.1<=exp:
                  exp = exp-(maxexp*0.1)
                  break
                else:
                  exp = 0
                  break
              else:
                print('\nPodano niewlasciowa liczbe')
            if akthp>0 and ruch!=4:
              print('\nWygrywasz walke! '+emoji.emojize(':sports_medal:', language='alias'))
              print('Otrzymane zloto: '+str(ozloto))
              print('Otrzymany EXP: '+str(oexp))
              zloto+=ozloto
              if oexp+exp>=maxexp:
                poziom += 1
                exp = 0
                maxexp += 50
                maxhp += 5
                akthp += 5
                print('Awansujesz na kolejny poziom! '+emoji.emojize(':sparkles:', language='alias'))
                continue
              else:
                exp+= oexp
                continue
            elif ruch ==4:
              continue
            else:
              print('\nZostajesz pokonany '+emoji.emojize(':skull:', language='alias')+'\n\nPrzegrywasz walke\n\nKONIEC GRY '+emoji.emojize(':crying_face:', language='alias'))
              koniec = int(input('\n1 - Zagraj od nowa\n2 - Wyjdz\n=>'))
              if koniec == 1:
                akthp = 100
                maxhp = 100
                zloto = 50
                poziom = 1
                exp = 0
                maxexp = 100
                mikstury = 2
                ilosc_trucizn = 0
                ilosc_mieczy = 0
                obrazeniaD = 0
                obrazeniaT = 0
                zbroja = 0
                tarcza = 0
                miecz = 'brak'
                continue
              else:
                exit
          elif wrog1 == 2:
            runda = 1
            hp1 = 145
            mhp = 145
            oexp = 150
            ozloto = 80
            obrazeniaT = 0
            nazwa1 = 'Niedzwiedz'
            ap1 = random.randint(25,27)
            while hp1>0 and akthp>0:
              print('\nRunda '+str(runda))
              print('\nAktualne statystyki:\nHP: '+str(akthp)+'/'+str(maxhp)+'\nMikstury: ' +str(mikstury)+'\nTrucizna: '+str(ilosc_trucizn)+'\nTarcza: '+str(tarcza))
              ruch = int(input('\nWrog: ' +str(nazwa1)+'\nHP: '+str(hp1)+'/'+str(mhp)+'\n\nWybierz akcje:\n1 - Atakuj'+emoji.emojize(':fist:', language='alias')+'\n2 - Wypij miksture'+emoji.emojize(':fire_extinguisher:', language='alias')+'\n3 - Rzuc trucizne'+emoji.emojize(':test_tube:', language='alias')+'\n4 - Uciekaj'+emoji.emojize(':leg:', language='alias')+'\n=>'))
              if ruch == 1:
                hp1 -= (random.randint(6,10)+obrazeniaD+obrazeniaT+obrazeniaW)
                print('Wykonujesz atak\n')
                print(emoji.emojize(':man:', language='alias'),end = ''),time.sleep(0.6),print('\U0001f5e1',end = ''),time.sleep(0.6),print(emoji.emojize(':bear:', language='alias'),end = ''),print(emoji.emojize(':collision:', language='alias'),end = ''),time.sleep(0.6)
                print('\n\nRuch przeciwnika\n')
                if tarcza == 1:
                  uTarczy = int(input('Uzyc tarczy?\n1 - Tak\n2 - Nie\n=>'))
                  if uTarczy == 1:
                    print(emoji.emojize(':man:', language='alias'),end = ''),print(emoji.emojize(':shield:'),end = ''),time.sleep(0.6),print(emoji.emojize(':collision:', language='alias'),end = ''),print(emoji.emojize(':bear:', language='alias'),end = ''),time.sleep(0.6),print(emoji.emojize(':red_question_mark:', language='alias')),time.sleep(0.6)
                    runda += 1
                    tarcza -= 1
                    continue
                  else:
                   akthp -= ap1
                   print(emoji.emojize(':man:', language='alias'),end = ''),time.sleep(0.6),print(emoji.emojize(':collision:'),end = ''),print(emoji.emojize(':bear:', language='alias')),time.sleep(0.6)
                   runda += 1
                   continue
                else:
                  akthp -= ap1
                  print(emoji.emojize(':man:', language='alias'),end = ''),time.sleep(0.6),print(emoji.emojize(':collision:'),end = ''),print(emoji.emojize(':bear:', language='alias')),time.sleep(0.6)
                  runda += 1
                  continue
              elif ruch == 2 and mikstury>=1 and akthp<=(maxhp-15):
                akthp += 15
                mikstury -= 1
                print('Pijesz miksture\n')
                print(emoji.emojize(':man:', language='alias'),end = ''),print(emoji.emojize(':fire_extinguisher:', language='alias'),end = ''),time.sleep(0.6),print(emoji.emojize(':anger:', language='alias')),time.sleep(0.6)
                continue
              elif ruch == 2 and mikstury<1:
                print('Nie posiadasz mikstur')
                continue
              elif ruch == 2 and mikstury>=1 and akthp>(maxhp-15):
                print('Masz za duzo HP, nie mozesz wypic mikstury')
                continue
              elif ruch == 3 and ilosc_trucizn>=1:
                obrazeniaT += 3
                ilosc_trucizn -=1
                print(emoji.emojize(':man:', language='alias'),end = ''),time.sleep(0.6),print(emoji.emojize(':dashing_away:'),end = ''),time.sleep(0.6),print(emoji.emojize(':dashing_away:', language='alias'),end = ''),time.sleep(0.6),print(emoji.emojize(':test_tube:', language='alias'),end = ''),print(emoji.emojize(':collision:', language='alias'),end = ''),print(emoji.emojize(':bear:', language='alias')),time.sleep(0.6)
                continue
              elif ruch == 3 and ilosc_trucizn<1:
                print('Nie posiadasz trucizn')
                continue
              elif ruch == 4:
                print('Uciekasz z areny\nWidownia nasmiewa sie z ciebie\nTracisz 10'+'% '+'EXPa\n')
                if maxexp*0.1<=exp:
                  exp = exp-(maxexp*0.1)
                  break
                else:
                  exp = 0
                  break
              else:
                print('\nPodano niewlasciowa liczbe')
            if akthp>0 and ruch!=4:
              print('\nWygrywasz walke! '+emoji.emojize(':sports_medal:', language='alias'))
              print('Otrzymane zloto: '+str(ozloto))
              print('Otrzymany EXP: '+str(oexp))
              zloto+=ozloto
              if oexp+exp>=maxexp:
                poziom += 1
                exp = 0
                maxexp += 50
                maxhp += 5
                akthp += 5
                print('Awansujesz na kolejny poziom! '+emoji.emojize(':sparkles:', language='alias'))
                continue
              else:
                exp+= oexp
                continue
            elif ruch ==4:
              continue
            else:
              print('\nZostajesz pokonany '+emoji.emojize(':skull:', language='alias')+'\n\nPrzegrywasz walke\n\nKONIEC GRY '+emoji.emojize(':crying_face:', language='alias'))
              koniec = int(input('\n1 - Zagraj od nowa\n2 - Wyjdz\n=>'))
              if koniec == 1:
                akthp = 100
                maxhp = 100
                zloto = 50
                poziom = 1
                exp = 0
                maxexp = 100
                mikstury = 2
                ilosc_trucizn = 0
                ilosc_mieczy = 0
                obrazeniaD = 0
                obrazeniaT = 0
                zbroja = 0
                tarcza = 0
                miecz = 'brak'
                continue
              else:
                exit 
          elif wrog1 == 3:
            runda = 1
            hp1 = 155
            mhp = 155
            oexp = 165
            ozloto = 88
            obrazeniaT = 0
            nazwa1 = 'Dowodca armii'
            ap1 = random.randint(28,30)
            while hp1>0 and akthp>0:
              print('\nRunda '+str(runda))
              print('\nAktualne statystyki:\nHP: '+str(akthp)+'/'+str(maxhp)+'\nMikstury: ' +str(mikstury)+'\nTrucizna: '+str(ilosc_trucizn)+'\nTarcza: '+str(tarcza))
              ruch = int(input('\nWrog: ' +str(nazwa1)+'\nHP: '+str(hp1)+'/'+str(mhp)+'\n\nWybierz akcje:\n1 - Atakuj'+emoji.emojize(':fist:', language='alias')+'\n2 - Wypij miksture'+emoji.emojize(':fire_extinguisher:', language='alias')+'\n3 - Rzuc trucizne'+emoji.emojize(':test_tube:', language='alias')+'\n4 - Uciekaj'+emoji.emojize(':leg:', language='alias')+'\n=>'))
              if ruch == 1:
                hp1 -= (random.randint(6,10)+obrazeniaD+obrazeniaT+obrazeniaW)
                print('Wykonujesz atak\n')
                print(emoji.emojize(':man:', language='alias'),end = ''),time.sleep(0.6),print('\U0001f5e1',end = ''),time.sleep(0.6),print('\U0001F472',end = ''),print(emoji.emojize(':collision:', language='alias'),end = ''),time.sleep(0.6)
                print('\n\nRuch przeciwnika\n')
                if tarcza == 1:
                  uTarczy = int(input('Uzyc tarczy?\n1 - Tak\n2 - Nie\n=>'))
                  if uTarczy == 1:
                    print(emoji.emojize(':man:', language='alias'),end = ''),print(emoji.emojize(':shield:'),end = ''),time.sleep(0.6),print(emoji.emojize(':dagger:'),end = ''),print('\U0001F472',end = ''),time.sleep(0.6),print(emoji.emojize(':red_question_mark:', language='alias')),time.sleep(0.6)
                    runda += 1
                    tarcza -= 1
                    continue
                  else:
                   akthp -= ap1
                   print(emoji.emojize(':man:', language='alias'),end = ''),time.sleep(0.6),print(emoji.emojize(':collision:'),end = ''),print(emoji.emojize(':dagger:'),end = ''),print('\U0001F472'),time.sleep(0.6)
                   runda += 1
                   continue
                else:
                  akthp -= ap1
                  print(emoji.emojize(':man:', language='alias'),end = ''),time.sleep(0.6),print(emoji.emojize(':collision:'),end = ''),print(emoji.emojize(':dagger:'),end = ''),print('\U0001F472'),time.sleep(0.6)
                  runda += 1
                  continue
              elif ruch == 2 and mikstury>=1 and akthp<=(maxhp-15):
                akthp += 15
                mikstury -= 1
                print('Pijesz miksture\n')
                print(emoji.emojize(':man:', language='alias'),end = ''),print(emoji.emojize(':fire_extinguisher:', language='alias'),end = ''),time.sleep(0.6),print(emoji.emojize(':anger:', language='alias')),time.sleep(0.6)
                continue
              elif ruch == 2 and mikstury<1:
                print('Nie posiadasz mikstur')
                continue
              elif ruch == 2 and mikstury>=1 and akthp>(maxhp-15):
                print('Masz za duzo HP, nie mozesz wypic mikstury')
                continue
              elif ruch == 3 and ilosc_trucizn>=1:
                obrazeniaT += 3
                ilosc_trucizn -=1
                print(emoji.emojize(':man:', language='alias'),end = ''),time.sleep(0.6),print(emoji.emojize(':dashing_away:'),end = ''),time.sleep(0.6),print(emoji.emojize(':dashing_away:', language='alias'),end = ''),time.sleep(0.6),print(emoji.emojize(':test_tube:', language='alias'),end = ''),print(emoji.emojize(':collision:', language='alias'),end = ''),print('\U0001F472'),time.sleep(0.6)
                continue
              elif ruch == 3 and ilosc_trucizn<1:
                print('Nie posiadasz trucizn')
                continue
              elif ruch == 4:
                print('Uciekasz z areny\nWidownia nasmiewa sie z ciebie\nTracisz 10'+'% '+'EXPa\n')
                if maxexp*0.1<=exp:
                  exp = exp-(maxexp*0.1)
                  break
                else:
                  exp = 0
                  break
              else:
                print('\nPodano niewlasciowa liczbe')
            if akthp>0 and ruch!=4:
              print('\nWygrywasz walke! '+emoji.emojize(':sports_medal:', language='alias'))
              print('Otrzymane zloto: '+str(ozloto))
              print('Otrzymany EXP: '+str(oexp))
              zloto+=ozloto
              trofeum3 = 1
              if oexp+exp>=maxexp:
                poziom += 1
                exp = 0
                maxexp += 50
                maxhp += 5
                akthp += 5
                print('Awansujesz na kolejny poziom! '+emoji.emojize(':sparkles:', language='alias'))
                continue
              else:
                exp+= oexp
                continue
            elif ruch ==4:
              continue
            else:
              print('\nZostajesz pokonany '+emoji.emojize(':skull:', language='alias')+'\n\nPrzegrywasz walke\n\nKONIEC GRY '+emoji.emojize(':crying_face:', language='alias'))
              koniec = int(input('\n1 - Zagraj od nowa\n2 - Wyjdz\n=>'))
              if koniec == 1:
                akthp = 100
                maxhp = 100
                zloto = 50
                poziom = 1
                exp = 0
                maxexp = 100
                mikstury = 2
                ilosc_trucizn = 0
                ilosc_mieczy = 0
                obrazeniaD = 0
                obrazeniaT = 0
                zbroja = 0
                tarcza = 0
                miecz = 'brak'
                continue
              else:
                exit
          elif wrog1 == 4:
            continue
          else:
            print('Podano niewlasciowa liczbe')
            continue
        elif arena == 3 and poziom <10:
          print('Masz za niski poziom zeby walczyc na tej arenie')
          continue
        elif arena == 4 and poziom>=16:
          wrog1 = int(input('Wybierz przeciwinika:\n(Sortowane od najprostszego do najtrudniejszego)\n1 - Ninja'+emoji.emojize(':ninja:', language='alias')+'\n2 - Slon'+emoji.emojize(':elephant:', language='alias')+'\n3 - Demon'+emoji.emojize(':ogre:',language='alias')+'\n4 - Wyjscie\n=>'))
          if wrog1 == 1:
            runda = 1
            hp1 = 165
            mhp = 165
            oexp = 175
            ozloto = 95
            obrazeniaT = 0
            nazwa1 = 'Ninja'
            ap1 = random.randint(32,33)
            while hp1>0 and akthp>0:
              print('\nRunda '+str(runda))
              print('\nAktualne statystyki:\nHP: '+str(akthp)+'/'+str(maxhp)+'\nMikstury: ' +str(mikstury)+'\nTrucizna: '+str(ilosc_trucizn)+'\nTarcza: '+str(tarcza))
              ruch = int(input('\nWrog: ' +str(nazwa1)+'\nHP: '+str(hp1)+'/'+str(mhp)+'\n\nWybierz akcje:\n1 - Atakuj'+emoji.emojize(':fist:', language='alias')+'\n2 - Wypij miksture'+emoji.emojize(':fire_extinguisher:', language='alias')+'\n3 - Rzuc trucizne'+emoji.emojize(':test_tube:', language='alias')+'\n4 - Uciekaj'+emoji.emojize(':leg:', language='alias')+'\n=>'))
              if ruch == 1:
                hp1 -= (random.randint(6,10)+obrazeniaD+obrazeniaT+obrazeniaW)
                print('Wykonujesz atak\n')
                print(emoji.emojize(':man:', language='alias'),end = ''),time.sleep(0.6),print('\U0001f5e1',end = ''),time.sleep(0.6),print(emoji.emojize(':ninja:', language='alias'),end = ''),print(emoji.emojize(':collision:', language='alias'),end = ''),time.sleep(0.6)
                print('\n\nRuch przeciwnika\n')
                if tarcza == 1:
                  uTarczy = int(input('Uzyc tarczy?\n1 - Tak\n2 - Nie\n=>'))
                  if uTarczy == 1:
                    print(emoji.emojize(':man:', language='alias'),end = ''),print(emoji.emojize(':shield:'),end = ''),time.sleep(0.6),print(emoji.emojize(':boomerang:', language='alias'),end = ''),print(emoji.emojize(' :ninja:', language='alias'),end = ''),time.sleep(0.6),print(emoji.emojize(':red_question_mark:', language='alias')),time.sleep(0.6)
                    runda += 1
                    tarcza -= 1
                    continue
                  else:
                   akthp -= ap1
                   print(emoji.emojize(':man:', language='alias'),end = ''),time.sleep(0.6),print(emoji.emojize(':collision:'),end = ''),print(emoji.emojize(':boomerang:', language='alias'),end = ''),print(emoji.emojize(' :ninja:', language='alias')),time.sleep(0.6)
                   runda += 1
                   continue
                else:
                  akthp -= ap1
                  print(emoji.emojize(':man:', language='alias'),end = ''),time.sleep(0.6),print(emoji.emojize(':collision:'),end = ''),print(emoji.emojize(':boomerang:', language='alias'),end = ''),print(emoji.emojize(' :ninja:', language='alias')),time.sleep(0.6)
                  runda += 1
                  continue
              elif ruch == 2 and mikstury>=1 and akthp<=(maxhp-15):
                akthp += 15
                mikstury -= 1
                print('Pijesz miksture\n')
                print(emoji.emojize(':man:', language='alias'),end = ''),print(emoji.emojize(':fire_extinguisher:', language='alias'),end = ''),time.sleep(0.6),print(emoji.emojize(':anger:', language='alias')),time.sleep(0.6)
                continue
              elif ruch == 2 and mikstury<1:
                print('Nie posiadasz mikstur')
                continue
              elif ruch == 2 and mikstury>=1 and akthp>(maxhp-15):
                print('Masz za duzo HP, nie mozesz wypic mikstury')
                continue
              elif ruch == 3 and ilosc_trucizn>=1:
                obrazeniaT += 3
                ilosc_trucizn -=1
                print(emoji.emojize(':man:', language='alias'),end = ''),time.sleep(0.6),print(emoji.emojize(':dashing_away:'),end = ''),time.sleep(0.6),print(emoji.emojize(':dashing_away:', language='alias'),end = ''),time.sleep(0.6),print(emoji.emojize(':test_tube:', language='alias'),end = ''),print(emoji.emojize(':collision:', language='alias'),end = ''),print(emoji.emojize(':ninja:', language='alias')),time.sleep(0.6)
                continue
              elif ruch == 3 and ilosc_trucizn<1:
                print('Nie posiadasz trucizn')
                continue
              elif ruch == 4:
                print('Uciekasz z areny\nWidownia nasmiewa sie z ciebie\nTracisz 10'+'% '+'EXPa\n')
                if maxexp*0.1<=exp:
                  exp = exp-(maxexp*0.1)
                  break
                else:
                  exp = 0
                  break
              else:
                print('\nPodano niewlasciowa liczbe')
            if akthp>0 and ruch!=4:
              print('\nWygrywasz walke! '+emoji.emojize(':sports_medal:', language='alias'))
              print('Otrzymane zloto: '+str(ozloto))
              print('Otrzymany EXP: '+str(oexp))
              zloto+=ozloto
              if oexp+exp>=maxexp:
                poziom += 1
                exp = 0
                maxexp += 50
                maxhp += 5
                akthp += 5
                print('Awansujesz na kolejny poziom! '+emoji.emojize(':sparkles:', language='alias'))
                continue
              else:
                exp+= oexp
                continue
            elif ruch ==4:
              continue
            else:
              print('\nZostajesz pokonany '+emoji.emojize(':skull:', language='alias')+'\n\nPrzegrywasz walke\n\nKONIEC GRY '+emoji.emojize(':crying_face:', language='alias'))
              koniec = int(input('\n1 - Zagraj od nowa\n2 - Wyjdz\n=>'))
              if koniec == 1:
                akthp = 100
                maxhp = 100
                zloto = 50
                poziom = 1
                exp = 0
                maxexp = 100
                mikstury = 2
                ilosc_trucizn = 0
                ilosc_mieczy = 0
                obrazeniaD = 0
                obrazeniaT = 0
                zbroja = 0
                tarcza = 0
                miecz = 'brak'
                continue
              else:
                exit
          elif wrog1 == 2:
            runda = 1
            hp1 = 175
            mhp = 175
            oexp = 180
            ozloto = 100
            obrazeniaT = 0
            nazwa1 = 'Slon'
            ap1 = random.randint(34,36)
            while hp1>0 and akthp>0:
              print('\nRunda '+str(runda))
              print('\nAktualne statystyki:\nHP: '+str(akthp)+'/'+str(maxhp)+'\nMikstury: ' +str(mikstury)+'\nTrucizna: '+str(ilosc_trucizn)+'\nTarcza: '+str(tarcza))
              ruch = int(input('\nWrog: ' +str(nazwa1)+'\nHP: '+str(hp1)+'/'+str(mhp)+'\n\nWybierz akcje:\n1 - Atakuj'+emoji.emojize(':fist:', language='alias')+'\n2 - Wypij miksture'+emoji.emojize(':fire_extinguisher:', language='alias')+'\n3 - Rzuc trucizne'+emoji.emojize(':test_tube:', language='alias')+'\n4 - Uciekaj'+emoji.emojize(':leg:', language='alias')+'\n=>'))
              if ruch == 1:
                hp1 -= (random.randint(6,10)+obrazeniaD+obrazeniaT+obrazeniaW)
                print('Wykonujesz atak\n')
                print(emoji.emojize(':man:', language='alias'),end = ''),time.sleep(0.6),print('\U0001f5e1',end = ''),time.sleep(0.6),print(emoji.emojize(':elephant:', language='alias'),end = ''),print(emoji.emojize(':collision:', language='alias'),end = ''),time.sleep(0.6)
                print('\n\nRuch przeciwnika\n')
                if tarcza == 1:
                  uTarczy = int(input('Uzyc tarczy?\n1 - Tak\n2 - Nie\n=>'))
                  if uTarczy == 1:
                    print(emoji.emojize(':man:', language='alias'),end = ''),print(emoji.emojize(':shield:'),end = ''),time.sleep(0.6),print(emoji.emojize(':collision:', language='alias'),end = ''),print(emoji.emojize(':elephant:', language='alias'),end = ''),time.sleep(0.6),print(emoji.emojize(':red_question_mark:', language='alias')),time.sleep(0.6)
                    runda += 1
                    tarcza -= 1
                    continue
                  else:
                   akthp -= ap1
                   print(emoji.emojize(':man:', language='alias'),end = ''),time.sleep(0.6),print(emoji.emojize(':collision:'),end = ''),print(emoji.emojize(':elephant:', language='alias')),time.sleep(0.6)
                   runda += 1
                   continue
                else:
                  akthp -= ap1
                  print(emoji.emojize(':man:', language='alias'),end = ''),time.sleep(0.6),print(emoji.emojize(':collision:'),end = ''),print(emoji.emojize(':elephant:', language='alias')),time.sleep(0.6)
                  runda += 1
                  continue
              elif ruch == 2 and mikstury>=1 and akthp<=(maxhp-15):
                akthp += 15
                mikstury -= 1
                print('Pijesz miksture\n')
                print(emoji.emojize(':man:', language='alias'),end = ''),print(emoji.emojize(':fire_extinguisher:', language='alias'),end = ''),time.sleep(0.6),print(emoji.emojize(':anger:', language='alias')),time.sleep(0.6)
                continue
              elif ruch == 2 and mikstury<1:
                print('Nie posiadasz mikstur')
                continue
              elif ruch == 2 and mikstury>=1 and akthp>(maxhp-15):
                print('Masz za duzo HP, nie mozesz wypic mikstury')
                continue
              elif ruch == 3 and ilosc_trucizn>=1:
                obrazeniaT += 3
                ilosc_trucizn -=1
                print(emoji.emojize(':man:', language='alias'),end = ''),time.sleep(0.6),print(emoji.emojize(':dashing_away:'),end = ''),time.sleep(0.6),print(emoji.emojize(':dashing_away:', language='alias'),end = ''),time.sleep(0.6),print(emoji.emojize(':test_tube:', language='alias'),end = ''),print(emoji.emojize(':collision:', language='alias'),end = ''),print(emoji.emojize(':elephant:', language='alias')),time.sleep(0.6)
                continue
              elif ruch == 3 and ilosc_trucizn<1:
                print('Nie posiadasz trucizn')
                continue
              elif ruch == 4:
                print('Uciekasz z areny\nWidownia nasmiewa sie z ciebie\nTracisz 10'+'% '+'EXPa\n')
                if maxexp*0.1<=exp:
                  exp = exp-(maxexp*0.1)
                  break
                else:
                  exp = 0
                  break
              else:
                print('\nPodano niewlasciowa liczbe')
            if akthp>0 and ruch!=4:
              print('\nWygrywasz walke! '+emoji.emojize(':sports_medal:', language='alias'))
              print('Otrzymane zloto: '+str(ozloto))
              print('Otrzymany EXP: '+str(oexp))
              zloto+=ozloto
              if oexp+exp>=maxexp:
                poziom += 1
                exp = 0
                maxexp += 50
                maxhp += 5
                akthp += 5
                print('Awansujesz na kolejny poziom! '+emoji.emojize(':sparkles:', language='alias'))
                continue
              else:
                exp+= oexp
                continue
            elif ruch ==4:
              continue
            else:
              print('\nZostajesz pokonany '+emoji.emojize(':skull:', language='alias')+'\n\nPrzegrywasz walke\n\nKONIEC GRY '+emoji.emojize(':crying_face:', language='alias'))
              koniec = int(input('\n1 - Zagraj od nowa\n2 - Wyjdz\n=>'))
              if koniec == 1:
                akthp = 100
                maxhp = 100
                zloto = 50
                poziom = 1
                exp = 0
                maxexp = 100
                mikstury = 2
                ilosc_trucizn = 0
                ilosc_mieczy = 0
                obrazeniaD = 0
                obrazeniaT = 0
                zbroja = 0
                tarcza = 0
                miecz = 'brak'
                continue
              else:
                exit 
          elif wrog1 == 3:
            runda = 1
            hp1 = 190
            mhp = 190
            oexp = 192
            ozloto = 108
            obrazeniaT = 0
            nazwa1 = 'Demon'
            ap1 = random.randint(37,39)
            while hp1>0 and akthp>0:
              print('\nRunda '+str(runda))
              print('\nAktualne statystyki:\nHP: '+str(akthp)+'/'+str(maxhp)+'\nMikstury: ' +str(mikstury)+'\nTrucizna: '+str(ilosc_trucizn)+'\nTarcza: '+str(tarcza))
              ruch = int(input('\nWrog: ' +str(nazwa1)+'\nHP: '+str(hp1)+'/'+str(mhp)+'\n\nWybierz akcje:\n1 - Atakuj'+emoji.emojize(':fist:', language='alias')+'\n2 - Wypij miksture'+emoji.emojize(':fire_extinguisher:', language='alias')+'\n3 - Rzuc trucizne'+emoji.emojize(':test_tube:', language='alias')+'\n4 - Uciekaj'+emoji.emojize(':leg:', language='alias')+'\n=>'))
              if ruch == 1:
                hp1 -= (random.randint(6,10)+obrazeniaD+obrazeniaT+obrazeniaW)
                print('Wykonujesz atak\n')
                print(emoji.emojize(':man:', language='alias'),end = ''),time.sleep(0.6),print('\U0001f5e1',end = ''),time.sleep(0.6),print(emoji.emojize(':ogre:'),end = ''),print(emoji.emojize(':collision:', language='alias'),end = ''),time.sleep(0.6)
                print('\n\nRuch przeciwnika\n')
                if tarcza == 1:
                  uTarczy = int(input('Uzyc tarczy?\n1 - Tak\n2 - Nie\n=>'))
                  if uTarczy == 1:
                    print(emoji.emojize(':man:', language='alias'),end = ''),print(emoji.emojize(':shield:'),end = ''),time.sleep(0.6),print('\U0001F531',end = ''),print(emoji.emojize(':ogre:'),end = ''),time.sleep(0.6),print(emoji.emojize(':red_question_mark:', language='alias')),time.sleep(0.6)
                    runda += 1
                    tarcza -= 1
                    continue
                  else:
                   akthp -= ap1
                   print(emoji.emojize(':man:', language='alias'),end = ''),time.sleep(0.6),print(emoji.emojize(':collision:'),end = ''),print('\U0001F531',end = ''),print(emoji.emojize(':ogre:'),end = ''),time.sleep(0.6)
                   runda += 1
                   continue
                else:
                  akthp -= ap1
                  print(emoji.emojize(':man:', language='alias'),end = ''),time.sleep(0.6),print(emoji.emojize(':collision:'),end = ''),print('\U0001F531',end = ''),print(emoji.emojize(':ogre:'),end = ''),time.sleep(0.6)
                  runda += 1
                  continue
              elif ruch == 2 and mikstury>=1 and akthp<=(maxhp-15):
                akthp += 15
                mikstury -= 1
                print('Pijesz miksture\n')
                print(emoji.emojize(':man:', language='alias'),end = ''),print(emoji.emojize(':fire_extinguisher:', language='alias'),end = ''),time.sleep(0.6),print(emoji.emojize(':anger:', language='alias')),time.sleep(0.6)
                continue
              elif ruch == 2 and mikstury<1:
                print('Nie posiadasz mikstur')
                continue
              elif ruch == 2 and mikstury>=1 and akthp>(maxhp-15):
                print('Masz za duzo HP, nie mozesz wypic mikstury')
                continue
              elif ruch == 3 and ilosc_trucizn>=1:
                obrazeniaT += 3
                ilosc_trucizn -=1
                print(emoji.emojize(':man:', language='alias'),end = ''),time.sleep(0.6),print(emoji.emojize(':dashing_away:'),end = ''),time.sleep(0.6),print(emoji.emojize(':dashing_away:', language='alias'),end = ''),time.sleep(0.6),print(emoji.emojize(':test_tube:', language='alias'),end = ''),print(emoji.emojize(':collision:', language='alias'),end = ''),print(emoji.emojize(':ogre:'),end = ''),time.sleep(0.6)
                continue
              elif ruch == 3 and ilosc_trucizn<1:
                print('Nie posiadasz trucizn')
                continue
              elif ruch == 4:
                print('Uciekasz z areny\nWidownia nasmiewa sie z ciebie\nTracisz 10'+'% '+'EXPa\n')
                if maxexp*0.1<=exp:
                  exp = exp-(maxexp*0.1)
                  break
                else:
                  exp = 0
                  break
              else:
                print('\nPodano niewlasciowa liczbe')
            if akthp>0 and ruch!=4:
              print('\nWygrywasz walke! '+emoji.emojize(':sports_medal:', language='alias'))
              print('Otrzymane zloto: '+str(ozloto))
              print('Otrzymany EXP: '+str(oexp))
              zloto+=ozloto
              trofeum4 = 1
              if oexp+exp>=maxexp:
                poziom += 1
                exp = 0
                maxexp += 50
                maxhp += 5
                akthp += 5
                print('Awansujesz na kolejny poziom! '+emoji.emojize(':sparkles:', language='alias'))
                continue
              else:
                exp+= oexp
                continue
            elif ruch ==4:
              continue
            else:
              print('\nZostajesz pokonany '+emoji.emojize(':skull:', language='alias')+'\n\nPrzegrywasz walke\n\nKONIEC GRY '+emoji.emojize(':crying_face:', language='alias'))
              koniec = int(input('\n1 - Zagraj od nowa\n2 - Wyjdz\n=>'))
              if koniec == 1:
                akthp = 100
                maxhp = 100
                zloto = 50
                poziom = 1
                exp = 0
                maxexp = 100
                mikstury = 2
                ilosc_trucizn = 0
                ilosc_mieczy = 0
                obrazeniaD = 0
                obrazeniaT = 0
                zbroja = 0
                tarcza = 0
                miecz = 'brak'
                continue
              else:
                exit
          elif wrog1 == 4:
            continue
          else:
            print('Podano niewlasciowa liczbe')
            continue
        elif arena == 4 and poziom <16:
          print('Masz za niski poziom zeby walczyc na tej arenie')
          continue
        elif arena == 5 and poziom>=22:
          wrog1 = int(input('Wybierz przeciwinika:\n(Sortowane od najprostszego do najtrudniejszego)\n1 - Czarodziej'+emoji.emojize(':mage:', language='alias')+'\n2 - Smok'+emoji.emojize(':dragon:', language='alias')+'\n3 - Krolewski Pretendent'+emoji.emojize(':supervillain:',language='alias')+'\n4 - Wyjscie\n=>'))
          if wrog1 == 1:
            runda = 1
            hp1 = 200
            mhp = 200
            oexp = 205
            ozloto = 120
            obrazeniaT = 0
            nazwa1 = 'Ninja'
            ap1 = random.randint(40,42)
            while hp1>0 and akthp>0:
              print('\nRunda '+str(runda))
              print('\nAktualne statystyki:\nHP: '+str(akthp)+'/'+str(maxhp)+'\nMikstury: ' +str(mikstury)+'\nTrucizna: '+str(ilosc_trucizn)+'\nTarcza: '+str(tarcza))
              ruch = int(input('\nWrog: ' +str(nazwa1)+'\nHP: '+str(hp1)+'/'+str(mhp)+'\n\nWybierz akcje:\n1 - Atakuj'+emoji.emojize(':fist:', language='alias')+'\n2 - Wypij miksture'+emoji.emojize(':fire_extinguisher:', language='alias')+'\n3 - Rzuc trucizne'+emoji.emojize(':test_tube:', language='alias')+'\n4 - Uciekaj'+emoji.emojize(':leg:', language='alias')+'\n=>'))
              if ruch == 1:
                hp1 -= (random.randint(6,10)+obrazeniaD+obrazeniaT+obrazeniaW)
                print('Wykonujesz atak\n')
                print(emoji.emojize(':man:', language='alias'),end = ''),time.sleep(0.6),print('\U0001f5e1',end = ''),time.sleep(0.6),print(emoji.emojize(':mage:', language='alias'),end = ''),print(emoji.emojize(':collision:', language='alias'),end = ''),time.sleep(0.6)
                print('\n\nRuch przeciwnika\n')
                if tarcza == 1:
                  uTarczy = int(input('Uzyc tarczy?\n1 - Tak\n2 - Nie\n=>'))
                  if uTarczy == 1:
                    print(emoji.emojize(':man:', language='alias'),end = ''),print(emoji.emojize(':shield:'),end = ''),time.sleep(0.6),print(emoji.emojize(':high_voltage:', language='alias'),end = ''),print(emoji.emojize(':mage:', language='alias'),end = ''),time.sleep(0.6),print(emoji.emojize(':red_question_mark:', language='alias')),time.sleep(0.6)
                    runda += 1
                    tarcza -= 1
                    continue
                  else:
                   akthp -= ap1
                   print(emoji.emojize(':man:', language='alias'),end = ''),time.sleep(0.6),print(emoji.emojize(':collision:'),end = ''),print(emoji.emojize(':high_voltage:', language='alias'),end = ''),print(emoji.emojize(':mage:', language='alias')),time.sleep(0.6)
                   runda += 1
                   continue
                else:
                  akthp -= ap1
                  print(emoji.emojize(':man:', language='alias'),end = ''),time.sleep(0.6),print(emoji.emojize(':collision:'),end = ''),print(emoji.emojize(':high_voltage:', language='alias'),end = ''),print(emoji.emojize(':mage:', language='alias')),time.sleep(0.6)
                  runda += 1
                  continue
              elif ruch == 2 and mikstury>=1 and akthp<=(maxhp-15):
                akthp += 15
                mikstury -= 1
                print('Pijesz miksture\n')
                print(emoji.emojize(':man:', language='alias'),end = ''),print(emoji.emojize(':fire_extinguisher:', language='alias'),end = ''),time.sleep(0.6),print(emoji.emojize(':anger:', language='alias')),time.sleep(0.6)
                continue
              elif ruch == 2 and mikstury<1:
                print('Nie posiadasz mikstur')
                continue
              elif ruch == 2 and mikstury>=1 and akthp>(maxhp-15):
                print('Masz za duzo HP, nie mozesz wypic mikstury')
                continue
              elif ruch == 3 and ilosc_trucizn>=1:
                obrazeniaT += 3
                ilosc_trucizn -=1
                print(emoji.emojize(':man:', language='alias'),end = ''),time.sleep(0.6),print(emoji.emojize(':dashing_away:'),end = ''),time.sleep(0.6),print(emoji.emojize(':dashing_away:', language='alias'),end = ''),time.sleep(0.6),print(emoji.emojize(':test_tube:', language='alias'),end = ''),print(emoji.emojize(':collision:', language='alias'),end = ''),print(emoji.emojize(':mage:', language='alias')),time.sleep(0.6)
                continue
              elif ruch == 3 and ilosc_trucizn<1:
                print('Nie posiadasz trucizn')
                continue
              elif ruch == 4:
                print('Uciekasz z areny\nWidownia nasmiewa sie z ciebie\nTracisz 10'+'% '+'EXPa\n')
                if maxexp*0.1<=exp:
                  exp = exp-(maxexp*0.1)
                  break
                else:
                  exp = 0
                  break
              else:
                print('\nPodano niewlasciowa liczbe')
            if akthp>0 and ruch!=4:
              print('\nWygrywasz walke! '+emoji.emojize(':sports_medal:', language='alias'))
              print('Otrzymane zloto: '+str(ozloto))
              print('Otrzymany EXP: '+str(oexp))
              zloto+=ozloto
              if oexp+exp>=maxexp:
                poziom += 1
                exp = 0
                maxexp += 50
                maxhp += 5
                akthp += 5
                print('Awansujesz na kolejny poziom! '+emoji.emojize(':sparkles:', language='alias'))
                continue
              else:
                exp+= oexp
                continue
            elif ruch ==4:
              continue
            else:
              print('\nZostajesz pokonany '+emoji.emojize(':skull:', language='alias')+'\n\nPrzegrywasz walke\n\nKONIEC GRY '+emoji.emojize(':crying_face:', language='alias'))
              koniec = int(input('\n1 - Zagraj od nowa\n2 - Wyjdz\n=>'))
              if koniec == 1:
                akthp = 100
                maxhp = 100
                zloto = 50
                poziom = 1
                exp = 0
                maxexp = 100
                mikstury = 2
                ilosc_trucizn = 0
                ilosc_mieczy = 0
                obrazeniaD = 0
                obrazeniaT = 0
                zbroja = 0
                tarcza = 0
                miecz = 'brak'
                continue
              else:
                exit
          elif wrog1 == 2:
            runda = 1
            hp1 = 225
            mhp = 225
            oexp = 220
            ozloto = 132
            obrazeniaT = 0
            nazwa1 = 'Smok'
            ap1 = random.randint(44,47)
            while hp1>0 and akthp>0:
              print('\nRunda '+str(runda))
              print('\nAktualne statystyki:\nHP: '+str(akthp)+'/'+str(maxhp)+'\nMikstury: ' +str(mikstury)+'\nTrucizna: '+str(ilosc_trucizn)+'\nTarcza: '+str(tarcza))
              ruch = int(input('\nWrog: ' +str(nazwa1)+'\nHP: '+str(hp1)+'/'+str(mhp)+'\n\nWybierz akcje:\n1 - Atakuj'+emoji.emojize(':fist:', language='alias')+'\n2 - Wypij miksture'+emoji.emojize(':fire_extinguisher:', language='alias')+'\n3 - Rzuc trucizne'+emoji.emojize(':test_tube:', language='alias')+'\n4 - Uciekaj'+emoji.emojize(':leg:', language='alias')+'\n=>'))
              if ruch == 1:
                hp1 -= (random.randint(6,10)+obrazeniaD+obrazeniaT+obrazeniaW)
                print('Wykonujesz atak\n')
                print(emoji.emojize(':man:', language='alias'),end = ''),time.sleep(0.6),print('\U0001f5e1',end = ''),time.sleep(0.6),print(emoji.emojize(':dragon:', language='alias'),end = ''),print(emoji.emojize(':collision:', language='alias'),end = ''),time.sleep(0.6)
                print('\n\nRuch przeciwnika\n')
                if tarcza == 1:
                  uTarczy = int(input('Uzyc tarczy?\n1 - Tak\n2 - Nie\n=>'))
                  if uTarczy == 1:
                    print(emoji.emojize(':man:', language='alias'),end = ''),print(emoji.emojize(':shield:'),end = ''),time.sleep(0.6),print(emoji.emojize(':collision:', language='alias'),end = ''),print(emoji.emojize(':comet:', language='alias'),end = ''),print(emoji.emojize(':dragon:', language='alias'),end = ''),time.sleep(0.6),print(emoji.emojize(':red_question_mark:', language='alias')),time.sleep(0.6)
                    runda += 1
                    tarcza -= 1
                    continue
                  else:
                   akthp -= ap1
                   print(emoji.emojize(':man:', language='alias'),end = ''),time.sleep(0.6),print(emoji.emojize(':collision:'),end = ''),print(emoji.emojize(':comet:', language='alias'),end = ''),print(emoji.emojize(':dragon:', language='alias')),time.sleep(0.6)
                   runda += 1
                   continue
                else:
                  akthp -= ap1
                  print(emoji.emojize(':man:', language='alias'),end = ''),time.sleep(0.6),print(emoji.emojize(':collision:'),end = ''),print(emoji.emojize(':comet:', language='alias'),end = ''),print(emoji.emojize(':dragon:', language='alias')),time.sleep(0.6)
                  runda += 1
                  continue
              elif ruch == 2 and mikstury>=1 and akthp<=(maxhp-15):
                akthp += 15
                mikstury -= 1
                print('Pijesz miksture\n')
                print(emoji.emojize(':man:', language='alias'),end = ''),print(emoji.emojize(':fire_extinguisher:', language='alias'),end = ''),time.sleep(0.6),print(emoji.emojize(':anger:', language='alias')),time.sleep(0.6)
                continue
              elif ruch == 2 and mikstury<1:
                print('Nie posiadasz mikstur')
                continue
              elif ruch == 2 and mikstury>=1 and akthp>(maxhp-15):
                print('Masz za duzo HP, nie mozesz wypic mikstury')
                continue
              elif ruch == 3 and ilosc_trucizn>=1:
                obrazeniaT += 3
                ilosc_trucizn -=1
                print(emoji.emojize(':man:', language='alias'),end = ''),time.sleep(0.6),print(emoji.emojize(':dashing_away:'),end = ''),time.sleep(0.6),print(emoji.emojize(':dashing_away:', language='alias'),end = ''),time.sleep(0.6),print(emoji.emojize(':test_tube:', language='alias'),end = ''),print(emoji.emojize(':collision:', language='alias'),end = ''),print(emoji.emojize(':dragon:', language='alias')),time.sleep(0.6)
                continue
              elif ruch == 3 and ilosc_trucizn<1:
                print('Nie posiadasz trucizn')
                continue
              elif ruch == 4:
                print('Uciekasz z areny\nWidownia nasmiewa sie z ciebie\nTracisz 10'+'% '+'EXPa\n')
                if maxexp*0.1<=exp:
                  exp = exp-(maxexp*0.1)
                  break
                else:
                  exp = 0
                  break
              else:
                print('\nPodano niewlasciowa liczbe')
            if akthp>0 and ruch!=4:
              print('\nWygrywasz walke! '+emoji.emojize(':sports_medal:', language='alias'))
              print('Otrzymane zloto: '+str(ozloto))
              print('Otrzymany EXP: '+str(oexp))
              zloto+=ozloto
              if oexp+exp>=maxexp:
                poziom += 1
                exp = 0
                maxexp += 50
                maxhp += 5
                akthp += 5
                print('Awansujesz na kolejny poziom! '+emoji.emojize(':sparkles:', language='alias'))
                continue
              else:
                exp+= oexp
                continue
            elif ruch ==4:
              continue
            else:
              print('\nZostajesz pokonany '+emoji.emojize(':skull:', language='alias')+'\n\nPrzegrywasz walke\n\nKONIEC GRY '+emoji.emojize(':crying_face:', language='alias'))
              koniec = int(input('\n1 - Zagraj od nowa\n2 - Wyjdz\n=>'))
              if koniec == 1:
                akthp = 100
                maxhp = 100
                zloto = 50
                poziom = 1
                exp = 0
                maxexp = 100
                mikstury = 2
                ilosc_trucizn = 0
                ilosc_mieczy = 0
                obrazeniaD = 0
                obrazeniaT = 0
                zbroja = 0
                tarcza = 0
                miecz = 'brak'
                continue
              else:
                exit 
          elif wrog1 == 3:
            runda = 1
            hp1 = 255
            mhp = 255
            oexp = 240
            ozloto = 150
            obrazeniaT = 0
            nazwa1 = 'Krolewski Pretendent'
            ap1 = random.randint(49,52)
            while hp1>0 and akthp>0:
              print('\nRunda '+str(runda))
              print('\nAktualne statystyki:\nHP: '+str(akthp)+'/'+str(maxhp)+'\nMikstury: ' +str(mikstury)+'\nTrucizna: '+str(ilosc_trucizn)+'\nTarcza: '+str(tarcza))
              ruch = int(input('\nWrog: ' +str(nazwa1)+'\nHP: '+str(hp1)+'/'+str(mhp)+'\n\nWybierz akcje:\n1 - Atakuj'+emoji.emojize(':fist:', language='alias')+'\n2 - Wypij miksture'+emoji.emojize(':fire_extinguisher:', language='alias')+'\n3 - Rzuc trucizne'+emoji.emojize(':test_tube:', language='alias')+'\n4 - Uciekaj'+emoji.emojize(':leg:', language='alias')+'\n=>'))
              if ruch == 1:
                hp1 -= (random.randint(6,10)+obrazeniaD+obrazeniaT+obrazeniaW)
                print('Wykonujesz atak\n')
                print(emoji.emojize(':man:', language='alias'),end = ''),time.sleep(0.6),print('\U0001f5e1',end = ''),time.sleep(0.6),print(emoji.emojize(':supervillain:'),end = ''),print(emoji.emojize(':collision:', language='alias'),end = ''),time.sleep(0.6)
                print('\n\nRuch przeciwnika\n')
                if tarcza == 1:
                  uTarczy = int(input('Uzyc tarczy?\n1 - Tak\n2 - Nie\n=>'))
                  if uTarczy == 1:
                    print(emoji.emojize(':man:', language='alias'),end = ''),print(emoji.emojize(':shield:'),end = ''),time.sleep(0.6),print('\U0001F529',end = ''),print(emoji.emojize(':supervillain:'),end = ''),time.sleep(0.6),print(emoji.emojize(':red_question_mark:', language='alias')),time.sleep(0.6)
                    runda += 1
                    tarcza -= 1
                    continue
                  else:
                   akthp -= ap1
                   print(emoji.emojize(':man:', language='alias'),end = ''),time.sleep(0.6),print(emoji.emojize(':collision:'),end = ''),print('\U0001F529',end = ''),print(emoji.emojize(':supervillain:'),end = ''),time.sleep(0.6)
                   runda += 1
                   continue
                else:
                  akthp -= ap1
                  print(emoji.emojize(':man:', language='alias'),end = ''),time.sleep(0.6),print(emoji.emojize(':collision:'),end = ''),print('\U0001F529',end = ''),print(emoji.emojize(':supervillain:'),end = ''),time.sleep(0.6)
                  runda += 1
                  continue
              elif ruch == 2 and mikstury>=1 and akthp<=(maxhp-15):
                akthp += 15
                mikstury -= 1
                print('Pijesz miksture\n')
                print(emoji.emojize(':man:', language='alias'),end = ''),print(emoji.emojize(':fire_extinguisher:', language='alias'),end = ''),time.sleep(0.6),print(emoji.emojize(':anger:', language='alias')),time.sleep(0.6)
                continue
              elif ruch == 2 and mikstury<1:
                print('Nie posiadasz mikstur')
                continue
              elif ruch == 2 and mikstury>=1 and akthp>(maxhp-15):
                print('Masz za duzo HP, nie mozesz wypic mikstury')
                continue
              elif ruch == 3 and ilosc_trucizn>=1:
                obrazeniaT += 3
                ilosc_trucizn -=1
                print(emoji.emojize(':man:', language='alias'),end = ''),time.sleep(0.6),print(emoji.emojize(':dashing_away:'),end = ''),time.sleep(0.6),print(emoji.emojize(':dashing_away:', language='alias'),end = ''),time.sleep(0.6),print(emoji.emojize(':test_tube:', language='alias'),end = ''),print(emoji.emojize(':collision:', language='alias'),end = ''),print(emoji.emojize(':supervillain:'),end = ''),time.sleep(0.6)
                continue
              elif ruch == 3 and ilosc_trucizn<1:
                print('Nie posiadasz trucizn')
                continue
              elif ruch == 4:
                print('Uciekasz z areny\nWidownia nasmiewa sie z ciebie\nTracisz 10'+'% '+'EXPa\n')
                if maxexp*0.1<=exp:
                  exp = exp-(maxexp*0.1)
                  break
                else:
                  exp = 0
                  break
              else:
                print('\nPodano niewlasciowa liczbe')
            if akthp>0 and ruch!=4:
              print('\nWygrywasz walke! '+emoji.emojize(':sports_medal:', language='alias'))
              print('\nZostajesz Nowym Pretendentem Areny!')
              print('Otrzymane zloto: '+str(ozloto))
              print('Otrzymany EXP: '+str(oexp))
              zloto+=ozloto
              trofeum5 = 1
              if oexp+exp>=maxexp:
                poziom += 1
                exp = 0
                maxexp += 50
                maxhp += 5
                akthp += 5
                print('Awansujesz na kolejny poziom! '+emoji.emojize(':sparkles:', language='alias'))
                continue
              else:
                exp+= oexp
                continue
            elif ruch ==4:
              continue
            else:
              print('\nZostajesz pokonany '+emoji.emojize(':skull:', language='alias')+'\n\nPrzegrywasz walke\n\nKONIEC GRY '+emoji.emojize(':crying_face:', language='alias'))
              koniec = int(input('\n1 - Zagraj od nowa\n2 - Wyjdz\n=>'))
              if koniec == 1:
                akthp = 100
                maxhp = 100
                zloto = 50
                poziom = 1
                exp = 0
                maxexp = 100
                mikstury = 2
                ilosc_trucizn = 0
                ilosc_mieczy = 0
                obrazeniaD = 0
                obrazeniaT = 0
                zbroja = 0
                tarcza = 0
                miecz = 'brak'
                continue
              else:
                exit
          elif wrog1 == 4:
            continue
          else:
            print('Podano niewlasciowa liczbe')
            continue
        elif arena == 5 and poziom <1:
          print('Masz za niski poziom zeby walczyc na tej arenie')
          continue
        elif arena == 6:
          continue
        else: print('Podano niewlasciowa liczbe')
       elif docelowe == 4:
         if poziom >=5:
           print('\nRynek miasta'+emoji.emojize(':fountain:', language='alias')+'\nWybierz aktywnosc:')
           miasto = int(input('1 - Mieszkanie'+emoji.emojize(':house:', language='alias')+'\n2 - Sklep wiedzmy'+emoji.emojize(':japanese_castle:', language='alias')+'\n3 - Wyjscie'+emoji.emojize(':cross_mark:', language='alias')+'\n=>'))
           if miasto == 1 and mieszkanie != 1:
             print('\nMieszkanie')
             kupM = int(input('1 - Kup mieszkanie - 500 szt. zlota\n(mozliwosc regeneracji HP za darmo, a takze tansze wytwarzanie mikstur)\n2 - Wyjscie'+emoji.emojize(':cross_mark:', language='alias')+'\n=>'))
             if kupM == 1 and zloto >=500:
               print('Zakupiles mieszkanie!')
               zloto -= 500
               mieszkanie = 1
               continue
             elif kupM == 1 and zloto<500:
               print('Masz za malo zlota')
               continue
             elif kupM == 2:
               continue
             else: print('Podano niewlasciwa liczbe')
             continue
           elif miasto == 1 and mieszkanie == 1:
             print('\nMieszkanie')
             mA = int(input('1 - Idz spac\n2 - Wytworz domowe mikstury - 1 szt. zlota\n3 - Spojrz na trofea\n4 - Wyjscie'+emoji.emojize(':cross_mark:', language='alias')+'\n=>'))
             if mA == 1 and akthp!=maxhp:
               akthp += random.randint(5,90)
               print('\n'+emoji.emojize(':bed:', language='alias'),end =''),time.sleep(0.6),print(('\U0001f4a4'),end = ''),time.sleep(0.6),print(('\U0001f4a4'),end = ''),time.sleep(0.6),print(('\U0001f4a4'),end = ''),time.sleep(0.6),print('\U0001f4a4'),time.sleep(0.6)
               if akthp>maxhp:
                 akthp = akthp-(akthp-maxhp)
                 continue
               else: continue
             elif mA == 1 and akthp==maxhp:
               print('Masz maksymalna liczbe HP')
             elif mA == 2 and zloto >= 1 and mikstury < 2:
               mikstury += 1
               zloto -= 1
               print('Wytworzono miksture')
               continue
             elif mA == 2 and zloto <= 1:
               print('Masz za malo zlota')
               continue
             elif mA == 2 and mikstury >= 2:
               print('Masz maksymalna liczbe mikstur')
               continue
             elif mA == 3:
               if trofeum1 == 1:
                 print(('\U0001F949'),end ='')
               else: print(end = '')
               if trofeum2 == 1:
                 print(('\U0001F948'),end ='')
               else: print(end = '')
               if trofeum3 == 1:
                 print(('\U0001F3C5'),end ='')
               else: print(end = '')
               if trofeum4 == 1:
                 print(('\U0001F3C6'),end ='')
               else: print(end = '')
               if trofeum5 == 1:
                 print(emoji.emojize(':crown:', language='alias'),end ='')
               else: print(end = '')
               if trofeum1 == 0 and trofeum2 == 0 and trofeum3 == 0 and trofeum4 == 0 and trofeum5 == 0:
                 print('\nNie posiadasz jeszcze zadnych trofeow')
                 continue
               elif trofeum1 == 0 or trofeum2 == 0 or trofeum3 == 0 or trofeum4 == 0 or trofeum5 == 0:
                 trof = int(input('\n1 - Wyjscie'+emoji.emojize(':cross_mark:', language='alias')+'\n=>'))
                 if trof == 1:
                   continue
                 else: continue
               else: continue  
             elif mA == 4:
               continue
             else:
               print('Podano niewlasciwa liczbe')
               continue
           elif miasto == 2:
             wiedzma = int(input('\nSklep wiedzmy\n1 - Magiczny miecz - 199 szt. zlota\n2 - Starozytny miecz - 320 szt. zlota\n3 - Boski miecz - 480 szt. zlota\n4 - Ognik - 30 szt. zlota\nOgnik zwieksza obrazenia miecza (lub piesci) nakladajac na przeciwnika efekt podpalenia.\nOgniki zadaja obrazenia w kazdej rundzie.\nMozna kupowac wielokrotnie.\n5 - Jaszczur - 260 szt. zlota\nTowarzyszy Ci podczas walki.\nZadaje dodatkowe obrazenia w kazdej rundzie.\nMozna kupic tylko raz\n6 - Wyjscie'+emoji.emojize(':cross_mark:', language='alias')+'\n=>'))
             if wiedzma==1 and ilosc_mieczy==0 and zloto>=199:
               obrazeniaD = 23
               zloto-=199
               ilosc_mieczy += 1
               miecz = 4
               print('Zakupiono Magiczny miecz')
               continue
             elif wiedzma == 2 and ilosc_mieczy==0 and zloto>=320:
               obrazeniaD = 36
               zloto-=320
               ilosc_mieczy += 1
               miecz = 5
               print('Zakupiono Starozytny miecz')
               continue
             elif wiedzma == 3 and ilosc_mieczy==0 and zloto>=480:
               obrazeniaD = 50
               zloto-=480
               ilosc_mieczy += 1
               miecz = 6
               print('Zakupiono Boski miecz')
               continue
             elif wiedzma == 4 and zloto>=30:
               obrazeniaW += 2
               zloto -= 30
               print('Zakupiono Ognika')
               continue
             elif (wiedzma == 1 or wiedzma == 2 or wiedzma == 3) and ilosc_mieczy==1:
               print('Posiadasz juz miecz. Sprzedaj go, aby zakupic inny')
               continue
             elif wiedzma == 5 and zloto>=260 and jaszczur == 0:
               obrazeniaW += 20
               zloto -= 260
               jaszczur = 1
               continue
             elif wiedzma == 5 and jaszczur == 1:
               print('Posiadasz juz Jaszczura')
               continue
             elif wiedzma == 6:
               continue
             else: print('Podano niewlasciwa liczbe lub masz za malo zlota')
             continue
           else: print('Podano niewlasciwa liczbe')
           continue
         else: print('Masz za niski poziom (Wymagany poziom: 5)')
         continue
       elif docelowe==5:
           with open("zapis.pkl","wb") as f:
               pickle.dump(akthp,f)
               pickle.dump(maxhp,f)
               pickle.dump(zloto,f)
               pickle.dump(poziom,f)
               pickle.dump(exp,f)
               pickle.dump(maxexp,f)
               pickle.dump(mikstury,f)
               pickle.dump(ilosc_trucizn,f)
               pickle.dump(ilosc_mieczy,f)
               pickle.dump(obrazeniaD,f)
               pickle.dump(obrazeniaT,f)
               pickle.dump(obrazeniaW,f)
               pickle.dump(zbroja,f)
               pickle.dump(tarcza,f)
               pickle.dump(miecz,f)
               pickle.dump(mieszkanie,f)
               pickle.dump(trofeum1,f)
               pickle.dump(trofeum2,f)
               pickle.dump(trofeum3,f)
               pickle.dump(trofeum4,f)
               pickle.dump(trofeum5,f)
               pickle.dump(jaszczur,f)
               print("\nGra zostala zapisana")
               continue 
       elif docelowe==6:
         exit1 = int(input('Czy na pewno chcesz wyjsc?\nUtracisz wszystkie niezapisane postepy.\n1 - Tak\n2 - Nie\n=>'))
         if exit1 == 1:
           sys.exit()
         else: continue      
       else:
         print('Podano niewlasciowa liczbe')
         continue
       break