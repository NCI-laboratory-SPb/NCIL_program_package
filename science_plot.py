import matplotlib.pyplot as plt
import numpy as np

class Science_Plot:
    """Class Science_Plot.
    
    """

    @staticmethod
    def plt_clv_clv(clvs_lsts, colvar1_num=0, colvar2_num=1, title='Graph', x_label='q1', y_label='q1', font_size=14, trandline=False):
        """Get lists of coolvars and make plot colvar_1 - colvar_2"""
        x = clvs_lsts.colvars_lsts[colvar1_num]
        y = clvs_lsts.colvars_lsts[colvar2_num]

        if len(clvs_lsts.colvars_lsts) < 2:
            print("We can't make plot for one collective variable.")
            return None
        
        plt.title(title, fontsize=int(font_size))
        plt.xlabel(x_label+'_'+str(colvar1_num), fontsize=int(font_size))
        plt.ylabel(y_label+'_'+str(colvar2_num), fontsize=int(font_size))
        plt.scatter(x, y, s = 1)

        if trandline == 'linear':
            a, b = np.polyfit(x, y, 1)
            y_trend = a*x + b
            equation = f'y = {round(a, 2)}x + {round(b, 2)}'
            plt.text(0.5, 0.9, equation, fontsize=font_size, transform=plt.gca().transAxes)
            plt.plot(x, y_trend, color = 'red')

        plt.show()
        return None