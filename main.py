def find_mask(dictionary_mask, string_to_cover):
    mask_to_find = ""
    index_hexadecimal = []
    is_hexa_in_string = False

    # Je recherche les hexadécimales dans la chaine à couvrir
    for hexadecimal in dictionary_mask['b']:
        if hexadecimal in string_to_cover:
            is_hexa_in_string = True
            # J'enregistre la postion de l'hexadécimal pour le remplacer par la bonne lettre plus tard
            index_hexadecimal.append(string_to_cover.index(hexadecimal))
            # J'enlève les caractères en trop car un hexadécimal est composé de 4 caractères
            string_to_cover = string_to_cover[:string_to_cover.index(hexadecimal) + 1] + '' + \
                string_to_cover[string_to_cover.index(hexadecimal) + 4:]

    # Pour ne pas dépasser 81 442 800 000 000 mots la longueur maximal d'un
    # masque avec seulement des "a" est de 7 caractères (95^7)
    # Afin d'avoir un plus grand taux de recouvrement le masque ne pourra pas avoir plus de 6 "a"
    # Je compare donc avec 7 car 6 + \n
    if len(string_to_cover) <= 7:
        # Je soustrait par 1 afin de ne pas prendre en compte le \n à la fin de la chaine
        for i in range(len(string_to_cover) - 1):
            mask_to_find += string_to_cover.replace(string_to_cover, "a")
    else:
        for caractere in string_to_cover:
            lettre_masque_trouve = False
            for key in dictionary_mask:
                # J'empèche le programme de parcourir toutes les valeurs des clés si
                # j'ai déja trouvé ma lettre pour mon masque
                if not lettre_masque_trouve:
                    for c in dictionary_mask[key]:
                        if c == caractere:
                            mask_to_find += key
                            lettre_masque_trouve = True
    # Je remplace la lettre à la postion de ma chaine hexadécimal par un b
    if is_hexa_in_string:
        for index in index_hexadecimal:
            mask_to_find = mask_to_find[:index] + 'b' + mask_to_find[index + 1:]

    return mask_to_find


def calculate_generated_space(mask_find):

    generated_space_dictionary = {
        'l': 26,
        'u': 26,
        'd': 10,
        'h': 16,
        'H': 16,
        's': 33,
        'a': 95,
        'b': 255
    }

    # Je multiplie chaque taille des espaces générés afin de trouver la taille d'un masque
    mask_generate_space = 1
    for letter in mask_find:
        for letter_for_mask in generated_space_dictionary:
            if letter == letter_for_mask:
                mask_generate_space *= generated_space_dictionary[letter_for_mask]

    return mask_generate_space


