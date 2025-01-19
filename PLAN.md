# Cahier des charges

## Objectifs

### Description
* Fournir une calculatrice facile à utiliser, intégrée à l'outil de valorisation existant et utilisant la Notation Polonaise Inversée ([NPI](https://www.example.com)).
* Offrir des fonctionnalités de calcul pertinentes pour les besoins de vos clients, complémentaires à l'outil de valorisation déjà développé.

## Calculatrice
* **Fonctionnalités de base :** addition, soustraction, multiplication, division.
* **Documentation claire :** inclure des exemples d'utilisation pour garantir une adoption facile.
* **Interface utilisateur :** simple, ergonomique et compatible avec l'outil existant.

## Livrables
* **API :** Une API Python pour la calculatrice.
* **Tests complets :** unitaires, d'intégration, end-to-end, et de régression.
* **Documentation :** technique et utilisateur.
* **Interface :** Une interface front-end développée en React.js.
* **Format :** Docker container.

---

# Organisation

## Rôles et responsabilités
* **Product Owner :** priorisation des fonctionnalités et validation.
* **Lead Developer :** supervision technique et gestion des revues de code.
* **Développeurs Python :** implémentation des fonctionnalités.
* **Développeurs React.js :** création de l'interface utilisateur.
* **QA Tester :** définition des tests et vérification de la qualité du produit.

> Une personne peut assumer plusieurs rôles selon les besoins.

---

# Méthodologie

## Approches recommandées
* **TDD (Test Driven Development) :** garantir la qualité et la conformité aux besoins.
* **DDD (Domain Driven Design) :** découpler le projet pour une modularité et une évolutivité accrues.
* **Agile Scrum :** organisation en sprints courts (1 ou 2 semaines).

> Un sprint de 2 semaines est prévu pour cette amélioration.

---

# Planification

## Étape 1 : Préparation
* Rédaction des spécifications fonctionnelles et techniques (cahier des charges, diagrammes UML).
* Validation des besoins clients et alignement avec l'équipe (ex. : création de tickets dans Jira).
* Décision sur l'intégration de la calculatrice : service additionnel ou extension de l'outil existant.
* Analyse de l'impact sur le projet global (tests de régression).

> Durée prévue: 3 jours

## Étape 2 : Tests
* Rédaction des cas de test, couvrant tous les scénarios d'utilisation.

> Durée prévue: 2 jours

## Étape 3 : Développement

### Couche domaine
* Création des entités, agrégats et value objects pour répondre à la logique définie dans le cahier des charges.

> Durée prévue: 2 jours

### Couche applicative
* Création des commandes et requêtes :
  - **ComputeCommand** : réalise les calculs.
  - **GenerateCSVCommand** : génère un fichier CSV des calculs précédents.
  - **ReadManyCalculationsQuery** : retourne la liste des calculs.

> Durée prévue 3 jours

### Couche infrastructure
* Implémentation des dépôts (PostgreSQL/MongoDB) pour gérer les calculs.
* Création du générateur de fichiers CSV.

> Durée prévue: 3 jours

### Couche interface
* Développement d'une nouvelle route `calculator` pour effectuer les calculs et générer des fichiers CSV.

> Durée prévue: 3 jours

### Front-end
* Développement de l'interface utilisateur en React.JS

> Durée prévue: 3 jours

> Chaque couche peut être attribuée à un développeur différent, selon l'architecture DDD.

> Si qu'un seul développeur s'occupe de la réalisation du projet, alors la durée totale maximale de réalisation est estimée à 14 jours.

---

# Outils utilisés

## Containerization
`Docket / Docker compose`

## Gestion de projet
`Jira / GitHub Projects`

## Versionnage du code
`GitHub`

## Qualité du code
**Back-end** `ruff (Back-end)`

**Front-end** `eslint + prettier`

## Communication
`Slack / Microsoft Teams`

## CI/CD
`GitHub Actions`

# Livraison

1. Merge des braches avec l'environnement de développement.
2. Validation par le QA.
3. Déploiement en environnement de pré-production.
4. Validation par le maître d'ouvrage.
5. Déploiement en production.
6. Validation finale par le QA.
7. Validation finale par le maître d'ouvrage.
8. Formation éventuelle des utilisateurs.
