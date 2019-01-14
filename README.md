# Getting started
```bash
python manage.py migrate
python manage.py createsuperuser --username admin --email admin@test.fr
python manage.py loaddata packages
# Import cards from Admin
```

# TODO Minimal
- [X] Acheter des paquets de cartes
- [X] Constituer des decks, les enregistrer pour les réutiliser plus tard
- [X] Echanger des cartes avec un autre joueur (troc)
- [X] Vendre des cartes
- [X] Jouer contre un autre joueur
- [ ] Jouer contre un personnage non joueur, préconfiguré par l'administrateur
- [X] Suivre d'autres joueurs (vous aurez alors des informations sur leurs dernières actions dans votre flux d'actualité)
- [X] Discuter avec d'autres membres via des forums
- [X] Voir sa collection, et celle des autres joueurs

# TODO Bonus
- [ ] Constituer une guilde (avec un chef, et des lieutenants):
- [ ] Les lieutenants peuvent inviter de nouveaux membres, accepter/refuser les demandes, exclure des membres
- [ ] Le chef peut faire tout cela, et en plus promouvoir ou rétrograder des lieutenant parmi les membres
- [ ] Vous pouvez faire en sorte que les discutions sur les forums soient temps réel
- [ ] Vous pouvez mettre en place un système de classement ELO
- [ ] Vous pouvez faire en sorte que les parties soient interactives
- [ ] Vous pouvez faire des tournois