import random
import time
import emoji
import sys
import os
import pickle

trofeum1 = 0
trofeum2 = 0
trofeum3 = 0
trofeum4 = 0
trofeum5 = 0

def safe_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            cls()
            print("Podano nieprawidlowa wartosc. Wprowadz liczbe.")

def get_emoji(nazwa1):
    emoji_map = {
        'Jednoreki bandyta': ':person_pouting:',
        'Wilk': ':wolf:',
        'Pijany kowal': ':old_man:',
        'Zly Wiesniak': ':farmer:',
        'Puma': ':leopard:',
        'Rzeznik': ':man_cook:',
        'Gladiator': ':guard:',
        'Niedzwiedz': ':bear:',
        'Troll': '\U0001f9cc',
        'Ninja': ':ninja:',
        'Slon': ':elephant:',
        'Demon': ':ogre:',
        'Czarodziej': ':mage:',
        'Smok': ':dragon:',
        'Krolewski Pretendent': ':supervillain:'
    }
    return emoji_map.get(nazwa1, ':question:')

def get_weapon_emoji(nazwa1):
    weapon_map = {
        'Jednoreki bandyta': emoji.emojize(':hammer:', language='alias'),
        'Wilk': '',
        'Pijany kowal': '\U0001F529',
        'Zly Wiesniak': emoji.emojize(':pick:', language='alias'),
        'Puma': '',
        'Rzeznik': '\U0001FA9A',
        'Gladiator': emoji.emojize(':axe:', language='alias'),
        'Niedzwiedz': '',
        'Troll': emoji.emojize(':hammer:', language='alias'),
        'Ninja': emoji.emojize(':boomerang:', language='alias'),
        'Slon': '',
        'Demon': '\U0001F531',
        'Czarodziej': emoji.emojize(':high_voltage:', language='alias'),
        'Smok': emoji.emojize(':comet:', language='alias'),
        'Krolewski Pretendent': '\U0001F529'
    }
    return weapon_map.get(nazwa1, '')


