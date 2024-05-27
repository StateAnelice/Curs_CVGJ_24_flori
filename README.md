1. Folder start: Am creat directorul **proiect**, unde am folosit comanda _git clone_, pentru a clona repository-ul de pe GitHub./
Am instalat si dependintele: **python3, pytest, flask, pylint**
![1](https://github.com/StateAnelice/Curs_CVGJ_24_flori/assets/161729268/ed759b2e-f81a-4f0a-8d50-0e95442633f5)
![2](https://github.com/StateAnelice/Curs_CVGJ_24_flori/assets/161729268/ba633926-ad64-4123-8214-491cf190eda2)

2.Creearea aplicatiei: Am creat fisierul **444D_flori.py** in directorul _app_ si fisierul **biblioteca_flori.py** in app/lib. Fisierul 444D_flori.py 
este o aplicatie de tip WEB/Flask ce implementeaza o pagina ce afiseaza descrierea si provenienta culorii margaretei. In fisierul biblioteca_flori.py
sunt implementate 2 functii ce sunt apelate la aplicatia principala. Pentru rularea aplicatiei s-au folosit comenzile:
![image](https://github.com/StateAnelice/Curs_CVGJ_24_flori/assets/161729268/de630ca1-d236-4f39-8a71-da7ffdde94c2)
![3](https://github.com/StateAnelice/Curs_CVGJ_24_flori/assets/161729268/7651613c-bd84-4d76-bbd2-c66bd7359072)
![4](https://github.com/StateAnelice/Curs_CVGJ_24_flori/assets/161729268/99e7f8bb-66a8-4da8-8c3a-96c1dbd0d9be)

3.Testarea:
  Testarea aplicatiei s-a facut folosind comanda pytest si s-a incercat si testarea in Jenkins, dar am obtinut o eroare pe care am atasat-o mai jos.
S-a creat in fisierul app si fisierele activeaza_venv, activeaza_venv_jenkins, ruleaza_aplicatia si Jenkinsfile in directorul curent. Aceste fisiere
ar fi trebuit folosite pentru testarea in Jenkins. Pentru aceasta se incepe testarea in terminal, apoi se continua in browser. In Jenkins se incepe prin
crearea unui **nou item**, apoi selectarea optiunii de pipeline, se introduce adresa URL a repository-ului si branch-ul ce se doreste a fi testat.
![5](https://github.com/StateAnelice/Curs_CVGJ_24_flori/assets/161729268/8e7af5b3-2594-4125-b00d-5bbe0ee9bb1a)
![6](https://github.com/StateAnelice/Curs_CVGJ_24_flori/assets/161729268/874e70ba-5f5a-42de-9f5b-901d0e0a2c50)
![7](https://github.com/StateAnelice/Curs_CVGJ_24_flori/assets/161729268/bb454986-4ef2-400a-acd5-a8a50f9dbaf5)
![11](https://github.com/StateAnelice/Curs_CVGJ_24_flori/assets/161729268/6122fde9-c58a-4cc0-85c8-d4bf570771da)

4.Adaugarea pe GIT. S-a creat un branch nou folosind comanda **git branch dev/AntonioMihaita**. S-a facut comutarea pe branch-ul nou creat cu 
**git checkout dev/AntonioMihaita**. Apoi s-au introdus comenzile **git add . // git commit -m "message" // git push origin main_AntonioMihaita**
![8](https://github.com/StateAnelice/Curs_CVGJ_24_flori/assets/161729268/a85d2d31-85c4-4f57-8c14-eb680ace1e0e)
![9](https://github.com/StateAnelice/Curs_CVGJ_24_flori/assets/161729268/d8c772c0-67b3-40e3-8419-1d3c629b5fff)
Aici am facut screenshot-ul gresit. Push-ul se facea in dev/AntonioConache, apoi din browser se facea pull request-ul din dev in main
![10](https://github.com/StateAnelice/Curs_CVGJ_24_flori/assets/161729268/445775ee-a063-4edd-ba88-0b53fe05b41b)
