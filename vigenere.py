#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @@ par NERET Sébastien & CARVALHO Olivier @@

#AU CAS OU ALPHABET MODIFIE:
#alphabet = ['b','a','d','c','f','d','h','g','j','i','l','k','n','m','p','o','r','q','t','s','v','u','x','v','z','y','\'','9','7','3','5','4','6','2','8','1','@','+',',','.','?',';',':','*','/','%',"#",'&','!','A','B','C','D','E','F','G','H','I','K','L','M','N','O','P','R','S','T','U','V','X','X','Y','Z']

alphabet = ['b','a','d','c','f','d','h','g','j','i','l','k','n','m','p','o','r','q','t','s','v','u','x','v','z','y','\'','9','7','3','5','4','6','2','8','1','@','+',',','.','?',';',':','*','/','%',"#",'&','!','A','B','C','D','E','F','G','H','I','K','L','M','N','O','P','R','S','T','U','V','X','X','Y','Z']

# ------------------------------------------------ FONCTION DE CRYPTAGE -------------------------------------- #
def crypte ( mess , cle ): #CHIFFREMENT POLYALPHABETIQUE PAR SUBSTITUTION (CRYPTAGE DE VIGENERE)
	t_mess = len(mess)-1
	t_cle = len(cle)-1
	mess_crpt = " "
	mess_code = []
	cle_code = []

	for i in range(0,t_mess+1):
		mess_code.insert(i, ret_nb(mess[i]))
	for i in range(0,t_cle+1):
		cle_code.insert(i, ret_nb(cle[i]))

	if t_mess <= t_cle:
		for i in range(0,t_mess+1):
			if mess_code[i] != 99:
				mess_code[i] += cle_code[i]
				if mess_code[i] >= len(alphabet):
					mess_code[i] -= len(alphabet)
	else:
		rang = -1
		rtn_beg = False

		for i in range(0,t_mess+1):
			rtn_beg = False
			if mess_code[i] != 99:
				rang += 1
				if rang == t_cle:
					rtn_beg = True
				mess_code[i] += cle_code[rang]
				if mess_code[i] >= len(alphabet):
					mess_code[i] -= len(alphabet)
				if rtn_beg == True:
					rang = -1
	for i in range(0,t_mess+1):
		mess_crpt += ret_ltr(mess_code[i])

	return mess_crpt
# ------------------------------------------------------------------------------------------------------------ #


# ------------------------------------------------- FONCTION DE DECRYPTAGE ----------------------------------- #	
def decrypte ( mess , cle ): #DECHIFFREMENT POLYALPHABETIQUE PAR SUBSTITUTION (CRYPTAGE DE VIGENERE)
	t_mess = len(mess)-1
	t_cle = len(cle)-1
	mess_crpt = " "
	mess_code = []
	cle_code = []

	for i in range(0,t_mess+1):
		mess_code.insert(i, ret_nb(mess[i]))
	for i in range(0,t_cle+1):
		cle_code.insert(i, ret_nb(cle[i]))

	if t_mess <= t_cle:
		for i in range(0,t_mess+1):
			if mess_code[i] != 99:
				mess_code[i] -= cle_code[i]
				if mess_code[i] < 0:
					mess_code[i] += len(alphabet)
	else:
		rang = -1
		rtn_beg = False

		for i in range(0,t_mess+1):
			rtn_beg = False
			if mess_code[i] != 99:
				rang += 1
				if rang == t_cle:
					rtn_beg = True
				mess_code[i] -= cle_code[rang]
				if mess_code[i] < 0:
					mess_code[i] += len(alphabet)
				if rtn_beg == True:
					rang = -1
	for i in range(0,t_mess+1):
		mess_crpt += ret_ltr(mess_code[i])

	return mess_crpt	
# ------------------------------------------------------------------------------------------------------------ #


