import pandas as pd
import numpy as np

# read in csv file
df = pd.read_csv('food.csv')

# lists that only have specific protein
beef = df[df['protein'] == 'beef']
chicken = df[df['protein'] == 'chicken']
pork = df[df['protein'] == 'pork']
seafood = df[df['protein'] == 'seafood']


def filter_limit(limit, protein):
    """
   check if there is dish under limit
    :param protein
   :param limit
   :return: dataframe
   """
    # filter dishes under calorie limit
    df_f = df[df.calories <= int(limit)]
    if protein == 'beef':
        # filter dishes by protein type
        beef_f = df_f[df_f['protein'] == 'beef']
        return beef_f
    elif protein == 'chicken':
        # filter dishes by protein type
        chicken_f = df_f[df_f['protein'] == 'chicken']
        return chicken_f
    elif protein == 'pork':
        # filter dishes by protein type
        pork_f = df_f[df_f['protein'] == 'pork']
        return pork_f
    else:
        # filter dishes by protein type
        seafood_f = df_f[df_f['protein'] == 'seafood']
        return seafood_f


def output(meal):
    """
    print meal selection, its calories and its recipe link
    :param meal: meal generated
    :return: none
    """
    # locate the index of meal generated
    meal_index = df.index[df.dish == meal]
    # get the calories and recipe of selected meal
    calories = df.calories[meal_index].values
    recipe = df.recipes[meal_index].values
    # print result
    """
    print()
    print('Hey, you are having', meal.upper(), 'for your dinner!')
    print('The calories of the meal is', calories)
    print('Here is the link of the recipe:\n', recipe)
    """
    return calories, recipe


def index(limit, protein):
    # random dish when no calories limit
    if limit < 0:
        if protein < 0:
            meal = np.random.choice(df['dish'].values)
            return meal
        elif protein == '1':
            meal = np.random.choice(beef['dish'].values)
            return meal
        elif protein == '2':
            meal = np.random.choice(pork['dish'].values)
            return meal
        elif protein == '3':
            meal = np.random.choice(chicken['dish'].values)
            return meal
        else:
            meal = np.random.choice(seafood['dish'].values)
            return meal
    else:
        if protein == '1':
            beef_dish = filter_limit(limit, 'beef')
            if len(beef_dish) == 0:
                return None
            else:
                meal = np.random.choice(beef_dish['dish'].values)
                calorie, recipe = output(meal)
                return meal, calorie, recipe
        elif protein == '2':
            pork_dish = filter_limit(limit, 'pork')
            if len(pork_dish) == 0:
                return None
            else:
                meal = np.random.choice(pork_dish['dish'].values)
                calorie, recipe = output(meal)
                return meal, calorie, recipe
        elif protein == '3':
            chicken_dish = filter_limit(limit, 'chicken')
            if len(chicken_dish) == 0:
                return None
            else:
                meal = np.random.choice(chicken_dish['dish'].values)
                calorie, recipe = output(meal)
                return meal, calorie, recipe
        else:
            seafood_dish = filter_limit(limit, 'seafood')
            if len(seafood_dish) == 0:
                return None
            else:
                meal = np.random.choice(seafood_dish['dish'].values)
                calorie, recipe = output(meal)
                return meal, calorie, recipe
