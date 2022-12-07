# Závěrečný projekt z předmětu AP1VS
Tento repozitář slouží jako podklad a vzor pro závěrečný projekt z předmětu AP1VS.

## Požadavky na projekt
* Projekt bude řešen formou forku a odevzdán pomocí pull requestu na githubu
    * nakonec hlavní řešitel odevzdá projekt pomocí pull requestu
* Kód musí být okomentovaný (ideálně všechny entity)
* Kód musí obsahovat unit testy (pokrytí kódu testy by se mělo blížit 100%)
* Zdrojový kód musí projít kontrolním testem na githubu v sekci Actions (je nutné povolit). Tzn. musí projít všechny unit testy a kontola pomocí flake8 a flake8-docstrings
* Zároveň dojde k automatickému vygenerování dokumentace s docstringů pomocí knihovny pdoc.

PYTEST

	py.exe -m pip install -U pytest

	py.exe -m pip install pytest-cov

	py.exe -m pytest --cov=. --cov-fail-under=90 --cov-report term-missing

	py.exe -m pytest --doctest-modules --cov=. --cov-fail-under=90 --cov-report term-missing

FLAKE8

	py.exe -m pip install flake8 flake8-docstrings

	py.exe -m flake8 rimcis.py

	py.exe -m flake8 test_rimcis.py

PDOC

	py.exe -m pip install pdoc

	py.exe -m pdoc rimcis.py

	py.exe -m pdoc test_rimcis.py

## Postup

2. Nastavte si přístup na GitHub z vašeho počítače, použijte a credential helper jako je [Git Credential Manager](https://github.com/GitCredentialManager/git-credential-manager/blob/main/README.md) nebo si vygenerujte osobní přístupový token: [a personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token). Případně můžete commity provádět přes web GitHubu (což je ale hodně neprogramátorská varianta :wink:).

3. Naklonujte si svůj repozitář a nastavte si upstream (toto provedou všichni uživatelé, neboť každý uživatel musí provést alespoň jeden commit):

    Naklonování vašeho repozitáře do aktuálního adresáře:
    
        git clone https://github.com/d-stefka/AP1VS-final-project.git
        
    Přejděte do adresáře s naklonovaným repozitářem:
    
        cd vs_project
        
    Přiřaďte originální repozitář k vašemu forku:
    
        git remote add upstream https://github.com/tureckova/AP1VS-final-project

3. Aktualizace z originálního repozitáře, přijetí změn z upstream:

        git pull upstream master
    
4. Commitujte vaše změny po logických oddílech, každý commit s výstižným popisem:

        git commit -m "logical commit description"
    
5. Proveďte push vašich změn na server:

        git push
    
6. Otevřete tzv. pull request s názvem a popisem projektu, návod jak na to [zde](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork)
    
7. Do moodlu každý řešitel odevzdá pouze odkaz na github stránku vašeho projektu - url adresu forku vašeho projektu - a url adresu svého účtu na GitHub.
