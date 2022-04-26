from IPython.display import clear_output
import matplotlib.pyplot as plt

def PlotMetrics(train, validate = None, 
                     clear = True, train_color = 'red', 
                     validate_color = 'blue', train_labels = None, validate_labels = None, 
                     plot_name = None, folder = "./"
                    ):
    folder = folder if folder[-1] == '/' else folder + '/'
    plot_name = None if plot_name is None else folder + plot_name
    
    if (clear):
        clear_output()
        
    if (train_labels is not None):
        train_title, train_x, train_y = train_labels
    else:
        train_title, train_x, train_y = "Train Loss Over Time", "Epochs", "Loss"
        
    if (validate_labels is not None):
        validate_title, validate_x, validate_y = train_labels
    else:
        validate_title, validate_x, validate_y = "Validate Loss Over Time", "Epochs", "Loss"
        
    
    fig, axs = plt.subplots(2 if validate is not None else 1, 1)
    axs[0].plot(train, color = train_color)

    axs[0].title.set_text(train_title)
    axs[0].set_xlabel(train_x)
    axs[0].set_ylabel(train_y)
    
    if (validate is not None):
        axs[1].plot(validate, color = validate_color)
        axs[1].title.set_text(validate_title)
        axs[1].set_xlabel(validate_x)
        axs[1].set_ylabel(validate_y)
        fig.tight_layout(h_pad=2)

    if (plot_name is not None):
        fig.savefig(plot_name)
    
    return fig, axs