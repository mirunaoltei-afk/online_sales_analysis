# Online Sales Analysis

## Descriere

Online Sales Analysis este un proiect Python pentru gestionarea produselor unui magazin online și a coșului de cumpărături. Proiectul utilizează concepte de programare orientată pe obiecte (OOP) și Git/GitHub pentru controlul versiunilor.

## Clase

### Product

Clasa `Product` reprezintă un produs din magazin.

Atribute:

* `name` – numele produsului
* `price` – prețul produsului
* `quantity` – cantitatea disponibilă

Funcționalități:

* afișarea informațiilor despre produs
* actualizarea cantității produsului

### ProductManager

Clasa `ProductManager` gestionează produsele disponibile în magazin.

Funcționalități:

* adăugarea produselor
* afișarea produselor
* calcularea valorii totale a inventarului
* eliminarea unui produs după nume

### Cart

Clasa `Cart` gestionează coșul de cumpărături al clientului.

Funcționalități:

* adăugarea produselor în coș
* afișarea produselor din coș
* calcularea valorii totale de plată

## Fișierele proiectului

* `product.py` – conține clasa Product
* `product_manager.py` – conține clasa ProductManager
* `cart.py` – conține clasa Cart
* `main.py` – rulează funcționalitățile proiectului
* `.gitignore` – exclude fișierele care nu trebuie urmărite de Git

## Tehnologii utilizate

* Python
* Git
* GitHub
* Visual Studio Code