def walka(akthp, maxhp, mikstury, ilosc_trucizn, tarcza, obrazeniaD, obrazeniaW, poziom, exp, maxexp, zloto, 
          nazwa1, hp1, mhp, ap1_min, ap1_max, oexp, ozloto, trofeumNumer, trofeum=None):
    runda = 1
    obrazeniaT = 0
    ap1 = random.randint(ap1_min, ap1_max)
    
    while hp1 > 0 and akthp > 0:
        print('\nRunda ' + str(runda))
        print('\nAktualne statystyki:\nHP: ' + str(akthp) + '/' + str(maxhp) + emoji.emojize(':red_heart:', language='alias') +
              '\nMikstury: ' + str(mikstury) + emoji.emojize(':fire_extinguisher:', language='alias')+ '\nTrucizna: ' + str(ilosc_trucizn) + emoji.emojize(':test_tube:', language='alias') +
              '\nTarcza: ' + str(tarcza) + emoji.emojize(':shield:', language='alias'))
        
        ruch = int(safe_input('\nWrog: ' + str(nazwa1) + '\nHP: ' + str(hp1) + '/' + str(mhp) + emoji.emojize(':red_heart:', language='alias') +
                     '\n\nWybierz akcje:\n1 - Atakuj' + emoji.emojize(':fist:', language='alias') + 
                     '\n2 - Wypij miksture' + emoji.emojize(':fire_extinguisher:', language='alias') + 
                     '\n3 - Rzuc trucizne' + emoji.emojize(':test_tube:', language='alias') + 
                     '\n4 - Uciekaj' + emoji.emojize(':leg:', language='alias') + '\n=>'))
        
        if ruch == 1:
            cls()
            hp1 -= (random.randint(6, 10) + obrazeniaD + obrazeniaT + obrazeniaW)
            print('Wykonujesz atak\n')
            print(emoji.emojize(':man:', language='alias'), end=''), time.sleep(0.5)
            print('\U0001f5e1', end=''), time.sleep(0.5)
            print(emoji.emojize(get_emoji(nazwa1), language='alias'), end='')
            print(emoji.emojize(':collision:', language='alias'), end=''), time.sleep(0.5)
            
            print('\n\nRuch przeciwnika\n')
            if tarcza == 1:
                uTarczy = int(safe_input('Uzyc tarczy?\n1 - Tak\n2 - Nie\n=>'))
                if uTarczy == 1:
                    print(emoji.emojize(':man:', language='alias'), end='')
                    print(emoji.emojize(':shield:'), end=''), time.sleep(0.5)
                    print(get_weapon_emoji(nazwa1), end='')
                    print(emoji.emojize(get_emoji(nazwa1), language='alias'), end=''), time.sleep(0.5)
                    print(emoji.emojize(':red_question_mark:', language='alias')), time.sleep(0.5)
                    runda += 1
                    tarcza -= 1
                    continue
                else:
                    akthp -= ap1
                    print(emoji.emojize(':man:', language='alias'), end=''), time.sleep(0.5)
                    print(emoji.emojize(':collision:'), end='')
                    print(get_weapon_emoji(nazwa1), end='')
                    print(emoji.emojize(get_emoji(nazwa1), language='alias')), time.sleep(0.5)
                    runda += 1
                    continue
            else:
                akthp -= ap1
                print(emoji.emojize(':man:', language='alias'), end=''), time.sleep(0.5)
                print(emoji.emojize(':collision:'), end='')
                print(get_weapon_emoji(nazwa1), end='')
                print(emoji.emojize(get_emoji(nazwa1), language='alias')), time.sleep(0.5)
                runda += 1
                continue
                
        elif ruch == 2 and mikstury >= 1 and akthp <= (maxhp - 15):
            cls()
            akthp += 15
            mikstury -= 1
            print('Pijesz miksture\n')
            print(emoji.emojize(':man:', language='alias'), end='')
            print(emoji.emojize(':fire_extinguisher:', language='alias'), end=''), time.sleep(0.5)
            print(emoji.emojize(':anger:', language='alias')), time.sleep(0.5)
            continue
            
        elif ruch == 2 and mikstury < 1:
            cls()
            print('Nie posiadasz mikstur')
            continue
            
        elif ruch == 2 and mikstury >= 1 and akthp > (maxhp - 15):
            cls()
            print('Masz za duzo HP, nie mozesz wypic mikstury')
            continue
            
        elif ruch == 3 and ilosc_trucizn >= 1:
            cls()
            obrazeniaT += 3
            ilosc_trucizn -= 1
            print(emoji.emojize(':man:', language='alias'), end=''), time.sleep(0.6)
            print(emoji.emojize(':dashing_away:'), end=''), time.sleep(0.6)
            print(emoji.emojize(':dashing_away:', language='alias'), end=''), time.sleep(0.6)
            print(emoji.emojize(':test_tube:', language='alias'), end='')
            print(emoji.emojize(':collision:', language='alias'), end='')
            print(emoji.emojize(get_emoji(nazwa1), language='alias')), time.sleep(0.6)
            continue
            
        elif ruch == 3 and ilosc_trucizn < 1:
            cls()
            print('Nie posiadasz trucizn')
            continue
            
        elif ruch == 4:
            cls()
            print('Uciekasz z areny\nWidownia nasmiewa sie z ciebie\nTracisz 10% EXPa')
            if maxexp * 0.1 <= exp:
                exp = exp - (maxexp * 0.1)
                return akthp, mikstury, ilosc_trucizn, tarcza, poziom, exp, zloto, maxexp, maxhp, True
            else:
                exp = 0
                return akthp, mikstury, ilosc_trucizn, tarcza, poziom, exp, zloto, maxexp, maxhp, True
        else:
            cls()
            print('\nPodano niewlasciowa liczbe')
    
    if akthp > 0 and ruch != 4:
        cls()
        print('\nWygrywasz walke! ' + emoji.emojize(':sports_medal:', language='alias'))
        if trofeum is not None:
            print('\n' + trofeum)
            if trofeumNumer==1:
              global trofeum1
              trofeum1 = 1
            elif trofeumNumer==2:
              global trofeum2
              trofeum2 = 1
            elif trofeumNumer==3:
              global trofeum3
              trofeum3 = 1
            elif trofeumNumer==4:
              global trofeum4
              trofeum4 = 1
            elif trofeumNumer==5:
              global trofeum5
              trofeum5 = 1
        print('Otrzymane zloto: ' + str(ozloto))
        print('Otrzymany EXP: ' + str(oexp))
        zloto += ozloto
        
        if oexp + exp >= maxexp:
            poziom += 1
            exp = 0
            maxexp += 50
            maxhp += 5
            akthp += 5
            print('Awansujesz na kolejny poziom! ' + emoji.emojize(':sparkles:', language='alias'))
        else:
            exp += oexp
            
        return akthp, mikstury, ilosc_trucizn, tarcza, poziom, exp, zloto, maxexp, maxhp, True
        
    elif ruch == 4:
        return akthp, mikstury, ilosc_trucizn, tarcza, poziom, exp, zloto, maxexp, maxhp, True
        
    else:
        cls()
        print('\nZostajesz pokonany ' + emoji.emojize(':skull:', language='alias') + 
              '\n\nPrzegrywasz walke\n\nKONIEC GRY ' + emoji.emojize(':crying_face:', language='alias'))
        koniec = int(safe_input('\n1 - Zagraj od nowa\n2 - Wyjdz\n=>'))
        if koniec == 1:
            return 100, 2, 0, 0, 1, 0, 50, 100, 100, True
        else:
            exit()

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
    

