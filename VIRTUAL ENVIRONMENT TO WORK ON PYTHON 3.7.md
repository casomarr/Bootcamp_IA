In **Bootcamp_IA** folder:

Pour installer python 3.7 et son environnement virtuel
```sh
sudo apt update
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.7
sudo apt install python3.7-venv
```

Pour check
```sh
python3.7 -V
```

Pour créer environnement virtuel:
```sh
python3.7 -m venv bootcamp
```

Pour activer l’environnement virtuel
```sh
source bootcamp/bin/activate
```

Pour quitter l’environnement virtuel
```sh
deactivate
```
Pour supprimer l’environnement virtuel
```sh
rm -rf bootcamp
```