dictionary_letter_for_mask = {
    'd': '0123456789',
    'h': '0123456789abcdef',
    'H': '0123456789ABCDEF',
    'l': 'abcdefghijklmnopqrstuvwxyz',
    'u': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
    's': r'! "#$%&\'()*+,-./:;<=>?@[\]^_`{|}~',
    'a': 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!'
         r' "#$%&\'()*+,-./:;<=>?@[\]^_`{|}~',
    'b': ['0x00', '0x01', '0x02', '0x03', '0x04', '0x05', '0x06', '0x07',
          '0x08', '0x09', '0x0a', '0x0b', '0x0c', '0x0d', '0x0e', '0x0f',
          '0x10', '0x11', '0x12', '0x13', '0x14', '0x15', '0x16', '0x17',
          '0x18', '0x19', '0x1a', '0x1b', '0x1c', '0x1d', '0x1e', '0x1f',
          '0x20', '0x21', '0x22', '0x23', '0x24', '0x25', '0x26', '0x27',
          '0x28', '0x29', '0x2a', '0x2b', '0x2c', '0x2d', '0x2e', '0x2f',
          '0x30', '0x31', '0x32', '0x33', '0x34', '0x35', '0x36', '0x37',
          '0x38', '0x39', '0x3a', '0x3b', '0x3c', '0x3d', '0x3e', '0x3f',
          '0x40', '0x41', '0x42', '0x43', '0x44', '0x45', '0x46', '0x47',
          '0x48', '0x49', '0x4a', '0x4b', '0x4c', '0x4d', '0x4e', '0x4f',
          '0x50', '0x51', '0x52', '0x53', '0x54', '0x55', '0x56', '0x57',
          '0x58', '0x59', '0x5a', '0x5b', '0x5c', '0x5d', '0x5e', '0x5f',
          '0x60', '0x61', '0x62', '0x63', '0x64', '0x65', '0x66', '0x67',
          '0x68', '0x69', '0x6a', '0x6b', '0x6c', '0x6d', '0x6e', '0x6f',
          '0x70', '0x71', '0x72', '0x73', '0x74', '0x75', '0x76', '0x77',
          '0x78', '0x79', '0x7a', '0x7b', '0x7c', '0x7d', '0x7e', '0x7f',
          '0x80', '0x81', '0x82', '0x83', '0x84', '0x85', '0x86', '0x87',
          '0x88', '0x89', '0x8a', '0x8b', '0x8c', '0x8d', '0x8e', '0x8f',
          '0x90', '0x91', '0x92', '0x93', '0x94', '0x95', '0x96', '0x97',
          '0x98', '0x99', '0x9a', '0x9b', '0x9c', '0x9d', '0x9e', '0x9f',
          '0xa0', '0xa1', '0xa2', '0xa3', '0xa4', '0xa5', '0xa6', '0xa7',
          '0xa8', '0xa9', '0xaa', '0xab', '0xac', '0xad', '0xae', '0xaf',
          '0xb0', '0xb1', '0xb2', '0xb3', '0xb4', '0xb5', '0xb6', '0xb7',
          '0xb8', '0xb9', '0xba', '0xbb', '0xbc', '0xbd', '0xbe', '0xbf',
          '0xc0', '0xc1', '0xc2', '0xc3', '0xc4', '0xc5', '0xc6', '0xc7',
          '0xc8', '0xc9', '0xca', '0xcb', '0xcc', '0xcd', '0xce', '0xcf',
          '0xd0', '0xd1', '0xd2', '0xd3', '0xd4', '0xd5', '0xd6', '0xd7',
          '0xd8', '0xd9', '0xda', '0xdb', '0xdc', '0xdd', '0xde', '0xdf',
          '0xe0', '0xe1', '0xe2', '0xe3', '0xe4', '0xe5', '0xe6', '0xe7',
          '0xe8', '0xe9', '0xea', '0xeb', '0xec', '0xed', '0xee', '0xef',
          '0xf0', '0xf1', '0xf2', '0xf3', '0xf4', '0xf5', '0xf6', '0xf7',
          '0xf8', '0xf9', '0xfa', '0xfb', '0xfc', '0xfd', '0xfe', '0xff']
}

file_path = input("Saisir le chemin du fichier : ")

list_of_combination = []

try:
    file = open(file_path)
    list_of_combination = file.readlines()
    file.close()
except FileNotFoundError:
    print('Fichier introuvable.')
except IOError:
    print('Erreur d\'entrée/sortie.')

list_of_mask = []
recovery_rate_dictionary = {}  # Ce dictionnaire me permettra d'enregistrer le nombre de fois ou un masque est utilisé
sum_of_generated_spaces = 0
number_of_string_covered = 0

for combination in list_of_combination:
    # Je vérifie que mon masque ne dépasse pas la limite de mot
    # Je l'ajoute dans mon dictionnaire s'il n'existe pas deja
    # Sinon j'ajoute 1 au masque déjà existant
    mask = find_mask(dictionary_letter_for_mask, combination)
    if calculate_generated_space(mask) <= 81442800000000:
        if mask not in recovery_rate_dictionary:
            recovery_rate_dictionary[mask] = 1
        else:
            recovery_rate_dictionary[mask] += 1

for key_mask, value_mask in sorted(recovery_rate_dictionary.items(), key=lambda x: x[1], reverse=True):
    sum_of_generated_spaces += calculate_generated_space(key_mask)
    # J'ajoute mon masque à la liste tant que la somme des tailles des espaces générés par les masques ne dépasse pas
    # 81 442 800 000 000 mots
    if sum_of_generated_spaces <= 81442800000000:
        list_of_mask.append(key_mask)
        number_of_string_covered += value_mask
    else:
        sum_of_generated_spaces -= calculate_generated_space(key_mask)

print("Liste des masques : \n")
print(*list_of_mask, sep="\n")
print("\nle nombre de masque généré est de: %s\n" % (len(list_of_mask)))
print("Le nombre de chaine recouverte est de : %s\n" % number_of_string_covered)
print("Le taux de recouvrement est de : %.2f\n" % (100 * number_of_string_covered / len(list_of_combination)))
print("La somme des tailles des espaces générés par les masques est de : {:,d}".format(sum_of_generated_spaces)
      .replace(',', ' ').replace('.', ','))
