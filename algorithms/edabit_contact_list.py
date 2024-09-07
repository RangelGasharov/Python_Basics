def sort_contacts(contacts_list, order_type):
    if contacts_list is None:
        return []
    contacts_list = separate_names(contacts_list)
    reverse_order = order_type == "DESC"
    contacts_list.sort(reverse=reverse_order)
    result = []
    for name in contacts_list:
        result.append(name[1] + " " + name[0])
    return result


def separate_names(names):
    result = []
    for name in names:
        index = -1
        for i in range(len(name)):
            if name[i] == " ":
                index = i
                break
        result.append([name[index + 1:], name[:index]])
    return result


print(sort_contacts(["John Locke", "Thomas Aquinas", "David Hume", "Rene Descartes"], "ASC"))
print(sort_contacts(["Paul Erdos", "Leonhard Euler", "Carl Gauss"], "DESC"))
print(sort_contacts(['Michael Phelps', 'Jesse Owens', 'Michael Jordan', 'Usain Bolt'], 'DESC'))
print(sort_contacts(['Al Gore', 'Barack Obama'], 'ASC'))
print(sort_contacts(['Albert Einstein'], 'ASC'))
print(sort_contacts([], "DESC"))
print(sort_contacts(None, "DESC"))
