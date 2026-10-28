from bs4 import BeautifulSoup


def analyser_images(html):
    soup = BeautifulSoup(html, "html.parser")
    problemes = []

    for image in soup.find_all("img"):
        if not image.has_attr("alt"):
            problemes.append(
                "Image sans attribut alt : " + str(image.get("src", "source inconnue"))
            )

    return problemes


def main():
    html = """
    <html>
        <body>
            <img src="photo.jpg">
            <img src="logo.png" alt="Logo de l'entreprise">
            <img src="graphique.png" alt="">
        </body>
    </html>
    """

    problemes = analyser_images(html)

    print("Rapport AccessiWeb")

    if problemes:
        for probleme in problemes:
            print("- " + probleme)
    else:
        print("Aucun problème détecté par cette règle.")


if __name__ == "__main__":
    main()