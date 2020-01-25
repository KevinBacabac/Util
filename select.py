import fnmatch


def multiple(given_list, multiple_select, autoselect):
    """ Selects one or more from a given list """

    assert len(given_list) > 0

    # All items to select from
    list_choice = sorted(given_list)
    # Selectable items
    search_results = list_choice.copy()
    selected = []

    while True:
        # Autoselect when one result left
        if len(search_results) == 1 and autoselect and not selected:
            print('Auto-selecting', search_results[0])
            selected = [search_results[0]]
            break

        # Select from list
        if multiple_select:
            print('Multiple-select. Please select a number, choose a glob',
                  'search by entering a string.')
            print('Additional commands: "Finish", "All", or "Cancel".')
            print('Selected results:', str(selected))

        else:
            print('Single select. Please select a number or make a',
                  'glob search by entering a string. "Cancel".')
            print('Additional commands: "Cancel"')

        for i, option in enumerate(search_results):
            print(str(i + 1) + '.', option)

        # userInput as integer occurs with 1 as initial, but array starts at 0
        userInput = input()

        if userInput == 'Cancel':
            selected = []
            break

        elif userInput == 'Finish' and multiple_select:
            break

        elif userInput == 'All' and multiple_select:
            selected = search_results.copy()
            break

        else:
            # Separate number from query
            try:
                userInput = int(userInput)

            except ValueError:
                # User chose a string
                search_results = fnmatch.filter(search_results, userInput)

                if not search_results:
                    print('No results would be found. Resetting query.')
                    search_results = list_choice.copy()

            else:  # User chose an integer
                maxBounds = len(search_results) + 1
                if userInput in range(1, maxBounds):
                    # In domain
                    if multiple_select:
                        selected.append(search_results[userInput - 1])
                        del search_results[userInput - 1]

                        if not search_results:
                            print('No results left. Finishing selection.')
                            break

                    else:
                        selected = [search_results[userInput - 1]]
                        break

                else:
                    print('Input must be within 1 -', maxBounds - 1)

    if multiple_select:
        return selected

    assert len(selected) <= 1
    if selected:
        return selected[0]
    else:
        return None
