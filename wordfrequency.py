from pathlib import Path
import sys
import string


# Dette er start-koden til den første programmeringsoppgave i ING 301
#
# Du skal utvikle et programm som finner det hyppigste ordet i en gitt tekstfil.
# Dette høres kanskje litt komplisiert ut, men fortvil ikke!
# Vi har forberedt den grove strukturen allerede. Din oppgave er å implementere
# noen enkelte funskjoner som trengs for det hele til å virke.
# Enhver funksjon kommer med en dokumentasjon som forklarer hva skal gjøres.


def read_file(file_name):
    """
    Denne funksjonen får et filnavn som argument og skal gi
    tilbake en liste av tekststrenger som representerer linjene i filen.
    """
    # Tips: kanksje "open"-funksjonen kunne være nyttig her: https://docs.python.org/3/library/functions.html#open
    #return NotImplemented  # TODO: Du må erstatte denne linjen

    with open(file_name,"r",encoding='utf-8') as file: # måtte endre til with open fordi det lukker filen på bedre måte og håndterer bokstaver som å
        result = [linje.strip() for linje in file]
    return result

    # Gammel testkode 
    # file = open(file_name) # åpne filen
    # result = [] 
    # innhold = file.read() # lese hele filinnholdet
    # linjer = innhold.split("\n") # del innholdet i linjer
    # for linje in linjer: # legger hver linje i en liste
    #     result.append(linje)
    # file.close()
    # return result # returnerer resultatet
    


def lines_to_words(lines):
    """
    Denne funksjonen får en liste med strenger som input (dvs. linjene av tekstfilen som har nettopp blitt lest inn)
    og deler linjene opp i enkelte ord. 
    Enhver linje blir delt opp der det er blanktegn (= whitespaces).
    Desto videre er vi bare interessert i faktiske ord, dvs. alle punktum (.), kolon (:), semikolon (;),
    kommaer (,), spørsmåls- (?) og utråbstegn (!) skal fjernes underveis.
    Til sist skal alle ord i den resulterende listen være skrevet i små bokstav slik at "Odin" og "odin"
    blir behandlet likt.
    OBS! Pass også på at du ikke legger til tomme ord (dvs. "" eller '' skal ikke være med) i resultatlisten!

    F. eks: Inn: ["Det er", "bare", "noen få ord"], Ut: ["Det", "er", "bare", "noen", "få", "ord"]
    """
    # Tips: se på "split()"-funksjonen https://docs.python.org/3/library/stdtypes.html#str.split
    # i tillegg kan "strip()": https://docs.python.org/3/library/stdtypes.html#str.strip
    # og "lower()": https://docs.python.org/3/library/stdtypes.html#str.lower være nyttig
    # return NotImplemented  # TODO: Du må erstatte denne linjen

    remove_chars = str.maketrans('', "", string.punctuation) #  genererer tabell som fjerner nødvendig tegnsetting

    words = []
    for line in lines: # itererer gjennom hver linje
        # Deler linjen i ord og fjærner spesifikke tegn
        for word in line.split(): # deler linjen i ord
            word = word.translate(remove_chars).lower() # fjerner tegnsetting og små bokstaver
            if word: # skjekker om et ord er tomt
                words.append(word)
    return words # returnerer ord
    

def compute_frequency(words):
    """
    Denne funksjonen tar inn en liste med ord og så lager den en frekvenstabell ut av den. En frekvenstabell
    teller hvor ofte hvert ord dykket opp i den opprinnelige input listen. Frekvenstabllen
    blir realisert gjennom Python dictionaires: https://docs.python.org/3/library/stdtypes.html#mapping-types-dict

    F. eks. Inn ["hun", "hen", "han", "hen"], Ut: {"hen": 2, "hun": 1, "han": 1}
    """
    # return NotImplemented  # TODO: Du må erstatte denne linjen

    freq_table = {}

    for word in words:
        if word in freq_table:
             freq_table[word] += 1
        else:
            freq_table[word] = 1
    return freq_table


FILL_WORDS = ['og', 'dei', 'i', 'eg', 'som', 'det', 'han', 'til', 'skal', 'på', 'for', 'då', 'ikkje', 'var', 'vera']


def remove_filler_words(frequency_table):
    """
    Ofte inneholder tekst koblingsord som "og", "eller", "jeg", "da". Disse er ikke så spennende når man vil
    analysere innholdet til en tekst. Derfor vil vi gjerne fjerne dem fra vår frekvenstabell.
    Vi har gitt deg en liste med slike koblingsord i variablen FILL_WORDS ovenfor.
    Målet med denne funksjonen er at den skal få en frekvenstabll som input og så fjerne alle fyll-ord
    som finnes i FILL_WORDS.
    """
    # return NotImplemented  # TODO: Du må erstatte denne linjen
    
    if not frequency_table: # skjekker at det er innhold
        return None
    
    resultat = {word: freq for word, freq in frequency_table.items() if word not in FILL_WORDS}
    print(resultat) 
    return resultat
    
def largest_pair(par_1, par_2):
    """
    Denne funksjonen får som input to tupler/par (https://docs.python.org/3/library/stdtypes.html#tuple) der den
    første komponenten er en string (et ord) og den andre komponenten er en integer (heltall).
    Denne funksjonen skal sammenligne heltalls-komponenten i begge par og så gi tilbake det paret der
    tallet er størst.
    """
    # OBS: Tenk også på situasjonen når to tall er lik! Vurder hvordan du vil handtere denne situasjonen
    # kanskje du vil skrive noen flere test metoder ?!
    # return NotImplemented  # TODO: Du må erstatte denne linjen

    if (par_1[1]) > (par_2[1]):
        return par_1
    elif(par_1[1] < par_2[1]):
        return par_2
    else:
        return [par_1, par_2] # returnerer begge to som en liste


def find_most_frequent(frequency_table):
    """
    Nå er det på tide å sette sammen alle bitene du har laget.
    Den funksjonen får frekvenstabllen som innputt og finner det ordet som dykket opp flest.
    """
    # Tips: se på "dict.items()" funksjonen (https://docs.python.org/3/library/stdtypes.html#dict.items)
    # og kanskje du kan gjenbruke den "largest_pair" metoden som du nettopp har laget
    # return NotImplemented  # TODO: Du må erstatte denne linjen

    if not frequency_table: # skjekker om det er innhold i tabellen
        return None
    

    # Finner ordet som forekommer flest ganger
    Mest_vanlig_ord = ""
    mest_Vanlig_ant = 0

    for word, frequency in frequency_table.items(): # bruker komma for å pakke ut tupler
        if frequency > mest_Vanlig_ant:
            Mest_vanlig_ord  = word
            mest_Vanlig_ant = frequency

    return Mest_vanlig_ord
    


############################################################
#                                                          #
# Her slutter dendelen av filen som er relevant for deg ;-)#
#                                                          #
############################################################


def main():
    if len(sys.argv) > 1 and Path(sys.argv[1]).exists():
        file = sys.argv[1]
    else:
        file = str(Path(__file__).parent.absolute()) + "/voluspaa.txt"
    lines = read_file(file)
    words = lines_to_words(lines)
    table = compute_frequency(words)
    table = remove_filler_words(table)
    most_frequent = find_most_frequent(table)
    print(f"The most frequent word in {file} is '{most_frequent}'")


if __name__ == '__main__':
    main()
