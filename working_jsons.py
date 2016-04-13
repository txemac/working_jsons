__author__ = 'josebermudez'


def add_new_entry(month, entry):

    if not month or not entry:
        raise ValueError('error in parameters.')

    month['count'] += 1
    month['amount'] += entry['amount']
    month['num_items'] += entry['num_items']

    if entry['gender'] in month['gender'].keys():
        month['gender'][entry['gender']]['count'] += 1
        month['gender'][entry['gender']]['amount'] += entry['amount']
        month['gender'][entry['gender']]['num_items'] += entry['num_items']
    else:
        month['gender'][entry['gender']] = {
            "count": entry['count'],
            "amount": entry['amount'],
            "num_items": entry['num_items']
        }

    if entry['currency'] in month['currency'].keys():
        month['currency'][entry['currency']]['count'] += 1
        month['currency'][entry['currency']]['amount'] += entry['amount']
        month['currency'][entry['currency']]['num_items'] += entry['num_items']
    else:
        month['currency'][entry['currency']] = {
            "count": 1,
            "amount": entry['amount'],
            "num_items": entry['num_items']
        }

    return month