def ret_nb(lettre): #RECOIS UNE LETTRE -> RENVOIE SON RANG
	ltr_find = False
	for ltr in range(0,len(alphabet)):
		if lettre == alphabet[ltr]:
			ltr_find = True
			rang = ltr
			
	if ltr_find == False:
		return 99
	else:
		return rang
		

def ret_ltr(nb): #RECOIS UN NOMBRE -> RENVOIE LA LETTRE
	if nb >= 0 and nb <= len(alphabet):
		return alphabet[nb]
	else:
		return ' '
		

if __name__ == "__main__" : #MAIN
	print "** program by NERET sebastien & CARVALHO olivier **"
	print "\n\n"
	lang = raw_input("LANGUAGE (fr / en) : ")
	if lang == "fr":
		msg_menu = " CRYTAGE / DECRYPTAGE VIGENERE  "
		msg_inp_mess_cl = "SAISIR MESSAGE CLAIR :"
		msg_inp_cle = "SAISIR LA CLE DE CRYPTAGE :"
		msg_inp_mess_crpt = "SAISIR LE MESSAGE CRYPTE :"
		msg_inp_cle_dec = "SAISIR LA CLE DE DECRYPTAGE :"
		msg_fin_crpt = "MESSAGE CRYPTE :"
		msg_fin_decrpt = "MESSAGE DECRYPTE :"
		msg_ch_1 = "   [c] - CRYPTER UN MESSAGE     "
		msg_ch_2 = "   [d] - DECRYPTER UN MESSAGE   "
		msg_ch_3 = "   [q] - QUITTER                "
		msg_err = "CHOIX INCORRECT : "
		msg_exit  = "MERCI D'AVOIR UTILISE NOTRE PROGRAMME, A BIENTOT !"
		inv = "CHOIX : "
	else:
		msg_menu = "ENCRYPTION / DECRYPTION VIGENERE"
		msg_inp_mess_cl = "INPUT CLEAR MESSAGE :"
		msg_inp_cle = "INPUT THE ENCRYPTION KEY :"
		msg_inp_mess_crpt = "INPUT THE ENCRYPTED MESSAGE :"
		msg_inp_cle_dec = "INPUT THE DECRYPTION KEY :"
		msg_fin_crpt = "ENCRYPTED MESSAGE :"
		msg_fin_decrpt = "DECRYPTED MESSAGE :"
		msg_ch_1 = "   [c] - ENCRYPT A MESSAGE      "
		msg_ch_2 = "   [d] - DECRYPT A MESSAGE      "
		msg_ch_3 = "   [q] - EXIT                   "
		inv = "CHOICE : "
		msg_exit = "THANKS TO USE OUT PROGRAM, SEE YOU SOON !"
		msg_err = "INCORRECT CHOICE : "
	
	print "\n\n\t------------------------------------"
	print "\t|" , msg_menu , "|"
	print "\t------------------------------------"
	print "\t|" , msg_ch_1 , "|"
	print "\t|" , msg_ch_2 , "|"
	print "\t|" , msg_ch_3 , "|"
	print "\t------------------------------------\n"
	
	choix = 'z'
	while choix != "c" and choix != "d" and choix != "q":
		choix = raw_input(inv)
		choix = choix.lower()
		if choix != "c" and choix != "d" and choix != "q":
			print msg_err,"'",choix,"'"
	
	if choix == 'c':
		print "\n\n"
		mess = raw_input(msg_inp_mess_cl)
		cle = raw_input(msg_inp_cle)
		mess_fin = crypte(mess,cle)
		print "\n" , msg_fin_crpt , "[" , mess_fin , "]"
	
	elif choix == 'd':
		print "\n\n"
		mess = raw_input(msg_inp_mess_crpt)
		cle = raw_input(msg_inp_cle_dec)
		mess_fin = decrypte(mess,cle)
		print "\n", msg_fin_decrpt , "[" , mess_fin , "]"
	
	else:
		print "\n\n" , msg_exit


