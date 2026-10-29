
from bs4 import BeautifulSoup


def analyser_images(html):
    soup = BeautifulSoup(html, "html.parser")
    problemes = []

    for image in soup.find_all("img"):
        if not image.has_attr("alt"):
            source = image.get("src", "source inconnue")
            problemes.append(
                "Image sans attribut alt : " + source
            )

    return problemes


def main():
    with open("page_test.html", "r", encoding="utf-8") as fichier:
        html = fichier.read()

    problemes = analyser_images(html)

    print("Rapport AccessiWeb")
    print("------------------")
    print("Nombre de problèmes détectés :", len(problemes))
    print()
    if problemes:
        for probleme in problemes:
            print("- " + probleme)
    else:
        print("Aucun problème détecté par cette règle.")


if __name__ == "__main__":
    main()
