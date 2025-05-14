types = {
    1: "Блокирующий",
    2: "Критический",
    3: "Значительный",
    4: "Незначительный",
    5: "Тривиальный",
}
tickets = {
    1: ["API_45", "API_76", "E2E_4"],
    2: ["UI_19", "API_65", "API_76", "E2E_45"],
    3: ["E2E_45", "API_45", "E2E_2"],
    4: ["E2E_9", "API_76"],
    5: ["E2E_2", "API_61"],
}
spisok = []


def constant_takes(list):
    global spisok
    final_spisok = []
    for i in list:
        if i not in spisok:
            spisok.append(i)
            final_spisok.append(i)

    return final_spisok


def criticality_level(types, tickets):
    tickets_by_type = {}
    for key in types:
        tickets_by_type[types[key]] = constant_takes(tickets[key])

    print(tickets_by_type)
    return tickets_by_type


criticality_level(types, tickets)
