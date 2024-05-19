# Curs_CVGJ_24_flori
![alt text](img1.png)
![alt text](img2.png)
![alt text](img3.png)
# Aplicația Web Flask pentru Zambile

Aceasta este o aplicație web simplă realizată cu Flask, care servește trei pagini HTML diferite despre "zambile".

## Configurare și Instalare

1. **Clonează depozitul** 

2. **Creează un mediu virtual**

    ```bash
    python3 -m venv venv
    source venv/bin/activate 
    ```

3. **Instalează dependențele**:

    ```bash
    pip install Flask
    ```

## Rularea Aplicației

1. **Setează variabila de mediu** 

    ```bash
    export FLASK_APP=zambila.py 
    ```

    Pe Windows, folosește `set` în loc de `export`.

2. **Rulează aplicația Flask**:

    ```bash
    flask run
    ```

3. **Deschide browserul web**:`http://127.0.0.1:5000/`.

## Rutele Aplicației

- **`/`**: Servește șablonul `zambila.html`.
- **`/descriere`**: Servește șablonul `descriere_zambila.html`.
- **`/poze`**: Servește șablonul `poze_zambila.html`.