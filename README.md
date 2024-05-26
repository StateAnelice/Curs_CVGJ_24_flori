1. M-am asigurat ca python3, pytest, flask si pylint sunt instalate si ruleaza cu succes. 

![image](https://github.com/StateAnelice/Curs_CVGJ_24_flori/blob/devel/Marius_Dutu/ss1.png)

2.Aplicatia.
Creearea aplicatiei: Cu gedit am creat fisierul 444D_flori.py in directorul app si fisierul biblioteca_flori.py in app/lib. 
Fisierul 444D_flori.py este o aplicatie WEB/Flask ce implementeaza o pagina ce afiseaza descrierea si provenienta culorii papadiei. 
In fidierul biblioteca_flori.py sunt implementate doua functii ce sunt apelate de aplicatia principala. 

Pentru rularea aplicatiei s-au introdus comenzile: 
    . .venv/bin/activate 
    export FLASK_APP=444D_flori.py 
    flask --app 444D_flori.py --debug run 

Pentru a vizualiza aplicatia se acceseaza un browser de internet si se apeleaza 127.0.0.1:5000.

![image](https://github.com/StateAnelice/Curs_CVGJ_24_flori/blob/devel/Marius_Dutu/run.png)

Testarea aplicatiei s-a facut atat cu Jenkins, cat si cu pytest. S-a creat in directorul app fisierul test_444D_flori in care s-a testat daca o anumita secventa se regaseste in functiile din biblioteca, daca da atunci testul a fost trecut . S-au creat in directorul app si fisierele activeaza_venv, activeaza_venv_jenkins, ruleaza_aplicatia si JenkinsFile in directorul Curs_CVGJ_24_flori. Aceste fisiere sunt folosite pentru testarea cu Jenkins. Pentru aceasta se incepe rularea jenkins din terminal, apoi se acceseaza din browser. Se creeaza un nou item unde se introduce ca sursa adresa URL a repozitorului si branch-ul ce se doreste a fi testat.
Adaugare pe git: S-a creeat un branch nou folosind comanda git branch . S-a facut comutarea pe branch-ul nou creat cu git checkout . Apoi s-au introdus comenzile git add ., git -m commit si git push.

![image](https://github.com/StateAnelice/Curs_CVGJ_24_flori/blob/devel/Marius_Dutu/ss2.png)
![image](https://github.com/StateAnelice/Curs_CVGJ_24_flori/blob/devel/Marius_Dutu/ss3.png)
![image](https://github.com/StateAnelice/Curs_CVGJ_24_flori/blob/devel/Marius_Dutu/ss4.png)
![image](https://github.com/StateAnelice/Curs_CVGJ_24_flori/blob/devel/Marius_Dutu/ss5.png)
![image](https://github.com/StateAnelice/Curs_CVGJ_24_flori/blob/devel/Marius_Dutu/ss6.png)
![image](https://github.com/StateAnelice/Curs_CVGJ_24_flori/blob/devel/Marius_Dutu/ss7.png)
![image](https://github.com/StateAnelice/Curs_CVGJ_24_flori/blob/devel/Marius_Dutu/ss8.png)

Din pacate urmatoarele doua erori nu m-au lasat sa continui partea de docker.
Am incercat si solutia de aici : https://www.linkedin.com/pulse/resolving-docker-permission-denied-error-guide-om-prakash-singh
Insa fara succes..

![image](https://github.com/StateAnelice/Curs_CVGJ_24_flori/blob/devel/Marius_Dutu/Err1.png)
![image](https://github.com/StateAnelice/Curs_CVGJ_24_flori/blob/devel/Marius_Dutu/Err2.png)
