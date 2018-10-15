"""
This module provides helper functions to support exercises during AM1
with outliers, robust regression and template regression in the CORE
data analytics workshop series, week 4.
"""

import numpy as np
import pandas as pd
import math
from collections import namedtuple

def recovery_sulphur_dataframe_with_outliers(outlier_probability):
    """Return dataframe representing recovery as a function of sulphur.

    Parameters:
    ----------
    outlier_probability:
        This floating point parameter should range between 0 and 1
        and is probability of an observation being an outlier.
    
    Returns:
    -------
    Pandas dataframe:
        A dataframe is returned with two series, the first being observed
        recovery, and the second being sulphur %.  The data may be sampled
        from the true underlying relationship, plus gaussian noise, or
        may be an outlier value taken from a non-gaussian distribution.

        The proportion of outliers to non-outliers will depend on
        the outlier_probability parameter.       
    """
    # Check that the outlier_probability is an ordinary number.
    assert isinstance(outlier_probability, (float, int))
    # As it's a probability, ensure that it ranges between 0 and 1.
    assert outlier_probability >= 0.0
    assert outlier_probability <= 1.0
    # If no exceptions have been thrown then we likely have a valid input.
    
    # Get 50 pairs of sulphur features and recovery labels
    sulphur_percent = _draw_sulphur_observations(50)
    recovery_percent = _observe_recovery(sulphur_percent, 
                                         outlier_probability)
    return pd.DataFrame({'metal_recovery_percent': recovery_percent,
        'feed_sulphur_percent': sulphur_percent})

def _initialise_randomstate(seed):
    """ Use RandomState object with seed set."""
    return np.random.RandomState(seed)

def _draw_sulphur_observations(count):
    rs = _initialise_randomstate(7)
    # draw "count" sulphur observations from a uniform distribution of
    # sulphur percentages between 0.15% and 1.35%
    sulphur_percent = rs.uniform(0.15, 1.35, count)
    return sulphur_percent

def _draw_dilithium_observations(count):
    rs = _initialise_randomstate(8)
    return  rs.uniform(25, 35, count)

def _draw_kryptonite_observations(count):
    rs = _initialise_randomstate(9)
    return rs.uniform(20, 25, count)
    
def _draw_unobtainium_observations(count):
    rs = _initialise_randomstate(10)
    return rs.uniform(0, 7, count)

def _draw_quartz_observations(count):
    rs = _initialise_randomstate(11)
    return rs.uniform(25, 35, count)

def _observe_recovery(sulphur_percent, outlier_probability):
    """Returns an array of metal recoveries.

    This method returns an array of metal recoveries given both
    an array of sulphur percentages and the probability of an
    outlier being observed.
    """
    recovery_percent = np.zeros_like(sulphur_percent)
    is_outlier = _is_outlier(outlier_probability, len(sulphur_percent))
    for index in range(0, len(recovery_percent)):
        if is_outlier[index]:
            recovery_percent [index]= _return_outlier_model_of_recovery(sulphur_percent[index])
        else:
            recovery_percent [index]=_noise_free_model_of_recovery(sulphur_percent[index])
    return recovery_percent

def _noise_free_model_of_recovery(sulphur):
    """This method returns a metal recovery for a given sulphur %."""
    return 74.81 - 6.81/sulphur

def _return_outlier_model_of_recovery(sulphur):
    return (74.81 - 6.81/sulphur)/3

def _is_outlier(outlier_probability, how_many):
    """Return true/false numpy array
    """
    rs = _initialise_randomstate(5)
    uniformly_distributed = rs.uniform(0, 1, how_many)
    is_outlier = np.zeros_like(uniformly_distributed)
    for index in range(0, len(is_outlier)):
        is_outlier[index]=uniformly_distributed[index]>(1-outlier_probability)
    return is_outlier

def add_gaussian_noise(noise_free_input, mean, sigma):
    """Adds gaussian noise to vector, given mean and sigma
    """
    bins = len(noise_free_input)
    noise = np.random.normal(mean, sigma, bins)
    return noise_free_input + noise


def gaussian_fwhm_pdf(X, height, x_position, fwhm):
    """Returns guassian probability distribution function, given FWHM

    This computes a gaussian probability density function (pdf) given a
    Full Width at Half Maximum (FWHM) instead of standard deviation, and
    scales it by the height parameters.  If the height is one, then the
    area of the guassian will also be unity, as required for a pdf, and
    for preserving area when used as an impulse response function in
    convolution operations.

    Note, this returns the function, it does not sample from the
    distribution.

    """
    return gaussian_pdf(X, height, x_position, fwhm / (2 * math.sqrt(2 * math.log(2))))


