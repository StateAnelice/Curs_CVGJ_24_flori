# Curs_CVGJ_24_flori
![alt text](image.png)
![alt text](image-1.png)
![alt text](image-2.png)
Started by user admin
Obtained Jenkinsfile from git https://github.com/StateAnelice/Curs_CVGJ_24_flori
[Pipeline] Start of Pipeline
[Pipeline] node
Running on Jenkins in /var/jenkins_home/workspace/Pipeline aplicatie
[Pipeline] {
[Pipeline] stage
[Pipeline] { (Declarative: Checkout SCM)
[Pipeline] checkout
Selected Git installation does not exist. Using Default
The recommended git tool is: NONE
No credentials specified
Cloning the remote Git repository
Cloning repository https://github.com/StateAnelice/Curs_CVGJ_24_flori
 > git init /var/jenkins_home/workspace/Pipeline aplicatie # timeout=10
Fetching upstream changes from https://github.com/StateAnelice/Curs_CVGJ_24_flori
 > git --version # timeout=10
 > git --version # 'git version 2.39.2'
 > git fetch --tags --force --progress -- https://github.com/StateAnelice/Curs_CVGJ_24_flori +refs/heads/*:refs/remotes/origin/* # timeout=10
 > git config remote.origin.url https://github.com/StateAnelice/Curs_CVGJ_24_flori # timeout=10
 > git config --add remote.origin.fetch +refs/heads/*:refs/remotes/origin/* # timeout=10
Avoid second fetch
 > git rev-parse origin/Tudor_Barnoaiea^{commit} # timeout=10
Checking out Revision 48c46f2f4fc0022afcc4d6ffb24caea1bb9a8011 (origin/Tudor_Barnoaiea)
 > git config core.sparsecheckout # timeout=10
 > git checkout -f 48c46f2f4fc0022afcc4d6ffb24caea1bb9a8011 # timeout=10
Commit message: "Tudor Barnoaiea: aplicatie floarea soarelui"
First time build. Skipping changelog.
[Pipeline] }
[Pipeline] // stage
[Pipeline] withEnv
[Pipeline] {
[Pipeline] stage
[Pipeline] { (Build)
[Pipeline] echo
Building...
[Pipeline] sh
+ pip install Flask --break-system-packages
Defaulting to user installation because normal site-packages is not writeable
Collecting Flask
  Downloading flask-3.0.3-py3-none-any.whl (101 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 101.7/101.7 kB 1.5 MB/s eta 0:00:00
Collecting Werkzeug>=3.0.0
  Downloading werkzeug-3.0.3-py3-none-any.whl (227 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 227.3/227.3 kB 3.3 MB/s eta 0:00:00
Collecting Jinja2>=3.1.2
  Downloading jinja2-3.1.4-py3-none-any.whl (133 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 133.3/133.3 kB 5.0 MB/s eta 0:00:00
Collecting itsdangerous>=2.1.2
  Downloading itsdangerous-2.2.0-py3-none-any.whl (16 kB)
Collecting click>=8.1.3
  Downloading click-8.1.7-py3-none-any.whl (97 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 97.9/97.9 kB 545.7 kB/s eta 0:00:00
Collecting blinker>=1.6.2
  Downloading blinker-1.8.2-py3-none-any.whl (9.5 kB)
Collecting MarkupSafe>=2.0
  Downloading MarkupSafe-2.1.5-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (28 kB)
Installing collected packages: MarkupSafe, itsdangerous, click, blinker, Werkzeug, Jinja2, Flask
  WARNING: The script flask is installed in '/var/jenkins_home/.local/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
Successfully installed Flask-3.0.3 Jinja2-3.1.4 MarkupSafe-2.1.5 Werkzeug-3.0.3 blinker-1.8.2 click-8.1.7 itsdangerous-2.2.0
[Pipeline] }
[Pipeline] // stage
[Pipeline] stage
[Pipeline] { (Test)
[Pipeline] echo
Running tests...
[Pipeline] sh
+ python3 -m unittest discover
...
----------------------------------------------------------------------
Ran 3 tests in 0.013s

OK
b'<!DOCTYPE html>\n<html lang="en">\n<head>\n    <meta charset="UTF-8">\n    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n    <title>Culoarea Floarea Soarelui</title>\n</head>\n<body>\n    <h1>Culoarea Floarea Soarelui</h1>\n    <p>Floarea-soarelui este predominant de culoare <strong>galben\xc4\x83</strong>.</p>\n    <a href="/">\xc3\x8enapoi la pagina principal\xc4\x83</a>\n</body>\n</html>'
b'<!DOCTYPE html>\n<html lang="en">\n<head>\n    <meta charset="UTF-8">\n    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n    <title>Descrierea Floarea Soarelui</title>\n</head>\n<body>\n    <h1>Descrierea Floarea Soarelui</h1>\n    <p>Floarea-soarelui (Helianthus annuus) este o plant\xc4\x83 anual\xc4\x83 din familia Asteraceae, nativ\xc4\x83 din America de Nord. Este bine cunoscut\xc4\x83 pentru capacitatea ei de a se \xc3\xaentoarce dup\xc4\x83 soare pe parcursul zilei. Florile sale mari \xc8\x99i galbene sunt foarte distinctive \xc8\x99i atr\xc4\x83g\xc4\x83toare, adesea asociate cu soarele.</p>\n    <a href="/">\xc3\x8enapoi la pagina principal\xc4\x83</a>\n</body>\n</html>'
b'<!DOCTYPE html>\n<html lang="en">\n<head>\n    <meta charset="UTF-8">\n    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n    <title>Floarea Soarelui</title>\n</head>\n<body>\n    <h1>Floarea Soarelui</h1>\n    <p>Floarea-soarelui (Helianthus annuus) este o plant\xc4\x83 originar\xc4\x83 din America, cunoscut\xc4\x83 pentru capacitatea sa de a se \xc3\xaentoarce dup\xc4\x83 soare.</p>\n    <img src="/static//images/sunflower.jpeg" alt="Sunflower">\n    <a href="/color"><button>Afl\xc4\x83 culoarea floarea-soarelui</button></a>\n    <a href="/description"><button>Cite\xc8\x99te descrierea floarea-soarelui</button></a>\n</body>\n</html>'
[Pipeline] }
[Pipeline] // stage
[Pipeline] stage
[Pipeline] { (Deploy)
[Pipeline] echo
Deploying...
[Pipeline] }
[Pipeline] // stage
[Pipeline] }
[Pipeline] // withEnv
[Pipeline] }
[Pipeline] // node
[Pipeline] End of Pipeline
Finished: SUCCESS
