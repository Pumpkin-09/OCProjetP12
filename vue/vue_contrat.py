from vue.vue import verification_input, clear_terminal, demander_modification, vue_affichage_informations, vue_choix, choix_modification
import re


def vue_choix_recherche_contrat():
    clear_terminal()
    print("Pour chercher les contrats par le nom du client, veuillez saisir 1\n")
    print("Pour chercher les contrats par l'ID du contrat, veuillez saisir 2\n")
    return vue_choix(2)


def vue_creation_contrat():
    infos_contrat = {}
    print("Veuillez saisir l'ID du collaborateur:")
    infos_contrat["ID collaborateur"] = verification_input(" - ", lambda id_collaborateur: re.match(r"^\d+$", id_collaborateur))

    print("Veuillez saisir le montant total, en € avec un . pour les décimales:")
    infos_contrat["Montant total"] = verification_input(" - ", lambda montant_tot: re.match(r"^\d+([.]\d{1,2})?$", montant_tot))
    
    print("Veuillez saisir le montant qu'il reste à payer, en € avec un . pour les décimales:")
    infos_contrat["Reste à payer"] = verification_input(" - ", lambda montant_rest: re.match(r"^\d+([.]\d{1,2})?$", montant_rest))

    print("Statu du contrat :")
    while True:
        choix = input("Est-il signé?\nOui\nNon\n")
        if re.match(r"^OUI$", choix, re.I):
            infos_contrat["statu du contrat"] = True
            break
        if re.match(r"^NON$", choix, re.I):
            infos_contrat["statu du contrat"] = False
            break
        else:
            print("Choix non valide, entrez \"oui\" ou \"non\"\n")

    return infos_contrat


def vue_modification_contrat(contrat):
    client = demander_modification(
        "ID client",
        contrat.id_client,
        "Veuillez saisir l'ID du client.\n - ",
        lambda id_client: re.match(r"^\d+$", id_client)
    )

    collaborateur = demander_modification(
        "ID collaborateur",
        contrat.id_collaborateur,
        "Veuillez saisir l'ID du collaborateur:\n - ",
        lambda id_collaborateur: re.match(r"^\d+$", id_collaborateur)
    )

    montant_total = demander_modification(
        "Le montant total",
        contrat.montant_total,
        "Veuillez saisir le montant total, en € avec un . pour les décimales:\n - ",
        lambda montant_tot: re.match(r"^\d+([.]\d{1,2})?$", montant_tot)
    )

    reste_a_payer = demander_modification(
        "Le montant qu'il reste à payer",
        contrat.reste_a_payer,
        "Veuillez saisir le montant qu'il reste à payer, en € avec un . pour les décimales:\n - ",
        lambda montant_rest: re.match(r"^\d+([.]\d{1,2})?$", montant_rest)
    )

    print(f"\nStatus du contrat actuel: {contrat.status_contrat}")
    choix = choix_modification()
    if choix:
        while True:
            choix = input("Est-il signé?\nOui\nNon\n")
            if re.match(r"^OUI$", choix, re.I):
                status_contrat = True
                break
            if re.match(r"^NON$", choix, re.I):
                status_contrat = False
                break
            else:
                print("Choix non valide, entrez \"oui\" ou \"non\"\n")
    else:
        status_contrat = contrat.status_contrat

    infos_contrat = {
        "id_client": client,
        "id_collaborateur": collaborateur,
        "montant_total": montant_total,
        "reste_a_payer": reste_a_payer,
        "status_contrat": status_contrat
        }

    return infos_contrat


def vue_choix_contrat(contrats):
    if contrats:
        vue_affichage_informations(contrats)
    choix = input("Veuillez saisir l'ID du contrat\n - ")
    return choix


def vue_filtre_contrat():
    print("Pour afficher les contrats non signer, veuillez saisir 1\n")
    print("Pour afficher les contrats non payés, veuillez saisir 2\n")
    return vue_choix(2)
