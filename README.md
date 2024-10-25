<h1 align="center">
  <a href="">
    <picture>
      <source height="220" media="(prefers-color-scheme: white)" srcset="https://i.imgur.com/nGEReZh.png">
      <img height="300" alt="Helios" src="./HELIOS_LOGO.png" style="border-radius: 100%;">
    </picture>
  </a>
  <br>
</h1>
<p align="center">
   Un ensemble d'outils basé sur Python pour la collecte d'informations et la <br>reconnaissance
</p>

## À propos du projet

Helios est une boîte à outils tout-en-un, propulsée par Python, conçue pour simplifier le processus de collecte d'informations et de reconnaissance. Avec une interface conviviale et une suite de modules puissants.
Helios vous apporte une mine d'informations à portée de main, le tout réuni en un seul endroit.

## ⚠️ AVERTISSEMENT : DÉCLARATION LÉGALE

Cet outil est destiné **exclusivement à des fins éducatives et éthiques**. L'auteur ne saurait être tenu responsable de toute utilisation illégale ou abusive de cet outil. Les utilisateurs sont seuls responsables de leurs actions et doivent s'assurer d'avoir une autorisation explicite pour scanner les systèmes cibles.



## ⚙️ Installation

Pour commencer avec Helios, suivait les étapes suivantes:

```bash
git clone https://github.com/BenCoding/Helios.git
cd Helios
pip install -r requirements.txt
```

Une fois installé , vous pouvez lancer Helios comme ceci:

```bash
python3 Helios.py
```

---

## 📖 Liste Outils

Ce projet offre une riche collection d'outils répartis en plusieurs catégories : **DNS Tools**, **Domain and IP Information**, **Server and Network Tools**, **Web Application Analysis**, et **Security & Threat Intelligence**.

### Outils DNS

Ces outils permettent de recueillir des informations DNS et d'évaluer la configuration du domaine.

1. **DNS Over HTTPS** : Résolution DNS sécurisée via des canaux chiffrés.
2. **DNS Records** : Collecte des enregistrements DNS (A, AAAA, MX, etc.).
3. **DNSSEC Check** : Vérification de la configuration correcte de DNSSEC.
4. **TXT Records** : Récupère les enregistrements TXT utilisés à des fins de vérification.
5. **WHOIS Lookup** : Recherche WHOIS pour obtenir des informations sur le propriétaire d'un domaine.
6. **Zone Transfer** : Tentative de transfert de zone DNS pour découvrir des informations sensibles.

### Domaine et IP information

Ces outils aident à recueillir des informations sur le domaine et l'adresse IP.

7. **Domain Info** : Rassemble des informations sur le domaine (registrar, dates d'expiration, etc.).
8. **Domain Reputation Check** : Évaluation de la réputation du domaine à l'aide de diverses sources.
9. **IP Info** : Récupère des détails géographiques et sur le propriétaire de l'adresse IP.

### serveur et outil réseau

Ces outils permettent d'analyser l'infrastructure réseau et les serveurs.

10. **Associated Hosts** : Découverte des domaines associés à l'hôte cible.
11. **Server Info** : Extraction d'informations clés sur le serveur.
12. **Server Location** : Identification de l'emplacement physique du serveur.
13. **Traceroute** : Trace l'itinéraire des paquets jusqu'à la cible.

### Analyse application web

Ces outils sont axés sur l'analyse des applications web pour en comprendre la structure et la sécurité.

14. **Archive History** : Visualisation de l'historique du site à l'aide d'archives internet.
15. **Broken Links Detection** : Recherche de liens cassés susceptibles de causer des problèmes d'utilisateur ou de sécurité.
16. **CMS Detection** : Détection du CMS utilisé (WordPress, Joomla, etc.).
17. **Cookies Analyzer** : Analyse des cookies pour vérifier les attributs de sécurité et les problèmes de confidentialité.
18. **Content Discovery** : Découverte de fichiers et répertoires cachés sur le site.
19. **Crawler** : Exploration du site pour découvrir des données et cartographier sa structure.
20. **Robots.txt Analyzer** : Analyse du fichier `robots.txt` pour découvrir des ressources cachées.
21. **Directory Finder** : Recherche de répertoires qui ne sont pas indexés publiquement.
22. **Email Harvesting** : Extraction d'adresses e-mail du domaine cible.
23. **Sitemap Parsing** : Extraction des URLs à partir du sitemap du site.
24. **Technology Stack Detection** : Identification des technologies et frameworks utilisés par le site.
25. **Third-Party Integrations** : Découverte des services tiers intégrés dans le site.

### Securite & Threat Intelligence

Les modules de sécurité sont conçus pour évaluer les défenses de la cible et recueillir des informations sur les menaces.

26. **Certificate Authority Recon** : Examen des détails sur l'autorité de certification.
27. **Exposed Environment Files Checker** : Identification des fichiers `.env` exposés publiquement.
28. **HTTP Headers** : Extraction et évaluation des en-têtes de réponse HTTP.
29. **HTTP Security Features** : Vérification des en-têtes HTTP sécurisés, tels que HSTS et CSP.
30. **Shodan Reconnaissance** : Utilisation de Shodan pour découvrir les ports ouverts, services et vulnérabilités.
31. **SSL Labs Report** : Obtention d'un rapport détaillé sur SSL/TLS via SSL Labs.
32. **SSL Pinning Check** : Vérification de l'implémentation du SSL pinning sur le site.
33. **Subdomain Enumeration** : Découverte des sous-domaines du domaine cible.
34. **Subdomain Takeover** : Test des sous-domaines pour voir s'ils sont vulnérables à une prise de contrôle.

### Comment utiliser Helios

1. Lancez Helios depuis la ligne de commande.
2. Une liste de tool du mode audit vous ai fournis.
3. Lancer le mode AUDIT.
4. Suivez les instructions pour entrer les informations pertinentes.
5. Consultez les résultats et ajustez votre stratégie en conséquence.

**Example Command:**

```bash
root@Helios:~# test.fr
