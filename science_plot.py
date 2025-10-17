import matplotlib.pyplot as plt

class Science_Plot:
    """Class Science_Plot.
    
    """

    @staticmethod
    def plt_clv_clv(colvar_1, colvar_2):
        """Get lists of coolvars and make plot colvar_1 - colvar_2"""
        plt.scatter(colvar_1, colvar_2, s = 1)
        plt.show()