
# TypeR

Ce projet est un bot Discord qui permet aux utilisateurs de tester leur vitesse et leur précision de frappe. Le bot fournit une phrase choisie au hasard à partir d'un Google Sheet et mesure les mots par minute (WPM) de l'utilisateur ainsi que le nombre d'erreurs commises lors de la frappe de la phrase.


## Features

- Sélectionne une phrase au hasard à partir d'une liste personnelle, d'un générateur de phrases en ligne ou d'une feuille de calcul Google Sheets.
- Affiche un compte à rebours avant de commencer le test de frappe.
- Mesure la vitesse de frappe (WPM) et la précision (nombre d'erreurs) de l'utilisateur.
- Fournit un retour sur les résultats du test, notamment les WPM, le nombre d'erreurs et le temps écoulé.
- Empêche l'exécution de plusieurs tests simultanément.


## Installation

Installez les bibliothèques Python requises

```bash
pip install -r requirements.txt
```
    
Obtenez un jeton de bot Discord et le renseigner dans la variable token.

Configurez un projet Google Cloud Platform, activez l'API Google Sheets et créez un compte de service avec les autorisations appropriées. Téléchargez le fichier JSON des informations d'identification du compte de service et remplacez `'keys.json'` par le chemin du fichier.

Renseignez l'ID de votre feuille de calcul Google Sheets contenant les phrases dans la variable SAMPLE_SPREADSHEET_ID.
## Utilisation

```
1. Exécutez le script Python : 'python main.py'
2. Invitez le bot sur votre serveur Discord.
3. Dans un canal textuel Discord, tapez '!start' pour lancer un test de frappe.
4. Le bot fournira un compte à rebours et affichera une phrase choisie au hasard.
5. Tapez la phrase aussi rapidement et précisément que possible.
6. Une fois que vous avez fini de taper, le bot affichera les résultats de votre test, notamment les WPM, le nombre d'erreurs et le temps écoulé.
```