def gaussian_pdf(X, area, x_position, standard_deviation):
    """Returns gaussian probability distribution function multiplied by area.

    This computes a gaussian with unit area and multiplies it
    by the area parameter.  It is translated to be centered
    on x_position and has the width specified by standard_deviation.

    Unit area gaussians are used as probability distributions functions,
    and are also important in convolutions, as area of the convolution
    of two functions is the product of their areas.  If it is important
    for the convolution to preserve area of a function when convolved
    with a gaussian then that gaussian needs to have unit area.  Preserving
    area also implies conservation of energy in many physical models.

    It can be shown that the integral of the gaussian function is unity
    when the guassian's height is scaled as a function of standard_deviation
    as:

        height_scaling = 1/(standard_deviation*sqrt(2*pi))

    So this function multiplies the height of the guassian by this factor and
    then multiplies this result by the area parameter that is passed in.

    If area parameter is 1, then the height of this gaussian with also
    be 1 for all standard deviations, otherwise the area will be set by the
    area parameter.  The relationship between height and area, and the scaling
    of height by the second parameter below, will be made clearer by
    also studying the guassian function.

    """
    return gaussian(X, area / (standard_deviation * math.sqrt(2 * math.pi)), x_position,
                    standard_deviation)


def gaussian(X, height, x_position, standard_deviation):
    """Return standard gaussian function

    This is the unnormalised gaussian function

        f(x)=height*exp(-(x-x_position)^2/(2*standard_deviation^2))

    Parameters
    ----------
    height:
        This is the maximum of the gaussian peak.

        This function does not normalise to constant area, the caller
        must do this if this is what they want.

    x_position:
        This is the x position of the centre of the gaussian.  If the
        guassian is being used to apply the impulse response of an
        instrument applied to an XRD reflection, then this will be the
        two-theta position of the peak.

    standard_deviation:
        The standard deviation of the guassian curve.

        If this function is being applied in spectroscopy, optics or
        electrical engineering, it is common for gaussians to be
        defined in terms of Full Width at Half Maximum (FWHM), which
        is the width of the peak when the height drops to half
        of the peak height, specified by the height parameter.  If
        the x-axis represents frequency, and the function height
        is proportional to energy or power, then this will be the
        gaussian's bandwidth, that is, the width between the -3db points.

        To convert from FWHM to standard deviation use the relationship:
            FWHM = 2*sqrt(2*log(2)) * standard_deviation

    Returns
    -------
    double:
        Evaluated gaussian function.

    """

    return height * math.e**(-(X - x_position)**2 / 2 / standard_deviation**2)

class MultichannelXAxis:
    """Set up an X axis for isntrument

    This object is set up with three inputs, min_x is the minimum value
    on the axis.  In the example I've chosen 5.  The max_x
    value is the highest value on the x axis, and spacing is
    the x spacing between channels.  In the example I've chosen
    a max_x of 90 and spacing of 0.2.  The unit is two-theta
    degrees, and this unit (and the axis values) come from the
    world of x-ray diffraction (XRD).  We're describing the x-axis
    of a low resolution XRD instrument.

    The object's as_vector method can return the x_axis as an array
    of numbers using numpy's linspace method, which we've already used
    for plotting and other purposes.
    """

    def __init__(self, min_x, max_x, spacing):
        self._min = min_x
        self._max = max_x
        self._spacing = spacing
        self._channel_count = \
            round((self.max - self.min) / self.spacing + 1)
        self._label = "r'$2\theta$ (degrees)"

    @property
    def min(self):
        """Return minimum two-theta for diffractogram x-axis."""
        return self._min

    @property
    def max(self):
        """Return maximum two-theta for diffractogram x-axis."""
        return self._max

    @property
    def spacing(self):
        """Return channel spacing in two-theta for diffractogram x-axis."""

        return self._spacing

    @property
    def channel_count(self):
        """Return the count of channels in this diffractogram."""
        return self._channel_count

    @property
    def label(self):
        """Return the x-axis label, for use with plot and report generation."""
        return self._label

    @property
    def as_vector(self):
        """Return a numpy vector containing two-theta values for each channel."""
        x_axis_vector = np.linspace(self.min, self.max, self.channel_count)
        return x_axis_vector

def _apply_convolution_kernals(x_axis_vector, intensity, two_theta_angle,
                               instrument_broadening_fwhm,
                               reflection_broadening_fwhm):
    """Apply gaussian kernel for instrument broadening only."""
        
    def _add_gaussian_fwhms(fwhm1, fwhm2):
        sigma_fwhm_conversion_constant = 2*math.sqrt(2*math.log(2))
        sigma_1 = fwhm1/sigma_fwhm_conversion_constant
        sigma_2 = fwhm2/sigma_fwhm_conversion_constant
        #squares of std_dev (ie sigma^2 which is variance) are additive
        sigma_summed = math.sqrt(sigma_1*sigma_1 + sigma_2*sigma_2)
        return sigma_summed*sigma_fwhm_conversion_constant
        
    fwhm = _add_gaussian_fwhms (instrument_broadening_fwhm,
                                    reflection_broadening_fwhm)
    return gaussian_fwhm_pdf(x_axis_vector, intensity, two_theta_angle,
                                 fwhm)