menu = 1
while menu==1:
  print(('\n              '),end = ''),print('Arena'+emoji.emojize(':stadium:'),end = ''),print('              ')
  gra1 = safe_input('\n1 - Nowa gra'+emoji.emojize(':crossed_swords:', language='alias')+'\n2 - Wczytaj gre'+emoji.emojize(':scroll:', language='alias')+'\n3 - Informacje'+emoji.emojize(':blue_book:', language='alias')+'\n4 - Wyjscie'+emoji.emojize(':cross_mark:', language='alias')+'\n=>')
  if gra1 == 1:
    cls()
    akthp = 1000
    maxhp = 1000
    zloto = 5000
    poziom = 100
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
    cls()
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
    cls()
    info = int(safe_input('1 - O grze\n2 - Instrukcje\n3 - Wyjscie'+emoji.emojize(':cross_mark:', language='alias')+'\n=>'))
    if info==1:
      cls()
      print('Wykonal Hubert Jedruchniewicz\nCzas pracy: ~45 godzin')
      continue
    elif info==2:
      cls()
      print('Tawerna\n-Mozesz tam spac (potrzebna losowa ilosc zlota,losowa regeneracja zycia)\n-U handlarza kupujesz i sprzedajesz przedmioty (Miecz - im drozszy tym wiecej obrazen zadaje,Tarcza - mozliwosc zablokowania jednego ataku przeciwnika,')
      print('Ulepszenie zbroi - na stale dodaje 5 maksymalnego HP,Sprzedaz miecza - zyskujesz 20 szt. zlota niezaleznie od rodzaju miecza)')
      print('Namiot medyka\n-Opatrzenie ran (zwieksza ilosc aktualnego HP)\n-Zakupy u medyka (Mikstura - moze przywrocic HP w trakcie walki,Trucizna - po rzuceniu zadaje obrazenia w kazdej rundzie)')
      print('Sklep wiedzmy\n-Magiczne stwory pomagajace w walce (Ognik - na stale ulepsza twoje piesci lub miecz,Jaszczur - towarzyszy ci podczas walk,zadaje dodatkowe obrazenia w kazdej rundzie)')
      print('Przydatna rada - kazda runda obejmuje atak twojego bohatera i atak przeciwnika (wiec mimo ze np. oboje posiadacie malo HP, to po twoim ataku walke wygra przeciwnik)')
      print('Wniosek: aby wygrac walke musisz posiadac na tyle duzo HP, zeby po zakonczeniu rundy zostalo ci jeszcze przynajmniej 1 HP')
      continue
    elif info==3:
      cls()
      continue
    else:
      cls()
      print('Podano niewlasciwa liczbe')
      continue                                                              
  elif gra1 == 4:
    sys.exit()
  else:
    cls()
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
       if jaszczur==1:
         print('Posiadasz Jaszczura\U0001f996')
       if ((obrazeniaW-20)>0) and jaszczur==1:
         print('Ogniki: '+str(int((obrazeniaW-20)/2))+'\U0001f525')
       elif ((obrazeniaW)>0) and jaszczur==0:
         print('Ogniki: '+str(int((obrazeniaW)/2))+'\U0001f525')
       print('\nWybierz miejsce podrozy:')
       docelowe = int(safe_input('1 - Tawerna'+emoji.emojize(':houses:', language='alias')+'\n2 - Namiot medyka'+emoji.emojize(':camping:', language='alias')+'\n3 - Arena'+emoji.emojize(':stadium:', language='alias')+'\n4 - Rynek miasta'+emoji.emojize(':castle:', language='alias')+'\n5 - Zapisz gre'+emoji.emojize(':scroll:', language='alias')+'\n6 - Wyjscie z gry'+emoji.emojize(':cross_mark:', language='alias')+'\n=>'))
       if docelowe == 1:
        cls()
        print('\nTawerna'+emoji.emojize(':beer:', language='alias')+'\n\nWybierz aktywnosc:')
        tawerna = int(safe_input('1 - Przespij sie'+emoji.emojize(':last_quarter_moon_face:', language='alias')+'\n2 - Handlarz'+emoji.emojize(':person_in_tuxedo:', language='alias')+'\n3 - Wyjscie'+emoji.emojize(':cross_mark:', language='alias')+'\n=>'))
        if tawerna==1 and zloto>=12 and akthp!=maxhp:
          cls()
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
          cls()
          print('Masz maksymalna liczbe HP')
          continue
        elif tawerna == 1 and zloto<12:
          cls()
          print('Masz za malo pieniedzy')
          continue
        elif tawerna==2:
          cls()
          handlarz =int(safe_input('\nHandlarz'+emoji.emojize(':person_in_tuxedo:', language='alias')+'\n\nWybierz przedmiot:\n1 - Zelazny miecz - 25 szt. zlota\n2 - Srebrny miecz - 50 szt. zlota\n3 - Mistrzowski miecz - 100 szt. zlota\n4 - Ulepszenie zbroi - 10 szt. zlota\n5 - Tarcza - 10 szt. zlota\n\nSprzedaz:\n6 - Sprzedaj miecz\n\n7 - Wyjscie'+emoji.emojize(':cross_mark:', language='alias')+'\n=>'))
          if handlarz == 1 and ilosc_mieczy==0 and zloto>=25:
            cls()
            obrazeniaD = 2
            zloto-=25
            ilosc_mieczy += 1
            miecz = 1
            print('Zakupiono Zelazny miecz')
            continue
          elif handlarz == 2 and ilosc_mieczy==0 and zloto>=50:
            cls()
            obrazeniaD = 5
            zloto-=50
            ilosc_mieczy += 1
            miecz = 2
            print('Zakupiono Srebrny miecz')
            continue
          elif handlarz == 3 and ilosc_mieczy==0 and zloto>=100:
            cls()
            obrazeniaD = 11
            zloto-=100
            ilosc_mieczy += 1
            miecz = 3
            print('Zakupiono Mistrzowski miecz')
            continue
          elif handlarz == 4 and zloto>=10 and zbroja<10:
            cls()
            maxhp += 4
            akthp += 4
            zloto -= 10
            zbroja += 1
            print('Zakupiono Uleszenie zbroi')
            continue
          elif (handlarz == 1 or handlarz == 2 or handlarz == 3) and ilosc_mieczy==1:
            cls()
            print('Posiadasz juz miecz. Sprzedaj go, aby zakupic inny')
            continue
          elif handlarz ==  4 and zbroja == 10:
            cls()
            print('Posiadasz maksymalne ulepszenie zbroi')
            continue
          elif handlarz == 6 and ilosc_mieczy == 1:
            cls()
            print('Sprzedano aktualnie uzywany miecz')
            obrazeniaD = 0
            zloto += 20
            ilosc_mieczy -= 1
            miecz = 'brak'
            continue
          elif handlarz == 6 and ilosc_mieczy == 0:
            cls()
            print('Nie posiadasz miecza')
            continue
          elif handlarz == 5 and tarcza<1 and zloto >=10:
            cls()
            print('Zakupiono tarcze')
            zloto -= 10
            tarcza += 1
            continue
          elif handlarz == 5 and tarcza>=1:
            cls()
            print('Posiadasz juz tarcze')
            continue
          elif handlarz == 7:
            cls()
            continue
          else: print('Podano niewlasciwa liczbe lub masz za malo zlota')
          cls()
          continue
        elif tawerna == 3:
          cls()
          continue
        elif tawerna == 1 and zloto < 10:
          cls()
          print('Masz za malo zlota zeby przespac sie w tawernie')
        else: 
          cls()
          print('Podano niewlasciwa liczbe')
        continue
       elif docelowe == 2:
        cls()
        print('\nNamiot Medyka'+emoji.emojize(':camping:', language='alias')+'\n\nWybierz aktywnosc:')
        medyk = int(safe_input('1 - Opatrz rany'+emoji.emojize(':adhesive_bandage:', language='alias')+'\n2 - Kup mikstury'+emoji.emojize(':elf:', language='alias')+'\n3 - Wyjscie'+emoji.emojize(':cross_mark:', language='alias')+'\n=> '))
        if medyk == 1:
          cls()
          usluga =int(safe_input('\nOpatrz rany'+emoji.emojize(':adhesive_bandage:', language='alias')+'\n\nWybierz usluge:\n1 - Podstawowy opatrunek (+20 HP) - 5 szt. zlota\n2 - Zatrzymanie krwawienia (+45 HP) - 10 szt. zlota\n3 - Usztywnienie zlamania (+90 HP) - 20 szt. zlota\n4 - Wyjscie'+emoji.emojize(':cross_mark:', language='alias')+'\n=>' ))
          if usluga == 1 and akthp<=(maxhp-20) and zloto>=5:
            cls()
            akthp += 20
            zloto -= 5
            print('Zakupiono Podstawowy opatrunek')
            continue
          elif usluga == 2 and akthp<=(maxhp-45) and zloto>=10:
            cls()
            akthp += 45
            zloto -= 10
            print('Zakupiono usluge zatrzymania krwawienia')
            continue
          elif usluga == 3 and akthp<=(maxhp-92) and zloto>=20:
            cls()
            akthp += 92
            zloto -= 20
            print('Zakupiono usluge usztywnienia zlamania')
            continue
          elif usluga == 1 and akthp>(maxhp-20) and zloto>=5:
            cls()
            print("Nie jestes tak powaznie ranny")
            continue
          elif usluga == 2 and akthp>(maxhp-45) and zloto>=10:
            cls()
            print("Nie jestes tak powaznie ranny")
            continue
          elif usluga == 3 and akthp>(maxhp-92) and zloto>=20:
            cls()
            print("Nie jestes tak powaznie ranny")
            continue
          elif usluga == 4:
            cls()
            continue
          else: 
            cls()
            print('Podano niewlasciwa liczbe lub masz za malo zlota')
        elif medyk == 2:
          cls()
          sklepMedyk =int(safe_input('\nKup mikstury'+emoji.emojize(':elf:', language='alias')+'\n\nWybierz miksture:\n1 - Mikstura podstawowa (+15 HP) - 5 szt. zlota\nPodstawowe leczenie w trakcie walki. Ograniczona ilosc w ekwipunku : 2.\n2 - Trucizna - 7 szt. zlota\nPo uzyciu w trakcie walki zadaje przeciwnikowi obrazenia rowne: 3 co runde.\n3 - Wyjscie'+emoji.emojize(':cross_mark:', language='alias')+'\n=>) '))
          if sklepMedyk == 1 and mikstury<2:
            cls()
            mikstury += 1
            zloto -= 5
            print('Zakupiono miksture')
            continue
          elif sklepMedyk == 1 and mikstury>=2 and zloto>=5:
            cls()
            print('Posiadasz maksymalna liczbe mikstur')
            continue
          elif sklepMedyk == 2 and zloto>=7:
            cls()
            ilosc_trucizn += 1
            zloto -= 7
            print('Zakupiono trucizne')
            continue
          elif sklepMedyk == 3:
            cls()
            continue
          else: 
            cls()
            print('Podano niewlasciwa liczbe lub masz za malo zlota')
        elif  medyk == 3:
          cls()
          continue
        else: 
          cls()
          print('Podano niewlasciwa liczbe')
          continue
       elif docelowe == 3:
        cls()
        arena = int(safe_input('\nArena'+emoji.emojize(':stadium:', language='alias')+'\n\nWybierz arene:\n1 - Arena Treningowa'+emoji.emojize(':star:', language='alias')+'(Poziom 1-3)\n2 - Arena Poczatkujacych'+emoji.emojize(':star::star:', language='alias')+'(Poziom 4-9)\n3 - Arena Wojownikow'+emoji.emojize(':star::star::star:', language='alias')+'(Poziom 10-15)\n4 - Arena Mistrzowska'+emoji.emojize(':trophy:', language='alias')+'(Poziom 16-21)\n5 - Arena Krolewska'+emoji.emojize(':crown:', language='alias')+' (Poziom 22+)\n6 - Wyjscie'+emoji.emojize(':cross_mark:', language='alias')+'\n=>'))
        if arena == 1:
          cls()
          wrog1 = int(safe_input('\nArena Treningowa'+emoji.emojize(':star:', language='alias')+'\n\nWybierz przeciwinika:\n(Sortowane od najprostszego do najtrudniejszego)\n1 - Jednoreki bandyta'+emoji.emojize(':person_pouting:', language='alias')+'\n2 - Wilk'+emoji.emojize(':wolf:', language='alias')+'\n3 - Pijany kowal'+emoji.emojize(':old_man:', language='alias')+'\n4 - Wyjscie'+emoji.emojize(':cross_mark:', language='alias')+'\n=>'))
          cls()
          if wrog1 == 1:
              akthp, mikstury, ilosc_trucizn, tarcza, poziom, exp, zloto, maxexp, maxhp, kontynuuj = walka(
                  akthp, maxhp, mikstury, ilosc_trucizn, tarcza, obrazeniaD, obrazeniaW, poziom, exp, maxexp, zloto,
                  'Jednoreki bandyta', 40, 40, 5, 7, 25, 10, 0
              )
              continue
          elif wrog1 == 2:
              akthp, mikstury, ilosc_trucizn, tarcza, poziom, exp, zloto, maxexp, maxhp, kontynuuj = walka(
                  akthp, maxhp, mikstury, ilosc_trucizn, tarcza, obrazeniaD, obrazeniaW, poziom, exp, maxexp, zloto,
                  'Wilk', 60, 60, 8, 10, 40, 20, 0
              )
              continue
          elif wrog1 == 3:
              akthp, mikstury, ilosc_trucizn, tarcza, poziom, exp, zloto,maxexp, maxhp, kontynuuj = walka(
                  akthp, maxhp, mikstury, ilosc_trucizn, tarcza, obrazeniaD, obrazeniaW, poziom, exp, maxexp, zloto,
                  'Pijany kowal', 85, 85, 11, 12, 70, 35, 1, 'Zdobyles trofeum z areny! \U0001F949'
              )
              continue
          elif wrog1 == 4:
              continue
          else:
              print('Podano niewlasciowa liczbe')
              continue
        elif arena == 2 and poziom >= 4:
          cls()
          wrog1 = int(safe_input('\nArena Poczatkujacych'+emoji.emojize(':star::star:', language='alias')+'\n\nWybierz przeciwinika:\n(Sortowane od najprostszego do najtrudniejszego)\n1 - Zly Wiesniak'+emoji.emojize(':farmer:', language='alias')+'\n2 - Puma'+emoji.emojize(':leopard:', language='alias')+'\n3 - Rzeznik'+emoji.emojize(':man_cook:', language='alias')+'\n4 - Wyjscie'+emoji.emojize(':cross_mark:', language='alias')+'\n=>'))
          cls()
          if wrog1 == 1:
              akthp, mikstury, ilosc_trucizn, tarcza, poziom, exp, zloto,maxexp, maxhp, kontynuuj = walka(
                  akthp, maxhp, mikstury, ilosc_trucizn, tarcza, obrazeniaD, obrazeniaW, poziom, exp, maxexp, zloto,
                  'Zly Wiesniak', 100, 100, 13, 15, 92, 48, 0
              )
              continue
          elif wrog1 == 2:
              akthp, mikstury, ilosc_trucizn, tarcza, poziom, exp, zloto,maxexp, maxhp, kontynuuj = walka(
                  akthp, maxhp, mikstury, ilosc_trucizn, tarcza, obrazeniaD, obrazeniaW, poziom, exp, maxexp, zloto,
                  'Puma', 105, 105, 17, 18, 105, 56, 0
              )
              continue
          elif wrog1 == 3:
              akthp, mikstury, ilosc_trucizn, tarcza, poziom, exp, zloto,maxexp, maxhp, kontynuuj = walka(
                  akthp, maxhp, mikstury, ilosc_trucizn, tarcza, obrazeniaD, obrazeniaW, poziom, exp, maxexp, zloto,
                  'Rzeznik', 120, 120, 19, 21, 125, 65, 2, 'Zdobyles trofeum z areny! \U0001F948'
              )
              continue
          elif wrog1 == 4:
              continue
          else:
              print('Podano niewlasciowa liczbe')
              continue
        elif arena == 2 and poziom < 4:
            cls()
            print('Masz za niski poziom zeby walczyc na tej arenie')
            continue

        elif arena == 3 and poziom >= 10:
            cls()
            wrog1 = int(safe_input('\nArena Wojownikow'+emoji.emojize(':star::star::star:', language='alias')+'\n\nWybierz przeciwinika:\n(Sortowane od najprostszego do najtrudniejszego)\n1 - Gladiator'+emoji.emojize(':guard:', language='alias')+'\n2 - Niedzwiedz'+emoji.emojize(':bear:', language='alias')+'\n3 - Troll'+('\U0001f9cc')+'\n4 - Wyjscie'+emoji.emojize(':cross_mark:', language='alias')+'\n=>'))
            cls()
            if wrog1 == 1:
                akthp, mikstury, ilosc_trucizn, tarcza, poziom, exp, zloto,maxexp, maxhp, kontynuuj = walka(
                    akthp, maxhp, mikstury, ilosc_trucizn, tarcza, obrazeniaD, obrazeniaW, poziom, exp, maxexp, zloto,
                    'Gladiator', 130, 130, 22, 23, 140, 73, 0
                )
                continue
            elif wrog1 == 2:
                akthp, mikstury, ilosc_trucizn, tarcza, poziom, exp, zloto,maxexp, maxhp, kontynuuj = walka(
                    akthp, maxhp, mikstury, ilosc_trucizn, tarcza, obrazeniaD, obrazeniaW, poziom, exp, maxexp, zloto,
                    'Niedzwiedz', 145, 145, 25, 27, 150, 80, 0
                )
                continue
            elif wrog1 == 3:
                akthp, mikstury, ilosc_trucizn, tarcza, poziom, exp, zloto,maxexp, maxhp, kontynuuj = walka(
                    akthp, maxhp, mikstury, ilosc_trucizn, tarcza, obrazeniaD, obrazeniaW, poziom, exp, maxexp, zloto,
                    'Troll', 155, 155, 28, 30, 165, 88, 3, 'Zdobyles trofeum z areny! \U0001F3C5'
                )
                continue
            elif wrog1 == 4:
                continue
            else:
                print('Podano niewlasciowa liczbe')
                continue
        elif arena == 3 and poziom < 10:
            cls()
            print('Masz za niski poziom zeby walczyc na tej arenie')
            continue

        elif arena == 4 and poziom >= 16:
            cls()
            wrog1 = int(safe_input('\nArena Mistrzowska'+emoji.emojize(':trophy:', language='alias')+'\n\nWybierz przeciwinika:\n(Sortowane od najprostszego do najtrudniejszego)\n1 - Ninja'+emoji.emojize(':ninja:', language='alias')+'\n2 - Slon'+emoji.emojize(':elephant:', language='alias')+'\n3 - Demon'+emoji.emojize(':ogre:',language='alias')+'\n4 - Wyjscie'+emoji.emojize(':cross_mark:', language='alias')+'\n=>'))
            cls()
            if wrog1 == 1:
                akthp, mikstury, ilosc_trucizn, tarcza, poziom, exp, zloto,maxexp, maxhp, kontynuuj = walka(
                    akthp, maxhp, mikstury, ilosc_trucizn, tarcza, obrazeniaD, obrazeniaW, poziom, exp, maxexp, zloto,
                    'Ninja', 165, 165, 32, 33, 175, 95, 0
                )
                continue
            elif wrog1 == 2:
                akthp, mikstury, ilosc_trucizn, tarcza, poziom, exp, zloto,maxexp, maxhp, kontynuuj = walka(
                    akthp, maxhp, mikstury, ilosc_trucizn, tarcza, obrazeniaD, obrazeniaW, poziom, exp, maxexp, zloto,
                    'Slon', 175, 175, 34, 36, 180, 100, 0
                )
                continue
            elif wrog1 == 3:
                akthp, mikstury, ilosc_trucizn, tarcza, poziom, exp, zloto,maxexp, maxhp, kontynuuj = walka(
                    akthp, maxhp, mikstury, ilosc_trucizn, tarcza, obrazeniaD, obrazeniaW, poziom, exp, maxexp, zloto,
                    'Demon', 190, 190, 37, 39, 192, 108, 4, 'Zdobyles trofeum z areny! \U0001F3C6'
                )
                continue
            elif wrog1 == 4:
                continue
            else:
                print('Podano niewlasciowa liczbe')
                continue
        elif arena == 4 and poziom < 16:
            cls()
            print('Masz za niski poziom zeby walczyc na tej arenie')
            continue

        elif arena == 5 and poziom >= 22:
            cls()
            wrog1 = int(safe_input('\nArena Krolewska'+emoji.emojize(':crown:', language='alias')+'\n\nWybierz przeciwinika:\n(Sortowane od najprostszego do najtrudniejszego)\n1 - Czarodziej'+emoji.emojize(':mage:', language='alias')+'\n2 - Smok'+emoji.emojize(':dragon:', language='alias')+'\n3 - Krolewski Pretendent'+emoji.emojize(':supervillain:',language='alias')+'\n4 - Wyjscie'+emoji.emojize(':cross_mark:', language='alias')+'\n=>'))
            cls()
            if wrog1 == 1:
                akthp, mikstury, ilosc_trucizn, tarcza, poziom, exp, zloto,maxexp, maxhp, kontynuuj = walka(
                    akthp, maxhp, mikstury, ilosc_trucizn, tarcza, obrazeniaD, obrazeniaW, poziom, exp, maxexp, zloto,
                    'Czarodziej', 200, 200, 40, 42, 205, 120, 0
                )
                continue
            elif wrog1 == 2:
                akthp, mikstury, ilosc_trucizn, tarcza, poziom, exp, zloto,maxexp, maxhp, kontynuuj = walka(
                    akthp, maxhp, mikstury, ilosc_trucizn, tarcza, obrazeniaD, obrazeniaW, poziom, exp, maxexp, zloto,
                    'Smok', 225, 225, 44, 47, 220, 132, 0
                )
                continue
            elif wrog1 == 3:
                akthp, mikstury, ilosc_trucizn, tarcza, poziom, exp, zloto,maxexp, maxhp, kontynuuj = walka(
                    akthp, maxhp, mikstury, ilosc_trucizn, tarcza, obrazeniaD, obrazeniaW, poziom, exp, maxexp, zloto,
                    'Krolewski Pretendent', 255, 255, 49, 52, 240, 150, 5, 'Zostajesz Nowym Pretendentem Areny!'+emoji.emojize(':crown:', language='alias')
                )
                continue
            elif wrog1 == 4:
                continue
            else:
                print('Podano niewlasciowa liczbe')
                continue
        elif arena == 5 and poziom < 22:
            cls()
            print('Masz za niski poziom zeby walczyc na tej arenie')
            continue

        elif arena == 6:
            cls()
            continue

        else:
            cls()
            print('Podano niewlasciowa liczbe')
            continue
       elif docelowe == 4:
         if poziom >=5:
           cls()
           print('\nRynek miasta'+emoji.emojize(':fountain:', language='alias')+'\n\nWybierz aktywnosc:')
           miasto = int(safe_input('1 - Mieszkanie'+emoji.emojize(':house:', language='alias')+'\n2 - Sklep wiedzmy'+emoji.emojize(':japanese_castle:', language='alias')+'\n3 - Wyjscie'+emoji.emojize(':cross_mark:', language='alias')+'\n=>'))
           if miasto == 1 and mieszkanie != 1:
             cls()
             print('\nMieszkanie'+emoji.emojize(':house:', language='alias')+'\n')
             kupM = int(safe_input('1 - Kup mieszkanie - 500 szt. zlota\n(mozliwosc regeneracji HP za darmo, a takze tansze wytwarzanie mikstur)\n2 - Wyjscie'+emoji.emojize(':cross_mark:', language='alias')+'\n=>'))
             if kupM == 1 and zloto >=500:
               cls()
               print('Zakupiles mieszkanie!')
               zloto -= 500
               mieszkanie = 1
               continue
             elif kupM == 1 and zloto<500:
               cls()
               print('Masz za malo zlota')
               continue
             elif kupM == 2:
               cls()
               continue
             else: 
               cls()
               print('Podano niewlasciwa liczbe')
             continue
           elif miasto == 1 and mieszkanie == 1:
             cls()
             print('\nMieszkanie'+emoji.emojize(':house:', language='alias')+'\n')
             mA = int(safe_input('1 - Idz spac\n2 - Wytworz domowe mikstury - 1 szt. zlota\n3 - Spojrz na trofea\n4 - Wyjscie'+emoji.emojize(':cross_mark:', language='alias')+'\n=>'))
             if mA == 1 and akthp!=maxhp:
               cls()
               akthp += random.randint(5,90)
               print('\n'+emoji.emojize(':bed:', language='alias'),end =''),time.sleep(0.6),print(('\U0001f4a4'),end = ''),time.sleep(0.6),print(('\U0001f4a4'),end = ''),time.sleep(0.6),print(('\U0001f4a4'),end = ''),time.sleep(0.6),print('\U0001f4a4'),time.sleep(0.6)
               if akthp>maxhp:
                 akthp = akthp-(akthp-maxhp)
                 continue
               else:
                 continue
             elif mA == 1 and akthp==maxhp:
               cls()
               print('Masz maksymalna liczbe HP')
             elif mA == 2 and zloto >= 1 and mikstury < 2:
               mikstury += 1
               zloto -= 1
               cls()
               print('Wytworzono miksture')
               continue
             elif mA == 2 and zloto <= 1:
               cls()
               print('Masz za malo zlota')
               continue
             elif mA == 2 and mikstury >= 2:
               cls()
               print('Masz maksymalna liczbe mikstur')
               continue
             elif mA == 3:
               cls()
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
                 cls()
                 print('Nie posiadasz jeszcze zadnych trofeow')
                 continue
               elif trofeum1 == 0 or trofeum2 == 0 or trofeum3 == 0 or trofeum4 == 0 or trofeum5 == 0:
                 trof = int(safe_input('\n1 - Wyjscie'+emoji.emojize(':cross_mark:', language='alias')+'\n=>'))
                 if trof == 1:
                   continue
                 else: continue
               else: continue  
             elif mA == 4:
               cls()
               continue
             else:
               cls()
               print('Podano niewlasciwa liczbe')
               continue
           elif miasto == 2:
             cls()
             wiedzma = int(safe_input('\nSklep wiedzmy'+emoji.emojize(':japanese_castle:', language='alias')+'\n\n1 - Magiczny miecz - 199 szt. zlota\n2 - Starozytny miecz - 320 szt. zlota\n3 - Boski miecz - 480 szt. zlota\n4 - Ognik - 30 szt. zlota\nOgnik zwieksza obrazenia miecza (lub piesci) nakladajac na przeciwnika efekt podpalenia.\nOgniki zadaja obrazenia w kazdej rundzie.\nMozna kupowac wielokrotnie.\n5 - Jaszczur - 260 szt. zlota\nTowarzyszy Ci podczas walki.\nZadaje dodatkowe obrazenia w kazdej rundzie.\nMozna kupic tylko raz\n6 - Wyjscie'+emoji.emojize(':cross_mark:', language='alias')+'\n=>'))
             if wiedzma==1 and ilosc_mieczy==0 and zloto>=199:
               obrazeniaD = 23
               zloto-=199
               ilosc_mieczy += 1
               miecz = 4
               cls()
               print('Zakupiono Magiczny miecz')
               continue
             elif wiedzma == 2 and ilosc_mieczy==0 and zloto>=320:
               obrazeniaD = 36
               zloto-=320
               ilosc_mieczy += 1
               miecz = 5
               cls()
               print('Zakupiono Starozytny miecz')
               continue
             elif wiedzma == 3 and ilosc_mieczy==0 and zloto>=480:
               obrazeniaD = 50
               zloto-=480
               ilosc_mieczy += 1
               miecz = 6
               cls()
               print('Zakupiono Boski miecz')
               continue
             elif wiedzma == 4 and zloto>=30:
               obrazeniaW += 2
               zloto -= 30
               cls()
               print('Zakupiono Ognika')
               continue
             elif (wiedzma == 1 or wiedzma == 2 or wiedzma == 3) and ilosc_mieczy==1:
               cls()
               print('Posiadasz juz miecz. Sprzedaj go, aby zakupic inny')
               continue
             elif wiedzma == 5 and zloto>=260 and jaszczur == 0:
               obrazeniaW += 20
               zloto -= 260
               jaszczur = 1
               cls()
               print('Zakupiono Jaszczura')
               continue
             elif wiedzma == 5 and jaszczur == 1:
               cls()
               print('Posiadasz juz Jaszczura')
               continue
             elif wiedzma == 6:
               cls()
               continue
             else:
               cls()
               print('Podano niewlasciwa liczbe lub masz za malo zlota')
               continue
           elif miasto==3:
             cls()
             continue
           else:
             cls()
             print('Podano niewlasciwa liczbe')
             continue
         else: 
           cls()
           print('Masz za niski poziom (Wymagany poziom: 5)')
           continue
       elif docelowe==5:
           cls()
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
         cls()
         exit1 = int(safe_input('Czy na pewno chcesz wyjsc?\nUtracisz wszystkie niezapisane postepy.\n1 - Tak\n2 - Nie\n=>'))
         if exit1 == 1:
           sys.exit()
         else:
           cls()
           continue      
       else:
         cls()
         print('Podano niewlasciowa liczbe')
         continue
       break
