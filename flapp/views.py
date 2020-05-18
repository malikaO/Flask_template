from flask import Flask, render_template, url_for

app = Flask(__name__)

#p.route('/')
#def index():
 #   return "Hello malika!"


@app.route('/')
def home():
   # dictionnaire de data:
   data = {"name": "Malika Ouizbouben",
   "Nom_famille": "Ouizbouben", 
   "Prénom": "Malika" ,
    "Adresse":"" ,
    "Tel": "", 
    "Mail": "" }

   experiences = {"Expérience_1": "VENDEUSE EN BOULANGERIE" ,
    "Détail_1": "Accueil du client, évaluation de ses besoins et conseil. Prise des commandes et encaissement. Respect des règles d'hygiène et de sécurité alimentaire. Entretien du magasin et contrôle de la conservation des produits. Organisation et mise en place des produits. Gestion des stocks et réapprovisionnement. Saisie de facture.",
    "Entreprise_1 ": "BOULANGERIE LA GENTILLAISE",
    "Date_1": "01/2009 - 07/2019", 
    "Expérience_2": "ASSISTANTE COMPTABLE", 
    "Entreprise_2 ":"STUDIO 107",
    "Date_2": "09/2008 - 10/2008",
    "Détail_2": "Gestion de la comptabilité client. Enregistrement des règlements, lettrage et relance client. Rapprochement bancaire. Suivi et comptabilisation des notes de frais. Saisie de factures. Suivi de trésorerie.",
    "Expérience_3": "ASSISTANTE COMPTABLE", 
    "Entreprise_3 ":"FEEDBACK",
    "Date_3": "07/2007 - 09/2007",
    "Détail_3": "Gestion de la comptabilité fournisseur. Gestion de la comptabilité client. Enregistrement des règlements. Rapprochement bancaire. Suivi et comptabilisation des notes de frais. Saisie de facture. Suivi de trésorerie.",
    "Expérience_4": "STAGE AU SERVICE ACHAT",
    "Entreprise_4 ": "ORVIF",
    "Date_4": "07/2006 - 08/2006",
    "Détail_4": " Gestion des commandes. Mise à prix des commandes. Enregistrement des règlements. Relance client. Saisie de facture.",
    "Expérience_5": "STAGE AU SERVICE ÉCONOMIQUE ET FINANCIER",
    "Entreprise_5 ": "HÔPITAL TENON",
    "Date_5": "06/2006 - 07/2006",
    "Détail_5": " Gestion de la comptabilité fournisseur. Gestion des commandes. Enregistrement des règlements. Rapprochement bancaire."
}
   presentation = {"Présentation": "Après avoir validé un master 1 en Economie et Gestion, pour des raisons personnelles j'ai dû commencer à travailler. Une opportunité s'est présentée à moi dans une boulangerie, en tant que vendeuse. Je garde de cette expérience de nombreuses compétences: l'organisation, la discipline, le travail en autonomie, en équipe, la communication, le relationnel, ainsi que la gestion du stress.<br> J’ai ressenti le besoin et l’envie de retourner vers mon amour premier : les maths. Les maths, la gestion des données , le Big Data sont aujourd’hui essentiels dans notre société. L’intelligence artificielle et le numérique sont des domaines qui attisent ma curiosité. L'IA est un domaine d'avenir et d'innovations. L'IA combinée à l'intelligence humaine ouvrent un champs de possibilités à l'infini et pour tous les secteurs d’activités. Ce domaine me passionne , nourrit ma curiosité . Je souhaite participer aux innovations du futur et aux opportunités qu'elles seront pour l'humanité. La formation Simplon X Microsoft est la plus réputée dans ce domaine , il était évident pour moi que c'était la formation à faire."}
   formations = {"Formation_1": "Ecole Intelligence Artificielle Microsoft X Simplon",
     "Certificat_1": "",
     "Intitulé_1": "",
     "Année_1": "Mars - Octobre 2020",
     "Formation_2": "Apple fundation X Simplon",
     "Certificat_2": "",
     "Intitulé_2": "",
     "Année_2": "Janvier 2020",
     "Université": "Sorbonne",
     "Diplôme": "Master 1",
     "Intitulé_3": "Economie et Gestion d'entreprise.",
     "Année_3": "2008",
     "Lycée": "Lycée Darius Milhaud",
     "Bac": "Bac scientifique",
     "Spécialité": "Spécialité Mathématiques",
     "Année_4": "2001"
   }
  # competences = {
       #"html": "fab fa-html5",
       #"css": "fab fa-css3-alt",
       #"python": "fab fa-python",
       #"R": "fab fa-r-project",
       #"swift": "fab fa-swift",
       #"node_js": "fab fa-node-js"
    #}
   workflow = {
        "w_1": "Analyser les besoins du client et le conseiller.",
        "w_2": "Argumentation commerciale.",
        "w_3": "Travail en équipe.",
        "w_4": "Travail  en autonomie."
    }
   interets = {
        "Loisir_1" : "Natation",
        "Loisir_2" : "Voyage",
        "Langue_1": "Anglais (intermédiaire)",
        "Langue_2": "Arabe (intermédiaire)",
        "Permis": "B - Véhicule léger"
            }
   return render_template('index.html',title= "Home", data= data, presentation = presentation,formations = formations,experiences = experiences, workflow = workflow, interets = interets)


if __name__ == "__main__":
    app.run(debug=True)