def create_templates_matrix():
    """Create templates for four test pure components.

    This creates templates for quartz, dilithium, kryptonite and
    unobtainium, in that order.  The templates are returned
    in an array where the first column is quartz, and the last is
    unobtainium.  If you plot them, you'll see gently varying 
    squiggly lines.
    """
    # Create a templates matrix containing space for four templates, plus
    # a column of ones.
    x_axis = MultichannelXAxis(5, 90, 0.2)
    template_count = 4
    templates_matrix = np.zeros((x_axis.channel_count, template_count+1))
    # set 4 two-theta units of instrument broadening
    instrument_broadening = 4

    # create a tuple for each reflection, and add it to a list.  The loop
    # then grabs each reflection from the list and then adds it to the
    # template.  The first value in the tuple is intensity, the second
    # two-theta angle and the third is how much broadening to apply.
    Reflection = namedtuple('Reflection', ('intensity', 'two_theta', 'broadening'))
    quartz_reflections = []
    quartz_reflections.append (Reflection(intensity=10.0, two_theta=25.0, broadening=3.0))
    quartz_reflections.append (Reflection(13.0, 38.0, 6.0))
    quartz_reflections.append (Reflection(10.0, 43.0, 2.0))
    quartz_reflections.append (Reflection(25.0, 60, 2.0))
    
    dilithium_reflections = []
    dilithium_reflections.append (Reflection(25.0, 80, 1.0))

    kryptonite_reflections = []
    #kryptonite_reflections.append (Reflection(intensity=12.0, two_theta=25.0, broadening=9.0))
    kryptonite_reflections.append (Reflection(17.0, 12.0, 1.0))
    kryptonite_reflections.append (Reflection(19.0, 43.0, 12.0))
    #kryptonite_reflections.append (Reflection(4.0, 70, 2.0))
    #kryptonite_reflections.append (Reflection(32.0, 74, 2.0))

    unobtainium_reflections = []
    #unobtainium_reflections.append (Reflection(intensity=4.0, two_theta=25.0, broadening=12.0))
    unobtainium_reflections.append (Reflection(5.0, 18.0, 6.0))
    unobtainium_reflections.append (Reflection(1.0, 23.0, 1.0))
    unobtainium_reflections.append (Reflection(5.0, 31.0, 2.0))
    unobtainium_reflections.append (Reflection(3.0, 55.0, 6.0))
    unobtainium_reflections.append (Reflection(7.0, 58.0, 1.0))
    #unobtainium_reflections.append (Reflection(5.0, 80, 2.0))

    phases=[]
    # create four phases
    phases.append(quartz_reflections)
    phases.append(dilithium_reflections)
    phases.append(kryptonite_reflections)
    phases.append(unobtainium_reflections)

    for phase_idx in range(0, template_count):
        for a_reflection in phases[phase_idx]:
            contribution_of_this_reflection = \
                _apply_convolution_kernals(
                    x_axis.as_vector,
                    a_reflection.intensity,
                    a_reflection.two_theta,
                    instrument_broadening,
                    a_reflection.broadening)
            templates_matrix[:, phase_idx] += \
                contribution_of_this_reflection  

    # set the last column to be all ones
    templates_matrix[:, template_count] = \
        np.ones(x_axis.channel_count)

    return templates_matrix

def create_composition_dataframe(observations_count):
    """Create a dataframe of observations of drilling samples

    Returns:
        Pandas DataFrame with observations_count observations.
        The dataframe has four columns representing the amount
        of quartz, dilithium, kryptonite and unobtainium present.

        These values are drawn from uniform distributions."""
    unobtainium = _draw_unobtainium_observations (observations_count)
    dilithium = _draw_dilithium_observations(observations_count)
    kryptonite = _draw_kryptonite_observations(observations_count)
    quartz = _draw_quartz_observations(observations_count)

    # Create clusters by imposing a relationship between quartz
    # and dilithium.
    
    for observation_idx in range(0, observations_count):
        if quartz[observation_idx] > 30:
            dilithium[observation_idx] = 5

        if dilithium[observation_idx] > 30:
            quartz[observation_idx] = 5

    return pd.DataFrame({'Quartz': quartz,
                        'Dilithium': dilithium,
                        'Kryptonite': kryptonite,
                        'Unobtainium': unobtainium})

def create_observations(compositions_dataframe, templates):
    """Create a new array containing synthetic observations"""

    observations_count = len(compositions_dataframe)
    channels_count = len(templates[:,0])
    observations_matrix = np.zeros((channels_count, observations_count))
    for observation_idx in range (0, observations_count):
        observations_matrix[:, observation_idx] = \
            templates[:,0]*compositions_dataframe['Quartz'][observation_idx] + \
            templates[:,1]*compositions_dataframe['Dilithium'][observation_idx] + \
            templates[:,2]*compositions_dataframe['Kryptonite'][observation_idx] + \
            templates[:,3]*compositions_dataframe['Unobtainium'][observation_idx]
        # add gaussian noise.  If you have time, try increasing this and watch
        # prediction performance fall over.
        observations_matrix[:, observation_idx] = \
            add_gaussian_noise(observations_matrix[:, observation_idx], 10, 3)
    
    return observations_matrix
