**\# Fusikab DJ**



!\[Logo Fusikab DJ\](static/images/logo\_fusikabdj\_noir.jpg)



**\*\*Fusikab DJ\*\*** est un site web professionnel pour présenter les services DJ, sonorisation, animation et prestations sur mesure pour tous types d’événements. Le site met en avant vos services, vos clients de confiance, ainsi que vos moments forts dans une galerie dynamique.



Le projet est développé avec **\*\*Flask\*\***, **\*\*Bootstrap 5\*\***, et un design sombre moderne avec des touches dorées pour un rendu élégant et professionnel.



\---



**\## Table des matières**



\- \[Fusikab DJ\](_#fusikab-dj_)

\- \[Table des matières\](_#table-des-matières_)

\- \[Fonctionnalités\](_#fonctionnalités_)

\- \[Technologies\](_#technologies_)

\- \[Installation\](_#installation_)



\---



**\## Fonctionnalités**



\- **\*\*Page d’accueil\*\*** avec présentation de Fusikab DJ et logo animé

\- **\*\*Section Nos Services\*\*** avec cartes interactives

\- **\*\*Section Ils nous font confiance\*\*** avec carousel des clients

\- **\*\*Galerie d’images\*\*** dynamique avec carousel et modal plein écran

\- **\*\*Pages légales\*\*** : CGV, CGU, Politique de Cookies, Politique de Confidentialité

\- **\*\*Page Contact\*\*** avec formulaire de contact

\- **\*\*Responsive design\*\*** adapté à tous les écrans

\- **\*\*Thème sombre\*\*** avec accents dorés et animations légères



\---



**\## Technologies**



\- **\*\*Backend :\*\*** Python 3, Flask

\- **\*\*Frontend :\*\*** HTML5, CSS3, JavaScript, Bootstrap 5

\- **\*\*Templates :\*\*** Jinja2

\- **\*\*Gestion des images :\*\*** Carousel Bootstrap + modal plein écran

\- **\*\*Hébergement :\*\*** Serveur Flask / WSGI



\---



**\## Installation**



1\. **\*\*Cloner le dépôt :\*\***



\`\`\`bash

git clone https://github.com/batrivieredev/fusikabdj.git

cd fusikabdj

Créer un environnement virtuel et l’activer :



bash

Copier le code

python3 \-m venv venv

source venv/bin/activate _\# macOS/Linux_

venv\\Scripts\\activate _\# Windows_

Installer les dépendances :



bash

Copier le code

pip install \-r requirements.txt

Lancer le serveur Flask :



bash

Copier le code

python run.py

Accéder au site :



Ouvrir http://127.0.0.1:5000 dans votre navigateur.



Structure du projet

csharp

Copier le code

fusikabdj/

│

├─ app.py / run.py _\# Entrée Flask_

├─ templates/ _\# Templates HTML Jinja2_

│ ├─ base.html _\# Template de base_

│ ├─ index.html _\# Page d’accueil_

│ ├─ gallery.html _\# Galerie_

│ ├─ contact.html

│ ├─ services.html

│ ├─ ... _\# Autres pages_

├─ static/

│ ├─ css/ _\# Feuilles de style_

│ ├─ js/ _\# Scripts JS_

│ ├─ images/ _\# Logos et images_

│ ├─ gallery/ _\# Galerie d’images_

│ └─ gallery\_confiance/ _\# Clients de confiance_

└─ README.md

Personnalisation

Ajouter des images dans /static/images/ ou /static/gallery/



Modifier les textes et titres directement dans les templates .html



Ajuster les couleurs et styles dans /static/css/



Contribution

Les contributions sont les bienvenues !



Fork le projet



Créez une branche pour vos modifications (git checkout \-b feature/nom-fonctionnalité)



Commitez vos changements (git commit \-m "Ajout d'une fonctionnalité")



Poussez la branche (git push origin feature/nom-fonctionnalité)



Ouvrez une Pull Request



Contact

Email : contact@fusikabdj.fr



Téléphone : 06 70 06 96 69



Site web : https://fusikabdj.fr
