# Projet Devops

Pour notre projet, nous avons utilisé terraform pour créer 3 instances sur lesquelles nous avons déployé des serveurs haproxy, apache et notre calculatrice. Nous avons ensuite utilisé ansible pour la configuration de nos serveurs.
Notre rapport explique le choix de nos technologies et les problèmes qu'on a
rencontré, ci_après le lien [RAPPORT DEVOPS](rapport/Rapport_devops.pdf)

Pour expliquer plus en détail les outils, stacks et autres qu'on a utilisé, vous allez trouvé les **README.md** pour chaque partie dans les dossiers. 
 

### Dossier ansible

Contient le code ansible pour configurer les serveurs.
[Link to ANSIBLE README](ansible/README.md)


### Dossier application 
Contient l'application calculatrice ainsi que les tests qui sont liés à ce dernier.

[Link to APPLICATION README](application/README.md)


### Dossier terraform

Contient tout le code terraform pour créer l'instance.

[Link to TERRAFORM README](terraform/README.md)


### Dossier sonarqube 
Ce dossier comprend les fichiers utilisés pour le déploiement de sonarqube.

[Link to SONARQUBE README](sonarqube/README.md)

### Dossier monitoring 

Ce dossier comprend les fichiers utilisés pour le dashboard grafana

[Link to MONITORING README](monitoring/README.md). 

[Link to DASHBOARD  README](.gitlab/dashboards/README.md).


### fichier .gitlab-ci.yml

Nous allons expliquer brievement les stages qu'on a crée.

- infra_validate : On initialise d'abord notre configuration terraform et on vérifie si la syntaxe et la structure de nos fichiers de configuration Terraform sont corrects.

- plan-apply : On affiche une liste détaillée des actions que Terraform exécutera sur notre configuration et si tout est ok, on applique ces modifications pour créer nos instances EC2.

- build : on utilise une image python pour tester si l'application "compile" bien ou si il y a des erreurs avec la commande de base que l'utilisateur pourrait taper.

- test-calculator : ensuite on teste l'application, c'est le lancement d'un ensemble des tests unitaires, on veut être sur que toutes les fonctionnalités de la calculatrice soient tester, dans le futur si on souhaite rajouter des fonctionnalités il faudra juste rajouté une fonction dans le fichier test.

- performance-test : afin de simuler plusieurs utilisateurs utilisant l'application dans un laps de temps donné et donc faire un "stress-test", ensuite on garde les résultats dans un artefact qui pourra être utilisé ultérieurement notamment pour grafana.

- security-test : pour tester notre projet s'il y a des vulnérabilités de sécurité à corriger, la pipeline va fail pour faire savoir qu'il faut corriger le code.

- release : On devrait conteneurisé notre sonarqube dans un ECR sur le tenant AWS mais dû à des soucis d'authentification avec docker, le stage n'a pas pu s'exécuter correctement.

- deploy_validate : Une dernière vérification de la structure de nos fichiers de configuration terraform est effectuée avant le déploiement définitif.

- deploy_plan_apply: On effectue dans ce stage le déploiement définitif de nos instances EC2.

- setup : On décrypte ici le fichier vault.yaml qui contient des données sensibles d'authentification.

- provisioning_ansible : On effectue le déploiement de notre application (calculatrice) sur l'une des instances créé avec terraform.

- monitoring : pour integré le dashboard grafana

## Contributors

- #### BAHOUNDJE Immaculée
- #### MUR Valentin
- #### RATOVOHERINJANAHARY Elodie 

