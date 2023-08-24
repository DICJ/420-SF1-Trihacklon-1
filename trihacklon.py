class Program:
    """
    Dessine des formes à la console.
    """ 

    def convert_int(s: str, default: int) -> int:
        """
        Convertit une chaîne de caractères en un entier.

            Parameters:
                s (str): La chaîne de caractères à convertir.
                default (int): La valeur par défaut à utiliser si la conversion échoue.

            Returns:
                int: La valeur entière convertie si la conversion réussit, sinon la valeur par défaut.
        """
        try:
            i = int(s)
        except ValueError:
            i = default
        return i
    
    def main():
        """
        Dessine des formes à la console.
        """
        MIN = 3
        MAX = 31
        DEFAULT = 9

        n = Program.convert_int(input(f'Entrez un nombre impair entre {MIN} et {MAX}\n'), default = DEFAULT)
        if n % 2 == 0:
            n += 1
        n = min(max(n, MIN), MAX)
        print(f'n = {n}\n')
        
        # ************************** UN CARRÉ *****************************
        print('*********************************')
        print('La 1e diagonale noire')
        for rangee in range(n):
            for colonne in range(n):
                print('█', end = '')
            print()
        print()

        # ************************** TRIANGLE NORD-OUEST *****************************
        print('*********************************')
        print('Le triangle Nord-Ouest')
        for rangee in range(n):
            for colonne in range(n):
                if colonne < n - rangee:
                    print('█', end = '')
                else:
                    print(' ', end = '')
            print()
        print()

        
        # ************************** VOS DESSINS ICI *****************************
   
        
if __name__ == '__main__':
    Program.main()