colors = 'white\nred\ngreen\nwhite'

def will_explode(colors):
    list_of_colors = colors.split("\n")
    for i,color in enumerate(list_of_colors):
        if color == 'white':
            try:
                if (list_of_colors[i+1] == 'white' or list_of_colors[i+1] == 'black'):
                    return True
            except IndexError:
                return False
        elif color == "red":
            try:
                if (list_of_colors[i+1] != 'green'):
                    return True
                else:
                    return False
            except IndexError:
                return True
        # realizing this sol'n is really bad gonna see what other people did

will_explode(colors)
