def analogie_QuestionsWords(model):
    """
    Cette fonction a pour but l'insertion et la transformation en matrice du fichier Questions Words

    :return: Une matrice de 3 colonnes (Mot 1, Mot 2, coef de correlation entre 0 et 1)
    """
    accuracy = model.accuracy('../DATA/questions-words.txt')
    sum_corr = len(accuracy[-1]['correct'])
    sum_incorr = len((accuracy[-1]['incorrect']))
    total = sum_corr + sum_incorr
    percent = lambda a: a / total * 100
    print('Nombre de phrases: {}, Correctes: {:.2f}%, Incorrectes: {:.2f}%'.format(total, percent(sum_corr),
                                                                                   percent(sum_incorr)))
    return
