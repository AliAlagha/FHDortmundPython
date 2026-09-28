if __name__ == '__main__':
    events = {
        "26. DEW21 Museumsnacht": "2026-09-19",
        "Moderne Grossstadt Dortmund (film, Dortmunder U)": "2026-09-19",
        "Keycabs - Kunst unter den Fingerspitzen": "2026-09-19",
        "INDUSTRIAL: Seidenstrassen 3000": "2026-09-19",
        "8. Tag der offenen Wohnprojekte": "2026-09-27",
        "FAVORITEN Festival 26": "2026-10-01",
        "30. Dortmunder Hansemarkt": "2026-11-04",
        "Xavier Rudd concert": "2026-07-22"
    }
    night_of_museums = "2026-09-19"
    print("Events during the Night of Museums on 19 September 2026:")
    for name, date in events.items():
        if date == night_of_museums:
            print("-", name)
