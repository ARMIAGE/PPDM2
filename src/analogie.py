def analogie_QuestionsWords(model):
    accuracy = model.accuracy('../DATA/questions-words.txt')
    sum_corr = len(accuracy[-1]['correct'])
    sum_incorr = len((accuracy[-1]['incorrect']))
    total = sum_corr + sum_incorr
    percent = lambda a: a / total * 100
    print('Nombre de phrases: {}, Correctes: {:.2f}%, Incorrectes: {:.2f}%'.format(total, percent(sum_corr),
                                                                                   percent(sum_incorr)))
    return