import numpy as np
#import fitsio
import matplotlib.pyplot as plt
import sep
from matplotlib.patches import Ellipse


def preprocess_dFFI(raw_data):
    """Preprocess the FFI

    Currently performs these pre processing steps:
    - Trims the edges to remove dark rows and collateral rows.
      TODO: currently hard coded to guesstimate of edges
    - Must use numpy C order to comply with sep's C functions

    Args:
        raw_data (numpy.ndarray): 2D numpy of one FFI channel

    Returns:
        trimmed_data (numpy.ndarray): A trimmed version of the input
    """
    raw_data = raw_data.copy(order='C')
    return raw_data[19:-28, 12:-20]



def quick_plot(data):
    """Make a quick plot of the FFI with sane screen stretch

    Returns:
        None
    """
    m, s = np.mean(data), np.std(data)
    plt.imshow(data, interpolation='nearest', cmap='gray', vmin=m-s, vmax=m+s, origin='lower')
    plt.colorbar();


def background_subtract(data, plot_bkg=False, return_bkg=False):
    """Background subtract the FFI

    Performs these steps:
    - Computes a mask based on the top 95th percentile of values
    - Estimate background with sep

    Args:
        data (numpy.ndarray): 2D numpy of one FFI channel
        plot_bkg (bool): Flag for whether to plot the background
                         default = False
        return_bkg (bool): Flag for whether to return the background
                         default = False

    Returns:
        background-subtracted FFI or optionally
        tuple of background-subtracted FFI, and background estimate
    """
    data = data.copy(order='C')
    mask = data > np.percentile(data, 95)
    bkg = sep.Background(data, mask=mask)

    if plot_bkg:
        bkg_image = bkg.back()
        # show the background
        plt.imshow(bkg_image, interpolation='nearest', cmap='gray', origin='lower')
        plt.colorbar();

    if return_bkg:
        return (data - bkg, bkg)
    else:
        return data - bkg


def plot_extractions(data_sub, df_objects):
    """Plot the detected traces with rectangles on the input image
    """
    # plot background-subtracted image
    fig, ax = plt.subplots()
    m, s = np.mean(data_sub), np.std(data_sub)
    im = ax.imshow(data_sub, interpolation='nearest', cmap='gray',
                   vmin=m-s, vmax=m+s, origin='lower')

    # plot an ellipse for each object
    for i in range(len(df_objects)):
        if df_objects.poor_fit[i]:
            color = 'red'
        elif df_objects.saturated[i]:
            color = 'yellow'
        else:
            color = 'blue'
        e = Ellipse(xy=(df_objects.x[i], df_objects.y[i]),
                    width=3*df_objects.a[i],
                    height=3*df_objects.b[i],
                    angle=df_objects.theta[i] * 180. / np.pi)
        e.set_facecolor('none')
        e.set_edgecolor(color)
        ax.add_artist(e)

    plt.axis('off')
    plt.show()


def plot_kernel(kernel, aper_mask=None):
    """Make a quick plot of the kernel with sane screen stretch

    Args:
        aper_mask (np.ndarray): Optionally overplot an aperture mask

    Returns:
        None
    """
    # show the image
    plt.imshow(kernel, interpolation='nearest', cmap='BuGn', vmin=0, vmax=np.max(kernel), origin='lower')
    if aper_mask is not None:
        plt.imshow(aper_mask, interpolation='nearest', cmap='BuGn', vmin=0, vmax=1, origin='lower', alpha=0.5)
    plt.colorbar();
