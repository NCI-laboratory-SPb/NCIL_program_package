import matplotlib.pyplot as plt

class Science_Plot:
    """Class Science_Plot.
    
    """

    @staticmethod
    def plt_clv_clv(clvs_lsts, colvar1_num = 0, colvar2_num = 1):
        """Get lists of coolvars and make plot colvar_1 - colvar_2"""
        if len(clvs_lsts.colvars_lsts) < 2:
            print("We can't make plot for one collective variable.")
            return None
        
        plt.scatter(clvs_lsts.colvars_lsts[colvar1_num], clvs_lsts.colvars_lsts[colvar2_num], s = 1)
        plt.show()